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


## Web Scraping

Scraped over 300 job postings from [MyCareersFuture](https://www.mycareersfuture.gov.sg/). We extracted the following parameters from each job posting:
- Job Title
- Company Name
- Address
- Job Title
- Seniority
- Minimum Years of Experience Required
- Company Sector
- Salary Range
- Salary Unit
- Job Description

## Data Cleaning

After scraping the data, the data needed to be cleaned for it to be usable by our models. The following changes were made to the data:
1. Re-categorising of job titles to standardise categories
2. Re-categorising of employment type to standardise categories
3. Re-categorising of seniority to standardise categories
4. Converting minimum experience into numerical data
5. Re-categorising of company sector to their primary category
6. Converting salary range to average salary
7. Dropping unused columns

## Data Exploration

I first scanned the various job descriptions visually and identified keywords that we would like to extract as features representing the value companies place on the keywords. Following which, I created new columns for job description length and all the keywords identified. (AWS, Python, SQL, R, Tableau, Excel, Powerbi, Spark, Hadoop, Tensorflow). Next, I plotted pivot tables and graphs for the various categorical variables.

## Model Building

Firstly, I transformed the relevant categorical variables into dummy variables. Next, I split the data into train and test sets in the ratio of 8:2.

I tried five different models and evaluated them using Mean Absolute Error (MAE), which is easier to intepret.

The models tested were:
1. Multiple Linear (Baseline)
2. Lasso Regression (Reduces overfitting and increases interpretability)
3. Random Forest (Useful for high number of dimensions)
4. Gradient Boosting (Gives higher weitage to higher accuracy samples)
5. Bootstrap Aggregation (Useful to account for high variance)

The hyperparameters for the models were tuned using GridsearchCV.

## Model Performance

The Gradient Boosting Regression model returned the lowest MAE for the test set. We will use it for our final model.


    Multiple linear regression  1450.715424
  
              Lasso Regression  1395.916264
            
                 Random Forest  1424.412900
               
             Gradiant Boosting  1345.158719
           
            Boostrap Aggregate  1391.509327

## Productionisation

With our model built, I moved forward to develop a client-facing UI that accepts the parameters and outputs the predicted salary. I used WTForms under the Flask API to create a form for users to key in the respective parameters. 

![Predictor Interface](https://github.com/edologgerbird/salary_pred/blob/main/assets/demo0.png "Predictor Interface")


![Predictor Interface](https://github.com/edologgerbird/salary_pred/blob/main/assets/demo1.png "Predictor Interface")


![Predictor Interface](https://github.com/edologgerbird/salary_pred/blob/main/assets/demo2.png "Predictor Interface")
