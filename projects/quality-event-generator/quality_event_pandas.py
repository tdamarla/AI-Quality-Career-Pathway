from pathlib import Path

import pandas as pd


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