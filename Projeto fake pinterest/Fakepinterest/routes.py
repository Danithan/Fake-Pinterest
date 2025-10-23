#criar as rotas do site
from flask import render_template, url_for
from Fakepinterest import app
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from flask_login import login_required
=======
from Fakepinterest.forms import FormLogin, FormCriaConta
>>>>>>> Stashed changes
=======
from Fakepinterest.forms import FormLogin, FormCriaConta
>>>>>>> Stashed changes

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    return render_template('index.html', form=formlogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    return render_template('criarconta.html',form=FormCriaConta)
<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)