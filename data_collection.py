import mcf_scraper as mcfs
job = "data analyst"
df = mcfs.get_jobs(job, 309)
df.to_csv('jobs.csv')

