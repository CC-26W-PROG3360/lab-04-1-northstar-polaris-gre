# 🛰️ Northstar Global Routing Engine (GRE)
_Project Polaris | Version 4.0-Alpha_

Our drones are currently managing 15% of all last-mile deliveries globally. The code in this repository controls the Global Routing Engine (GRE)—the brain behind drone velocity, telemetry, and flight-path integrity.

    ⚠️ MISSION CRITICAL: Failure to maintain the main branch stability results in immediate grounding of the fleet. Every minute of downtime costs Northstar $10,000.

## 🏗️ System Overview

    `engine/router.py`: Manages velocity and safety constraints.

    `engine/telemetry.py`: Handles GPS and status reporting formats.

    `tests/test_integrity.py`: The "Circuit Breaker" suite. If these tests fail, the code cannot be deployed.

## 🛠️ Installation & Setup

To get the GRE running on your local workstation:

    Clone the repository:
```bash
    git clone {YOUR GITHUB URL}

    cd lab-04-northstar-gre
```
    Run the Integrity Suite:
```bash

    python tests/test_integrity.py

## 🚀 Weekly Assignment: Workflow Trials

This week, Northstar is evaluating two branching strategies to increase our deployment velocity. Your team has been assigned one of the following:

### Option A: The Git Flow Protocol

    Goal: Maintain strict isolation for the new "Telemetry Upgrade."

    Workflow: feature/* → develop → release/* → main.

    The Challenge: Coordinate with other feature teams to avoid "Schema Drift" in telemetry.py.

### Option B: Trunk-Based Development (TBD)

    Goal: Enable "High-Speed Mode" using short-lived branches.

    Workflow: feature-fix → main (Merge via Pull Request).

    The Challenge: You must use the FEATURE_HIGH_SPEED environment variable. If you push raw speed increases without the toggle, the CI/CD pipeline will kill the build.

## 🚨 Emergency Protocols

    Merge Conflicts: If you hit a conflict, do not force push. Rebase onto the latest main or develop and resolve the logic according to the Northstar Engineering Handbook.

    Broken Build: If the GitHub Actions tab turns RED, all other development stops until the trunk is repaired.