from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    IntegerField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    NumberRange,
    Email,
    EqualTo,
    Length,
    URL
)

class PredForm(FlaskForm):
    min_exp = IntegerField(
        'Minimum Job Experience',
        [
            NumberRange(min=0, max=100, message="Please input a valid number"),
            DataRequired()
        ]
    )
    submit = SubmitField("Submit")