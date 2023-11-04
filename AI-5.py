#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''Implement Greedy search algorithm for Job Scheduling Problem '''
def greedy_job_scheduling(jobs):
    # Sort the jobs in descending order of their deadlines
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    schedule = [None] * n  # Initialize the schedule as an empty list
    filled_slots = [False] * n  # Track which slots in the schedule are filled

    for i in range(n):
        deadline = jobs[i][2]
        for j in range(min(n, deadline) - 1, -1, -1):
            if not filled_slots[j]:
                schedule[j] = jobs[i]
                filled_slots[j] = True
                break

    # Filter out the empty slots
    schedule = [job for job in schedule if job is not None]

    return schedule

# Example usage:
jobs = [(1, 3, 3), (2, 2, 2), (3, 5, 5), (4, 1, 3), (5, 4, 2)]
scheduled_jobs = greedy_job_scheduling(jobs)
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job {job[0]} (Processing Time: {job[1]}, Deadline: {job[2]})")


# In[ ]:




