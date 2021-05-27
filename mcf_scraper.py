# references: arapfaik


from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time
import pandas as pd


def get_jobs(keyword, num_jobs):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(executable_path=r'C:/Users/edmun/Dropbox/ds_projects/salary_pred/salary_pred/chromedriver.exe', chrome_options=options)  
    url = "https://www.mycareersfuture.gov.sg/search?search=" +keyword+ "&sortBy=new_posting_date&page=0"
    browser.get(url)
    

    loaded=False
    while not loaded:
        try:
            next_button = browser.find_element_by_xpath('.//span[@aria-label="Next"]')
            loaded=True
        except:
            time.sleep(3)

    #Scrape Job Links

    job_links=[]
    while len(job_links) < num_jobs:
        
        if len(job_links) >= num_jobs:
            break
        time.sleep(1)
        try:
            job_cards = browser.find_elements_by_xpath('.//div[@class="card relative"]')
        except NoSuchElementException:
            print("Scrape failed. Element card relative not found")

        for job in job_cards:
            link = job.find_element_by_xpath(".//a").get_attribute('href')
            job_links.append(link)
            print("Scraping Links in Progress: {}".format("" + str(len(job_links)) + "/" + str(num_jobs)))
            if len(job_links) >= num_jobs:
                break

        time.sleep(1)
        if len(job_links) < num_jobs:
            next_button = browser.find_element_by_xpath('.//span[@aria-label="Next"]')
            next_button.click()
            time.sleep(8)

        time.sleep(4)
    
    print("Link Scraping Completed")
    print("Scraping Job Information Now")

    jobs=[]

    for job_link in job_links:
        browser.get(job_link)
        time.sleep(3)

        loaded = False
        try_count = 0
        print("Scraping Job Infomation in Progress: {}".format("" + str(len(jobs)+1) + "/" + str(num_jobs)))
        while not loaded:
            try:
                company_name = browser.find_element_by_xpath('.//p[@data-cy="company-hire-info__company"]').text
                loaded = True
            except:
                time.sleep(2)
                try_count+=1
                if try_count >= 5:
                    browser.get(job_link)
                    time.sleep(2)
                    try_count=0

        job_title = browser.find_element_by_xpath('.//h1[@id="job_title"]').text
        job_post_id = browser.find_element_by_xpath('.//span[@data-cy="jobinfo__jobpostid--span"]').text
        try:
            address = browser.find_element_by_xpath('.//p[@id="address"]').text
        except NoSuchElementException:
            address = "NA"
        
        try:
            employment_type = browser.find_element_by_xpath('.//p[@id="employment_type"]').text
        except NoSuchElementException:
            employment_type = "NA"
        
        try:
            seniority = browser.find_element_by_xpath('.//p[@id="seniority"]').text
        except NoSuchElementException:
            seniority = "NA"
        
        try:
            min_exp = browser.find_element_by_xpath('.//p[@id="min_experience"]').text
        except NoSuchElementException:
            min_exp = "NA"
        
        try:
            job_cat = browser.find_element_by_xpath('.//p[@id="job-categories"]').text
        except NoSuchElementException:
            job_cat = "NA"
        
        try:       
            salary_range = browser.find_element_by_xpath('.//span[@class="salary_range dib f2-5 fw6 black-80"]').text
        except NoSuchElementException:
            salary_range = "NA"
        
        try:
            salary_unit = browser.find_element_by_xpath('.//span[@class="ttc salary_type dib f5 fw4 black-60 pr1 i pb"]').text
        except NoSuchElementException:
            salary_unit = "NA"

        try:
            date_posted = browser.find_element_by_xpath('.//span[@id="last_posted_date"]').text
        except NoSuchElementException:
            date_posted = "NA"
        
        try:
            date_expiry = browser.find_element_by_xpath('.//span[@id="expiry_date"]').text
        except NoSuchElementException:
            date_expiry = "NA"
        
        try:
            job_description = browser.find_element_by_xpath('.//div[@id="job_description"]').text
        except NoSuchElementException:
            job_description = "NA"

        jobs.append(
            {
                "company": company_name,
                "job_title": job_title,
                "listing_id":job_post_id,
                "address": address,
                "employment_type": employment_type,
                "seniority": seniority,
                "min_exp": min_exp,
                "job_cat": job_cat,
                "salary_range": salary_range,
                "salary_unit": salary_unit,
                "date_posted": date_posted,
                "date_expiry": date_expiry,
                "job_description": job_description,
            }
        )
    return pd.DataFrame(jobs)




