```
# Data Dictionary &amp; Formula Reference

&gt; **Disclaimer:** All data fields, project names, and financial metrics in this document are derived from synthetic mock data generated for educational and portfolio demonstration purposes.

## Data Pipeline Schema (`Master Cleaned Data Pipeline`)

| Field Name | Data Type | Source / Formula | Description |
| :--- | :--- | :--- | :--- |
| `TXN ID` | String | Raw Export | Unique transaction event identifier |
| `Date` | Date | Raw Export | Transaction event timestamp |
| `Project ID` | String | Raw Export | GCP Project ID |
| `Raw Business Unit` | String | Raw Export | Uncleaned business unit tag |
| `Region` | String | Raw Export | GCP deployment region |
| `GCP Service` | String | Raw Export | GCP service classification |
| `Raw Spend ($)` | Currency | Raw Export | Line item cost in USD |
| `Duplicate Flag` | Formula | `=IF(COUNTIF($A$5:$A$504, A5)&gt;1, "⚠️ DUPLICATE", "UNIQUE")` | Automated duplicate audit check |
| `Cleaned Business Unit` | Formula | `=IF(OR(ISBLANK(D5), D5=""), "Unassigned", D5)` | Null dimension assertion rule |
| `Line Item Type` | Formula | `=IF(G5&lt;0, "CREDIT / ADJUSTMENT", "STANDARD USAGE")` | Credit vs. usage classification |

## Key Formulas &amp; Statistical Definitions

* **Baseline Mean ($\mu$):** `=AVERAGE('Master Cleaned Data Pipeline'!G5:G504)` ($6,136.67)
* **Typical Median (50th %ile):** `=MEDIAN('Master Cleaned Data Pipeline'!G5:G504)` ($4,200.00)
* **Sample Volatility ($\sigma$):** `=STDEV.S('Master Cleaned Data Pipeline'!G5:G504)` ($9,466.29)
* **Sample Variance ($S^2$):** `=VAR.S('Master Cleaned Data Pipeline'!G5:G504)` (89,610,678.16)
* **3-Sigma Upper Control Limit (UCL):** `=\mu + (3 * \sigma)` ($34,535.54)
* **Z-Score Statistical Distance:** `=(Line_Item_Spend - Mean) / StdDev`

```


