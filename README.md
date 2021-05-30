# Monthly Salary Estimator for Data-related Jobs in Singapore

## Project Overview

 Repository for the salary prediction project
 - Developed an estimator for the month salary of data-related jobs in Singapore (MAE ~ S$1345) to help jobseekers in the field of data negotiate their income upon landing the job.
 - Scraped about 300 job descriptions from MyCareersFuture using Python and Selenium
 - Created features from the open-text job descriptions to quantify the value companies put on relevant technologies related to data science (AWS, Python, SQL, R, Tableau, Excel, Powerbi, Spark, Hadoop, Tensorflow).
 - Created models using common job parameters and the features from the job description using 5 regression models (Multiple Linear, Lasso, Random Forest, Gradient Boosting and Bootstrap Aggregation) tuned with GridsearchCV.
 - Built a client facing UI using Flask API, WTForms and Jinja2. 

## Codes and Resources Used

**Python Version:** 3.9
**Packages:** pandas, numpy, sklearn, matplotlip, seaborn, selenium, pickle, flask, wtforms
**Web Framework Requirements**: ```pip install -r requirements.txt```
**Inspiration:** https://github.com/PlayingNumbers/ds_salary_proj
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium
**Flask WTForms:** https://hackersandslackers.com/flask-wtforms-forms/
**Flask WTForms Github:** https://github.com/hackersandslackers/flask-wtform-tutorial/tree/master/flask_wtforms_tutorial
