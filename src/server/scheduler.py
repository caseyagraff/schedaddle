import multiprocessing
import threading
from queue import Queue

from job import Job

class Scheduler:
    def __init__(self, num_workers=1):
        self.num_workers = num_workers

        self.jobs = Queue()

        # self.original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        # signal.signal(signal.SIGINT, self.original_sigint_handler)

        self.pool = multiprocessing.Pool(self.num_workers)

    def start(self):
        print(f"Scheduler started with {self.num_workers} workers.")

        try:
            while True:
                job = self.jobs.get()

                # Will block when worker pool is empty
                self.pool.apply_async(job.run)
        except KeyboardInterrupt:
            print("\nSIGINT, terminating pool.")
            self.pool.terminate()
        else:
            print("Exiting normally")
            self.pool.close()

        self.pool.join()

        print("Scheduler stopping.")


    def add_job(self, job):
        split = job.rstrip().split(",")

        if len(split) > 1:
            job, save_file = split
        else:
            job, save_file = split[0], None

        self.jobs.put(Job(job, save_file))

        print(f'Added job "{job}" with save "{save_file}".')
