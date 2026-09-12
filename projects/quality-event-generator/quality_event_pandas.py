from pathlib import Path

import pandas as pd

import matplotlib.pyplot as plt

def classify_risk(risk_score):
    if not 0 <= risk_score <= 10:
        return "Invalid"

    if risk_score >= 8:
        return "High"
    elif risk_score >= 5:
        return "Medium"
    else:
        return "Low"


data_file = (
    Path(__file__).resolve().parents[2]
    / "datasets"
    / "quality_events.csv"
)

df = pd.read_csv(data_file)

# Apply the risk classification rule to every row
df["risk_level"] = df["risk_score"].apply(classify_risk)

# Identify invalid records
invalid_df = df[df["risk_level"] == "Invalid"]

# Keep only valid records for Quality analytics
valid_df = df[df["risk_level"] != "Invalid"]

print("QUALITY EVENT DATA")
print("------------------------------------------------------------")
print(df)

print()
print("DATA QUALITY EXCEPTIONS")
print("------------------------------------------------------------")

if len(invalid_df) > 0:
    print(
        invalid_df[
            ["event_id", "event_type", "risk_score"]
        ]
    )
else:
    print("No data quality exceptions found.")

total_records = len(df)
valid_events = len(valid_df)
data_quality_exceptions = len(invalid_df)

high_risk = (valid_df["risk_level"] == "High").sum()
medium_risk = (valid_df["risk_level"] == "Medium").sum()
low_risk = (valid_df["risk_level"] == "Low").sum()

open_events = (valid_df["status"] == "Open").sum()

if valid_events > 0:
    high_risk_percentage = (high_risk / valid_events) * 100
else:
    high_risk_percentage = 0

print()
print("QUALITY SUMMARY")
print("------------------------------------------------------------")
print("Total Records:", total_records)
print("Valid Events:", valid_events)
print("Data Quality Exceptions:", data_quality_exceptions)
print("High Risk:", high_risk)
print("Medium Risk:", medium_risk)
print("Low Risk:", low_risk)
print("Open Events:", open_events)
print("High Risk Percentage:", round(high_risk_percentage, 1), "%")
print()
print("EVENTS BY GXP AREA")
print("------------------------------------------------------------")
print(valid_df["gxp_area"].value_counts())

print()
print("EVENTS BY EVENT TYPE")
print("------------------------------------------------------------")
print(valid_df["event_type"].value_counts())

print()
print("EVENTS BY SEVERITY")
print("------------------------------------------------------------")
print(valid_df["severity"].value_counts())

print()
print("EVENTS BY STATUS")
print("------------------------------------------------------------")
print(valid_df["status"].value_counts())
print()
print("RISK DISTRIBUTION BY GXP AREA")
print("------------------------------------------------------------")

risk_by_gxp = (
    valid_df
    .groupby(["gxp_area", "risk_level"])
    .size()
    .unstack(fill_value=0)
)

print(risk_by_gxp)
print()
print("AVERAGE RISK SCORE BY GXP AREA")
print("------------------------------------------------------------")

average_risk_by_gxp = (
    valid_df
    .groupby("gxp_area")["risk_score"]
    .mean()
    .round(1)
)

print(average_risk_by_gxp)
output_dir = (
    Path(__file__).resolve().parent
    / "output"
)

output_dir.mkdir(exist_ok=True)

print()
print("CREATING CHART")
print("------------------------------------------------------------")

risk_by_gxp.plot(
    kind="bar"
)

plt.title("Risk Distribution by GxP Area")
plt.xlabel("GxP Area")
plt.ylabel("Number of Quality Events")
plt.xticks(rotation=0)
plt.tight_layout()

chart_file = output_dir / "risk_distribution_by_gxp.png"

plt.savefig(chart_file)
plt.close()

print("Chart saved to:", chart_file)
print()
print("QUALITY MANAGEMENT REVIEW SUMMARY")
print("------------------------------------------------------------")

open_event_rate = (open_events / valid_events) * 100 if valid_events > 0 else 0
data_quality_exception_rate = (
    data_quality_exceptions / total_records
) * 100 if total_records > 0 else 0

qmr_summary = pd.DataFrame(
    {
        "Metric": [
            "Total Records",
            "Valid Events",
            "Data Quality Exceptions",
            "Data Quality Exception Rate (%)",
            "High Risk Events",
            "High Risk Rate (%)",
            "Medium Risk Events",
            "Low Risk Events",
            "Open Events",
            "Open Event Rate (%)",
        ],
        "Value": [
            total_records,
            valid_events,
            data_quality_exceptions,
            round(data_quality_exception_rate, 1),
            high_risk,
            round(high_risk_percentage, 1),
            medium_risk,
            low_risk,
            open_events,
            round(open_event_rate, 1),
        ],
    }
)

print(qmr_summary.to_string(index=False))
qmr_summary_file = output_dir / "qmr_summary.csv"

qmr_summary.to_csv(
    qmr_summary_file,
    index=False
)

print()
print("QMR summary saved to:", qmr_summary_file)
risk_by_gxp_file = output_dir / "risk_by_gxp.csv"

risk_by_gxp.to_csv(risk_by_gxp_file)

print("GxP risk summary saved to:", risk_by_gxp_file)