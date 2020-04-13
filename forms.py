from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, RadioField, SubmitField, FormField, FieldList
from wtforms.validators import DataRequired
from sploit import get_formats, get_encoders, get_payloads


class GenerateForm(FlaskForm):
    payloads = SelectField('Payloads', choices=[(payload_choice, payload_choice) for payload_choice in get_payloads()], validators=[DataRequired()])
    encoders = SelectField('Encoders', choices=[(encoder_choice, encoder_choice) for encoder_choice in get_encoders()], validators=[DataRequired()])
    variable_name = StringField('Variable Name', validators=[DataRequired()])
    payload_formats = SelectField('Payload Formats', choices=[(payload_format_choice, payload_format_choice) for payload_format_choice in get_formats()], validators=[DataRequired()])
    bad_chars = TextAreaField('Bad Characters', validators=[DataRequired()])
    generate = SubmitField('Generate')

