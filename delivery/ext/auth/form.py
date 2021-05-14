import wtforms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email

# Flask-WTF will create a form to submit (email, password, picture)
#The validators=DataRequired(), Email() ensures that this field is not submitted empty and with a valid email (contains "@") 
#This will be used in the routes section (site/main.py), and in the userform.html


class UserForm(FlaskForm):
    email = wtforms.StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = wtforms.PasswordField("Senha", validators=[DataRequired()])
    foto = FileField("Foto")
