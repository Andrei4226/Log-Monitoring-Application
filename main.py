from generate import generate_report
from parser import parse_log_file
from processor import process_list


def main():
    input_file = "dataIN/logs.log"
    output_file = "dataOUT/report.txt"

    logs = parse_log_file(input_file)
    jobs, unmatched_jobs = process_list(logs)
    generate_report(jobs, output_file, unmatched_jobs)


if __name__ == "__main__":
    main()
