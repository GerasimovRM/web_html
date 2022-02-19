from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CrashLoginForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html",
                           title=title)


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("training.html",
                               title="Инженерные тренажеры",
                               image=url_for("static", filename="img/it.gif"))
    else:
        return render_template("training.html",
                               title="Научные симуляторы",
                               image=url_for("static", filename="img/ns.gif"))


@app.route("/list_prof/<list_type>")
def list_prof(list_type):
    ll = ["инженер-исследователь",
          "пилот",
          "строитель",
          "экзобиолог",
          "врач",
          "инженер по терраформированию",
          "климатолог",
          "специалист по радиационной защите",
          "астрогеолог",
          "гляциолог",
          "инженер жизнеобеспечения",
          "метеоролог",
          "оператор марсохода",
          "киберинженер",
          "штурман",
          "пилот дронов"]
    return render_template("list_prof.html",
                           title="Список профессий",
                           list_prof=ll,
                           list_type=list_type)



@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/crash_login", methods=['GET', 'POST'])
def crash_login():
    form = CrashLoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('crash_login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
