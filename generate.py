import logging
import os
MINUTES_PER_HOUR = 60
MINUTES_FOR_WARNING = 5
MINUTES_FOR_ERROR = 10


def generate_report(jobs, output_file, unmatched_jobs=None):
    """
    :param unmatched_jobs: a list with unmatched logs
    :param jobs: a list with matched logs
    :param output_file: the report file
    """
    lines = []

    for job in jobs:
        message = (
            f"Description Job: {job['description']}, "
            f"PID: {job['pid']}, "
            f"Duration(minutes): {job['duration'] / MINUTES_PER_HOUR:.2f}"
        )
        if job["duration"] / MINUTES_PER_HOUR > MINUTES_FOR_ERROR:
            logging.error(message)
            lines.append(f"ERROR: {message}")
        elif job["duration"] / MINUTES_PER_HOUR > MINUTES_FOR_WARNING:
            logging.warning(message)
            lines.append(f"WARNING: {message}")

    if unmatched_jobs:
        for pid, job in unmatched_jobs.items():
            message = (
                f"Unfinished Job: Description: {job['description']}, "
                f"PID: {pid}, "
                f"Started at: {job['timestamp'].strftime('%H:%M:%S')}"
            )
            logging.critical(message)
            lines.append(message)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        for line in lines:
            f.write(line + "\n")
