from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect
from form import PredForm
import predictor
import os 

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def pred_form():
    form = PredForm()
    if form.validate_on_submit():
        session['min_exp'] = form.min_exp.data
        session['job_title'] = form.job_title.data
        session['employment_type'] = form.employment_type.data
        session['seniority'] = form.seniority.data
        session['job_cat'] = form.job_cat.data
        session['job_desc'] = form.job_desc.data
        x_input = predictor.format_input(session['min_exp'],session['job_title'], session['employment_type'], session['seniority'], session['job_cat'], session['job_desc'] )
        pred_salary = predictor.predict(x_input)
        session['pred_salary'] = pred_salary
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
        pred_salary=session['pred_salary']
    )

