from flask import Flask, request, render_template

app = Flask(__name__)

# Dicionário com os usuários e senhas permitidos
usuarios = {
    'joao pedro soares': '22400621',
    'dolga': 'cotemig2026',
    'janaina': 'cotemig2026',
    'antonio': 'cotemig2026'
}

def show_the_login_form(erro=False):
    return render_template('login.html', erro=erro)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    # Percorre o dicionário procurando um usuário e senha que batam
    for usuario_cadastrado, senha_cadastrada in usuarios.items():
        if usuario == usuario_cadastrado and senha == senha_cadastrada:
            return render_template('bem_vindo.html', usuario=usuario)

    return show_the_login_form(erro=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping
