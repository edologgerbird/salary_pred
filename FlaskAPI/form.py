from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    TextAreaField,
    SubmitField,
    IntegerField,
    FloatField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    NumberRange,

)

class PredForm(FlaskForm):
    min_exp = IntegerField(
        'Minimum Job Experience',
    )

    job_title = SelectField(
        'Job Title',
        [DataRequired()],
        choices=[
            ('job_title_analyst', 'Data Analyst'),
            ('job_title_consultant', 'Consultant'),
            ('job_title_data management', 'Data Management'),
            ('job_title_data scientist', 'Data Scientist'), 
            ('job_title_developer', 'Developer') ,
            ('job_title_engineer', 'Data Engineer'), 
            ('job_title_manager', 'Manager'),
            ('job_title_trainee', 'Trainee/Intern'),
            ('job_title_others', 'Other'),
        ],
    )

    employment_type = SelectField(
        'Employment Type',
        [DataRequired()],
        choices=[
            ('employment_type_full time', 'Full Time'),
            ('employment_type_contract','Contract'),
            ('employment_type_temporary', 'Temporary'),
            ('employment_type_flexi-work','Flexi-work/Part Time'), 
            ('employment_type_internship/traineeship', 'Internship/Traineeship'),
        ]
    )

    seniority = SelectField(
        'Seniority',
        [DataRequired()],
        choices=[
            ('seniority_Senior Executive','Senior Executive'),
            ('seniority_Executive', 'Executive'),
            ('seniority_Junior Executive', 'Junior Executive'),
            ('seniority_Senior Management','Senior Management'),
            ('seniority_Middle Management', 'Middle Management'),
            ('seniority_Manager', 'Manager'),
            ('seniority_Non-executive', 'Non-Executive'),
            ('seniority_Professional','Professional'),            
            ('seniority_Fresh/entry level','Fresh/Entry Level'),
        ]
    )
    
    job_cat = SelectField(
        'Company Sector',
        [DataRequired()],
        choices=[
            ('job_cat_accounting / auditing / taxation', "Accounting/Auditing/Taxation"),
            ('job_cat_admin / secretarial', "Admin/Secretarial"),
            ('job_cat_advertising / media', "Advertising/Media"),
            ('job_cat_banking and finance', "Banking and Finance"),
            ('job_cat_building and construction', "Building and Construction"),
            ('job_cat_consulting', "Consulting"),
            ('job_cat_customer service', "Customer Service"),
            ('job_cat_engineering', "Engineering"),
            ('job_cat_general work', "General Work"),
            ('job_cat_healthcare / pharmaceutical', "Healthcare/Pharmaceutical"),
            ('job_cat_human resources','Human Resources'),
            ('job_cat_information technology', "Information Technology"),
            ('job_cat_insurance', "Insurance"),
            ('job_cat_logistics / supply chain', "Logistics/Supply Chain"),
            ('job_cat_manufacturing', "Manufacturing"),
            ('job_cat_marketing / public relations', "Marketing/Public Relations"),
            ('job_cat_public / civil service', 'Public/Civil Service'),
            ('job_cat_sciences / laboratory / r&d', "Sciences/Laboratory/R&D"),
            ('job_cat_wholesale trade', "Wholesale Trade"),
            ('job_cat_others','Others'),
        ]
    )

    job_desc = TextAreaField(
        'Job Description',
        [DataRequired()],
    )

    submit = SubmitField("Submit")