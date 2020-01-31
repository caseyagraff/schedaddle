"""
job.py
"""

import subprocess


class Job:
    def __init__(self, job, save_file=None):
        self.job = job
        self.save_file = save_file

    def run(self):
        print("Running job...")
        complete = subprocess.run(
            ["python"] + self.job.split(" "),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        if self.save_file:
            with open(self.save_file, "wb") as f_out:
                f_out.write(complete.stdout)
        else:
            print(complete.stdout.decode().rstrip())

        print(f'Job "{self.job}" finished.')
