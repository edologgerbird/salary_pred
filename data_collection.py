import mcf_scraper as mcfs

job = "data scientist"
df = mcfs.get_jobs(job, 212)
df.to_csv('jobs.csv')

