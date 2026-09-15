

import pandas as pd
import numpy as np


def run_data_governance_pipeline(input_file: str, output_file: str) -> pd.DataFrame
    # 1. Load Raw Dataset
    df = pd.read_excel(input_file, sheet_name="Raw Enterprise Billing Data")

    # 2. Task 1: De-duplication Audit
    duplicate_counts = df['TXN ID'].value_counts()
    df['Duplicate Flag'] = df['TXN ID'].apply(
        lambda x: "⚠️ DUPLICATE" if duplicate_counts[x] > 1 else "UNIQUE"
    )

    # 3. Task 2: Null Business Unit Assertion
    df['Cleaned Business Unit'] = df['Raw Business Unit'].fillna("Unassigned")
    df['Cleaned Business Unit'] = df['Cleaned Business Unit'].replace("", "Unassigned")

    # 4. Task 3: Credit Unblending & Classification
    df['Line Item Type'] = np.where(
        df['Raw Spend ($)'] < 0,
        "CREDIT / ADJUSTMENT",
        "STANDARD USAGE"
    )

    # 5. Task 4: Statistical 3-Sigma Z-Score Engine
    mean_spend = df['Raw Spend ($)'].mean()
    std_spend = df['Raw Spend ($)'].std(ddof=1)  # Sample StdDev (n-1)
    ucl_3sigma = mean_spend + (3 * std_spend)

    df['Z_Score'] = (df['Raw Spend ($)'] - mean_spend) / std_spend
    df['3_Sigma_Status'] = np.where(
        df['Raw Spend ($)'] > ucl_3sigma,
        "🚨 ANOMALY SPIKE",
        np.where(df['Raw Spend ($)'] < 0, "💳 CREDIT", "NORMAL")
    )

    # Save cleaned pipeline output
    df.to_csv(output_file, index=False)
    print(f"Pipeline executed successfully. Cleaned data saved to {output_file}")
    print(
        f"Summary: Baseline Mean=${mean_spend:,.2f} | StdDev=${std_spend:,.2f} | 3σ UCL=${ucl_3sigma:,.2f}"
    )
    return df


if __name__ == "__main__":
    run_data_governance_pipeline(
        input_file="../workbook/capstone1-enterprise-tracker.xlsx",
        output_file="../data/processed/cleaned_billing_pipeline.csv"
    )
