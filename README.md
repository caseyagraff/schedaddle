# Schedaddle

A simple out-of-processes Python job scheduler.

## Running the scheduler

#### 1. `python server.py <num_workers>`

    Starts the job scheduler (server.py) with a <num_workers> process pool.

#### 2. `python sender.py <job_file>`

    Send the jobs listed in <job_file> to the scheduler.

    The expected format of `<job_file>` is one job per line:

        `python test_job.py`

    You may proved a file to save the job's output to by adding a path after a comma:

        `python test_job.py ./job.out`

    Each job will be run in a subprocess in the same location as the server.

## Example Run (with provided test job and job_file)
    * `python server.py 2`
    * `python sender.py test_jobs.txt`

    This will start a server with two workers and then run three jobs, each of which
    print a message. The third job (job c) will be saved to the file job_c.out.
