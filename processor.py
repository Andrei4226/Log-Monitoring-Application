def process_list(logs_list):
    """
    :param logs_list: a list with formatted data
    :return: a list with matched logs
    """
    job_starts = {}
    job_data = []

    for log in logs_list:
        pid = log["pid"]
        if log["status"] == "START":
            job_starts[pid] = log
        elif log["status"] == "END" and pid in job_starts:
            start_log = job_starts.pop(pid)
            duration = (log["timestamp"] - start_log["timestamp"]).total_seconds()
            job_data.append({
                "pid": pid,
                "description": start_log["description"],
                "start": start_log["timestamp"],
                "end": log["timestamp"],
                "duration": duration
            })
    return job_data, job_starts
