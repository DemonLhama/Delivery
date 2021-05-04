import wtforms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    email = wtforms.StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = wtforms.PasswordField("Senha", validators=[DataRequired()])
    foto = FileField("Foto")
