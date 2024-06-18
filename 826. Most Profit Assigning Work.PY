#You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
#difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
#worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
#Every worker can be assigned at most one job, but one job can be completed multiple times.
#For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
#Return the maximum profit we can achieve after assigning the workers to the jobs.


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort the workers by their abilities
        worker.sort()
        max_profit = 0
        total_profit = 0
        job_index = 0
        n = len(jobs)
        # Iterate through each worker
        for ability in worker:
            # While the current job can be done by this worker (i.e., difficulty is less than or equal to ability)
            while job_index < n and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the max profit that this worker can achieve
            total_profit += max_profit

        return total_profit