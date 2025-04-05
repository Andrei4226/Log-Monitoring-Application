import unittest
from datetime import datetime
from main import parse_log_file, process_list


class TestLogMonitoring(unittest.TestCase):

    # test the parse_log_file function with mocked data
    def test_parse_log_file(self):
        test_file = "tests/test_logs_log"
        with open(test_file, "w") as f:
            f.write("11:35:23,scheduled task 001,START,12345\n")
            f.write("11:36:23,scheduled task 001,END,12345\n")

        logs = parse_log_file(test_file)

        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[0]["status"], "START")
        self.assertEqual(logs[1]["status"], "END")
        self.assertEqual(logs[0]["pid"], "12345")

    # test the process_list function to find the matched jobs
    def test_process_list_duration(self):
        job_starts = {}
        logs = [
            {"timestamp": datetime.strptime("11:00:21", "%H:%M:%S"),
             "description": "scheduled task 031",
             "status": "START",
             "pid": "57671"},
            {"timestamp": datetime.strptime("11:01:30", "%H:%M:%S"),
             "description": "scheduled task 031",
             "status": "END",
             "pid": "57671"},
        ]
        for log in logs:
            pid = log["pid"]
            if log["status"] == "START":
                job_starts[pid] = log
            elif log["status"] == "END" and pid in job_starts:
                job_starts.pop(pid)

        jobs_data, _ = process_list(logs)

        self.assertEqual(len(job_starts), 0)
        self.assertEqual(jobs_data[0]["pid"], "57671")
        self.assertEqual(jobs_data[0]["duration"], 69.0)

    #  test the process_list function to find the unmatched jobs
    def test_unfinished_jobs(self):
        logs = [
            {
                "timestamp": datetime.strptime("12:00:00", "%H:%M:%S"),
                "description": "background job test",
                "status": "START",
                "pid": "99999"
            }
        ]

        _, unmatched_jobs = process_list(logs)

        self.assertIn("99999", unmatched_jobs)
        self.assertEqual(unmatched_jobs["99999"]["description"], "background job test")
        self.assertEqual(unmatched_jobs["99999"]["timestamp"], datetime.strptime("12:00:00", "%H:%M:%S"))


if __name__ == '__main__':
    unittest.main()
