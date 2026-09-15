
# 📊 Enterprise GCP Cost Anomaly & Data Governance Pipeline

[![FinOps Framework](https://img.shields.io/badge/FinOps-Framework_v1.0-blue.svg)](https://www.finops.org/)
[![Google Cloud](https://img.shields.io/badge/GCP-Billing_Export-4285F4.svg)](https://cloud.google.com/billing)
[![Excel / Sheets](https://img.shields.io/badge/Workbook-Production_v2.0-1D6F42.svg)](./workbook/capstone1-enterprise-tracker.xlsx)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB.svg)](https://www.python.org/)

An enterprise-grade **Cloud Financial Operations (FinOps) & Statistical Anomaly Engine** built to ingest raw GCP billing exports, apply automated data governance (de-duplication, null dimension assertion, credit unblending), and enforce **3-Sigma Statistical Process Control (+3σ)** guardrails to detect runaway cloud spend spikes.

---

## 🔒 Data Privacy & Policy Compliance Disclaimer

> **Note on Data Privacy & Compliance:** All datasets, transaction IDs, project names, business units, and financial figures used in this repository are **100% synthetic mock data** created solely for educational, analytical demonstration, and portfolio purposes. No real customer data, proprietary billing exports, or confidential Google Cloud Platform (GCP) records were used, accessed, or disclosed. This project complies fully with all data privacy guidelines and policy standards.

---

## 🏛️ System Architecture

```text
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                      ENTERPRISE FINOPS DATA & ANOMALY PIPELINE                         │
 ├────────────────────────────────────────────────────────────────────────────────────────┤
 │ [1. RAW BILLING LOGS] ──► [2. GOVERNANCE PIPELINE] ──► [3. STATISTICAL PROCESS CONTROL]│
 │ 500 Enterprise Events      Automated De-duplication   Baseline Mean (\$6,136.67)            │
 │ Multi-Project & Regions    Null BU Imputation         Sample StdDev (\$9,466.29)          │
 │                            Credit Unblending          3-Sigma UCL Bound (\$34,535.54)     │
 ├────────────────────────────────────────────────────────────────────────────────────────┤
 │                            └──► [4. EXECUTIVE ANOMALY COMMAND CENTER]                  │
 │                                 Z-Score Escalation Engine & Incident Post-Mortem Report│
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Executive Summary & Key Metrics

During an automated audit of **500 enterprise billing events** spanning 5 core business units (*Enterprise SaaS, Global Logistics, Hardware & IoT, Pro Services, E-Commerce Engine*), the **3-Sigma Statistical Anomaly Engine** detected **5 critical cost spikes** totaling **$313,900.00** in unbudgeted spend.

While standard operational activities maintained a stable baseline median of **$4,200.00**, runaway compute scaling and unindexed BigQuery queries drove the overall arithmetic mean up to **$6,136.67**, producing a **1.46x positive skewness ratio**.

| Metric | Evaluated Benchmark | Analyst Interpretation |
| :--- | :--- | :--- |
| **Total Gross Spend** | **$3,037,650.00** | Total cumulative raw billing volume across 500 line items |
| **Baseline Mean ($\mu$)** | **$6,136.67** | Arithmetic balance point (heavily skewed by upper tail spikes) |
| **Typical Median (50th %ile)** | **$4,200.00** | Outlier-resistant typical operational spend baseline |
| **Sample StdDev ($\sigma$)** | **$9,466.29** | Standard operational volatility in original dollar units |
| **3-Sigma UCL (+3$\sigma$)** | **$34,535.54** | Upper statistical control boundary ($\mu + 3\sigma$) |
| **Flagged 3-Sigma Anomalies** | **5 Incidents ($313,900.00)** | Critical spikes triggering immediate engineering escalation |

---

## 🔍 Incident Post-Mortem: Top 5 Outlier Cost Spikes

All 5 flagged incidents breached the **$34,535.54 (+3σ)** Statistical Upper Control Limit, exhibiting extreme Z-scores ranging from **+4.34σ to +8.05σ** above baseline:

1. **Incident #1 — BigQuery Slot Spike ($68,500.00 | Z-Score: +6.59σ)**
   * **Business Unit:** Enterprise SaaS (`prj-enterprise-saas-102`)
   * **Root Cause:** An unoptimized analytical loop executed full-table scans over 450TB of unindexed log tables.
2. **Incident #2 — Compute Engine GPU Spike ($82,400.00 | Z-Score: +8.05σ)**
   * **Business Unit:** E-Commerce Engine (`prj-e-commerce-engine-101`)
   * **Root Cause:** Managed Instance Group (MIG) failed to trigger scale-in policies during off-peak weekend hours.
3. **Incident #3 — GKE Data Egress Loop ($54,200.00 | Z-Score: +5.08σ)**
   * **Business Unit:** Global Logistics (`prj-global-logistics-103`)
   * **Root Cause:** Misconfigured Kubernetes service mesh routed inter-pod microservice traffic across public internet gateways.
4. **Incident #4 — Cloud SQL Replication Surge ($47,800.00 | Z-Score: +4.40σ)**
   * **Business Unit:** Hardware & IoT (`prj-hardware-and-iot-104`)
   * **Root Cause:** Unexpected cross-region read-replica synchronization triggered during a regional failover test.
5. **Incident #5 — BigQuery Full Table Scan ($61,000.00 | Z-Score: +5.79σ)**
   * **Business Unit:** Pro Services (`prj-pro-services-103`)
   * **Root Cause:** Unthrottled ad-hoc queries executed against unpartitioned billing export partitions.

---

## 🧼 Data Governance & Quality Pipeline Rules

To prevent corrupted reporting and double-counting, the pipeline applies three automated governance rules:

1. **De-Duplication Audit:**
   $$\text{Rule: } \text{IF}(\text{COUNTIF}(\text{TXN\_Range}, \text{TXN\_ID}) > 1, \text{"⚠️ DUPLICATE"}, \text{"UNIQUE"})$$
   *Flags duplicate event retries (e.g., `TXN-6002`, `TXN-6007`).*

2. **Null Business Unit Assertion:**
   $$\text{Rule: } \text{IF}(\text{OR}(\text{ISBLANK}(\text{BU}), \text{BU} = ""), \text{"Unassigned"}, \text{BU})$$
   *Prevents orphan spend in pivot tables by asserting default dimension tags.*

3. **Credit Unblending & Classification:**
   $$\text{Rule: } \text{IF}(\text{Spend} < 0, \text{"CREDIT / ADJUSTMENT"}, \text{"STANDARD USAGE"})$$
   *Separates promotional credits and SLA outage refunds from true usage fees.*

---

## 🚀 Recommended FinOps Remediation Plan

1. **Enforce BigQuery Quotas:** Set hard daily slot usage caps ($5,000/day limit per user group) in GCP IAM.
2. **Cap Autoscaling Groups:** Configure maximum instance bounds on Compute Engine instance groups during non-business hours.
3. **Real-time Webhook Guards:** Connect the 3-Sigma Anomaly Engine to Slack/PagerDuty webhooks for notifications within 15 minutes of a UCL breach.
4. **Unblended Credit Allocation:** Allocate $3,500.00 in committed use discount credits directly against Enterprise SaaS compute costs.

---

## 🛠️ Repository Navigation & Files

* [`/workbook/capstone1-enterprise-tracker.xlsx`](./workbook/capstone1-enterprise-tracker.xlsx) — Full 5-tab production workbook.
* [`/docs/data_dictionary.md`](./docs/data_dictionary.md) — Column schema definitions & analytical formulas.
* [`/docs/incident_post_mortem.md`](./docs/incident_post_mortem.md) — In-depth post-mortem investigation report.
* [`/src/data_cleaning_pipeline.py`](./src/data_cleaning_pipeline.py) — Python implementation of the governance logic.
```
