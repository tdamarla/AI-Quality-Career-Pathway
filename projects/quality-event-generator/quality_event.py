event_id = "QE-2026-001"
event_type = "Protocol Deviation"
gxp_area = "GCP"
severity = "Major"
risk_score = 8
status = "Open"

if risk_score >= 8:
    risk_level = "High"
elif risk_score >= 5:
    risk_level = "Medium"
else:
    risk_level = "Low"

print("QUALITY EVENT")
print("------------------------")
print("Event ID:", event_id)
print("Event Type:", event_type)
print("GxP Area:", gxp_area)
print("Severity:", severity)
print("Risk Score:", risk_score)
print("Risk Level:", risk_level)
print("Status:", status)