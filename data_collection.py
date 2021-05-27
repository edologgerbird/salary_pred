import mcf_scraper as mcfs
job = "data scientist"
df = mcfs.get_jobs(job, 2)
df.to_csv('jobs.csv')

