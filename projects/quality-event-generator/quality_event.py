def classify_risk(risk_score):
    if not 0 <= risk_score <= 10:
        raise ValueError("Risk score must be between 0 and 10.")

    if risk_score >= 8:
        return "High"
    elif risk_score >= 5:
        return "Medium"
    else:
        return "Low"


quality_events = [
    {
        "event_id": "QE-2026-001",
        "event_type": "Protocol Deviation",
        "gxp_area": "GCP",
        "severity": "Major",
        "risk_score": 8,
        "status": "Open"
    },
    {
        "event_id": "QE-2026-002",
        "event_type": "Audit Finding",
        "gxp_area": "GMP",
        "severity": "Major",
        "risk_score": 6,
        "status": "Open"
    },
    {
        "event_id": "QE-2026-003",
        "event_type": "CAPA",
        "gxp_area": "GCP",
        "severity": "Minor",
        "risk_score": 15,
        "status": "Closed"
    },
    {
        "event_id": "QE-2026-004",
        "event_type": "Inspection Finding",
        "gxp_area": "GVP",
        "severity": "Critical",
        "risk_score": 9,
        "status": "Open"
    }
]

high_risk = 0
medium_risk = 0
low_risk = 0
open_events = 0
valid_events = 0
data_quality_exceptions = 0

print("QUALITY EVENTS")
print("------------------------------------------------------------")

for event in quality_events:

    try:
        risk_level = classify_risk(event["risk_score"])

    except ValueError as error:
        data_quality_exceptions += 1

        print(
            event["event_id"],
            "| DATA QUALITY EXCEPTION |",
            error
        )

        continue

    valid_events += 1

    if risk_level == "High":
        high_risk += 1
    elif risk_level == "Medium":
        medium_risk += 1
    else:
        low_risk += 1

    if event["status"] == "Open":
        open_events += 1

    print(
        event["event_id"],
        "|",
        event["event_type"],
        "|",
        event["gxp_area"],
        "| Risk Score:",
        event["risk_score"],
        "|",
        risk_level
    )

total_records = len(quality_events)

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