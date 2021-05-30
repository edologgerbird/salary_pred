from flask import Flask, render_template, request, url_for, session
import pickle
from werkzeug.utils import redirect
from form import PredForm
import os 


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/pred_form", methods=["GET", "POST"])
def pred_form():
    form = PredForm()
    if form.validate_on_submit():
        session['min_exp'] = form.min_exp.data
        session['job_title'] = form.job_title.data
        return redirect(url_for("success"))
    return render_template(
        "predform.jinja2",
        form=form,
        template="form-template"
    )

@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template(
        "success.jinja2",
        template="success-template",
        min_exp=session['min_exp'],
        job_title=session['job_title']
    )























@app.route('/', methods=['GET', 'POST'])
def hello_world():
    job_title = ['Data Analyst', 'Consultant', 'Data Management', 'Data Scientist', 'Developer', 'Data Engineer', 'Manager', 'Trainee/Intern', 'Other']
    employment_type = ['Full Time', 'Contract', 'Flexi-work', 'Temporary', 'Internship/Traineeship']
    seniority = [
        'Fresh/Entry level',
        'Executive',
        'Junior Executive', 
        'Manager', 
        'Middle Management', 
        'Non-executive', 
        'Professional', 
        'Senior Executive', 
        'Senior Management'
        ]
    job_cat = [
        'accounting / auditing / taxation',
        'admin / secretarial',
        'advertising / media',
        'banking and finance',
        'building and construction',
        'consulting',
        'customer service',
        'engineering',
        'general work',
        'healthcare / pharmaceutical',
        'human resources',
        'information technology',
        'insurance',
        'logistics / supply chain',
        'manufacturing',
        'marketing / public relations',
        'public / civil service',
        'sciences / laboratory / r&d',
        'wholesale trade',
        'others'
    ]
    if request.method == 'GET':
        return render_template('index.html', job_title=job_title, employment_type=employment_type, seniority=seniority, job_cat=job_cat)
    else:
        text1 = request.form['min_exp']
        text2 = request.form['job_title']
        text3 = request.form['employment_type']
        return text1 + text2 + text3



# def hello_world():
#     test_input = np.array([[10,0,0,1, 0, 0, 1, 0, 0, 0,0,2156,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
#     model = load_models()
#     preds = model.predict(test_input)
#     preds_str = str(preds)
#     return preds_str