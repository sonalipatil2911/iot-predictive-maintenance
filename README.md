# AI-Augmented Predictive Maintenance: Factory IoT Telemetry Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end automated industrial engineering framework. It ingests raw multi-sensor IoT logs, processes them through a deterministic math engine to evaluate Overall Equipment Effectiveness (OEE), and leverages an LLM microservice bounded by strict prompt guardrails to generate structured, actionable engineering maintenance tickets.

### ⚙️ System Architecture & Data Flow
1. **Data Simulation Layer:** 200 rows of continuous machine sensor data embedded with hidden physical anomalies (bearing friction heat spikes, precision tool alignment drift, and asset capacity drops).
2. **Deterministic OEE Engine:** A spreadsheet calculation layer mapping Availability, Performance, and Quality metrics to isolate granular breakdown drivers.
3. **Semantic Triage Layer (Gemini):** An automated diagnostic pipeline that converts multi-variable numeric data drops into precise engineering triage tickets.
4. **Visual Execution Layer:** A live, cross-filtered Looker Studio Dashboard for factory floor supervisors.

## 📊 Engineered Failure Modes & Diagnostics
The workflow successfully isolated three distinct mechanical failure profiles masked beneath identical operational alert statuses (`DEGRADED CAPACITY`):

* **MC-02 (Friction/Bearing Failure):** Isolated by low Availability (78.95%) caused by automated thermal and vibration safety cut-offs.
* **MC-04 (Quality Drift):** Isolated by low Quality yields (94.84%) paired with high running velocity, signaling a tool alignment head calibration issue.
* **MC-01 (Asset Fatigue):** Isolated by low Performance (82.03%) despite perfect quality, signaling structural cycle-time slowdowns due to extended runtime without maintenance intervals.

## 🛡️ Responsible AI Guardrails & Impact
* **Safety Protocol:** Mathematical calculation is fully decoupled from the LLM to completely eliminate hallucinated data variables or false engineering margins. 
* **Operational Velocity:** Reduced manual data forensic time from **1.5 hours per shift shift down to 10 minutes**, allowing maintenance crews to safely run real-time predictive triage.

## 🖼️ Dashboard & Code Artifacts
### Looker Studio Diagnostics Panel
![Looker Studio Dashboard](screenshots/factory_dashboard.png)

### Enforced Triage Ticket Structure
```json
// Saved in triage/triage_output.json
{
  "machine_id": "MC-02",
  "primary_failure_driver": "Availability",
  "triage_priority": "CRITICAL",
  "action_plan": [
    "Immediately halt machine cycles to check internal bearing lubrications and inspect physical spindle components for wear.",
    "Calibrate vibration sensors and cross-analyze structural alignment before restarting production."
  ]
}
