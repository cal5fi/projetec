from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for
import usuarios

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

@app.route('/cadastro_user')
def cadastrar_usuario():
    return render_template('cadastrar_usuario.html')


@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = usuarios.buscar(email, senha)
        if usuario is None:
            flash('Usuário/ Senha Inválidos.')
        else:
            session['usuario_email'] = usuario.email
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('index'))


app.run(debug=True)
