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
        "risk_score": 3,
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

print("QUALITY EVENTS")
print("------------------------------------------------------------")

for event in quality_events:

    if event["risk_score"] >= 8:
        risk_level = "High"
        high_risk += 1

    elif event["risk_score"] >= 5:
        risk_level = "Medium"
        medium_risk += 1

    else:
        risk_level = "Low"
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

total_events = len(quality_events)
high_risk_percentage = (high_risk / total_events) * 100

print()
print("QUALITY SUMMARY")
print("------------------------------------------------------------")
print("Total Events:", total_events)
print("High Risk:", high_risk)
print("Medium Risk:", medium_risk)
print("Low Risk:", low_risk)
print("Open Events:", open_events)
print("High Risk Percentage:", high_risk_percentage, "%")