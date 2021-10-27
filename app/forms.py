from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email, DataRequired



class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email("Endereço de E-mail inválido")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters")
    ])
    remember = BooleanField("Permanecer conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired()
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters")
    ])
    submit = SubmitField("Cadastrar")
