from datetime import datetime


def parse_log_file(file):
    """
    :param file: the input file that contains logs
    :return: a list with formatted data
    """
    logs_list = []
    with open(file, "r") as f:
        for line in f:
            arguments = line.strip().split(",")
            if len(arguments) != 4:
                continue
            # split the line into 4 variables and remove any whitespace from the beginning and end of each field
            time, description, status, pid = [arg.strip() for arg in arguments]
            timestamp = datetime.strptime(time, "%H:%M:%S")
            logs_list.append({
                "timestamp": timestamp,
                "description": description,
                "status": status,
                "pid": pid
            })
    return logs_list
