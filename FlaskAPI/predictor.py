import pickle
import pandas as pd 
import math

def load_models():
    file_name = "model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

def format_input(min_exp, job_title, employment_type, seniority, job_cat, job_desc):
    row = pd.read_csv('sample_row.csv')
    # print(row)
    row['min_exp'] = min_exp
    row[job_title] = 1
    row[employment_type] = 1
    row[seniority] = 1
    row[job_cat] = 1
    row['job_desc_len'] = len(job_desc)
    keywords = ['aws', 'python', 'sql', 'r', 'tableau', 'excel', 'powerbi', 'spark', 'spark', 'hadoop', 'tensorflow']
    job_desc_lower = job_desc.lower()
    for keyword in keywords:
        if keyword in job_desc_lower:
            row[keyword] = 1
    return row.iloc[: , 1:]

def predict(x_input):
    model=load_models()
    prediction = math.ceil(model.predict(x_input)[0])
    return prediction

min_exp = 4
job_title = 'job_title_data scientist'
employment_type = 'employment_type_full time'
seniority = 'seniority_Senior Executive'
job_cat = 'job_cat_accounting / auditing / taxation'
job_desc = 'hehehehehehe python aws spark hehehehhe r heheheheheh tensorflow'
