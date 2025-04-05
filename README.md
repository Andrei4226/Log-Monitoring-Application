# Log-Monitoring-Application

---

## Description
This Python application monitors a log file containing job entries, calculates job durations and generates a report with warnings, errors, or critical messages if jobs exceed defined thresholds or if they remain unfinished.

---

## Features

- **Log Parsing:** Reads a structured log file with entries in the format:  
  `HH:MM:SS, <job description>, <START or END>, <PID>`
- **Job Matching:** Pairs each job's START and END entries by unique PID.
- **Duration Calculation:** Computes the duration of each job.
- **Reporting:** 
  - Logs a **WARNING** if a job takes longer than 5 minutes.
  - Logs an **ERROR** if a job takes longer than 10 minutes.
  - Logs a **CRITICAL** message for jobs that are unfinished (missing an END).
- **Output:** Generates a report file with the results.

---

## How to Run

1. Place your log file in the `dataIN` folder as `logs.log`.
2. Run the main script:

   ```bash
   python main.py

--- 

## How to Run Tests

- Run the main script:

   ```bash
   python -m unittest discover tests

---
