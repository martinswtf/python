from flask import Flask

app = Flask(__name__)

@app.route("/r")
def home():
    return "Página inicial"

@app.route("/")
def decorator():
    return """
    <h1>Decorators em Python</h1>

    <p><strong>O que é?</strong><br>
    Um decorator é uma função que modifica ou adiciona comportamentos a outra função sem alterar seu código original.
    </p>

    <p><strong>Para que serve?</strong><br>
    Ele é usado para reutilizar código, adicionar funcionalidades e deixar o programa mais organizado.
    </p>

    <p><strong>Como é utilizado no Flask?</strong><br>
    No Flask, o decorator <code>@app.route()</code> é usado para associar uma função a uma rota da aplicação. Assim, quando o usuário acessa uma URL específica, a função correspondente é executada.
    </p>

    <p>Exemplo:</p>

    <pre>
@app.route("/decorator")
def decorator():
    return "Olá!"
    </pre>
    """

if __name__ == "__main__":
    app.run(debug=True)
