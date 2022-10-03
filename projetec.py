from flask import render_template
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('projetec.html', titulo="Home")


@app.route('/atv_metas')
def atividades_metas():
    #                                           Alterar variáveis quando trocar atividade/metas
    return render_template('atv_metas.html', titulo="Atividades & Metas", atividade="a", meta="e", texto_meta="comer")


@app.route('/sobre')
def about():
    return render_template('about_us.html', titulo="Sobre Nós")

# As rotas e funções a seguir podem facilmente serem baseadas nas atividades de WEB

# @app.route('cadastro_user')
# def cadastrar_usuario():
#    return render_template('cadastrar_usuario.hrml', titulo="Cadastre-se!")


# @app.route('/login')
# def login():
#    return render_template('login.html', titulo="Login")

# @app.route('logout')
# def logout():


app.run(debug=True)
