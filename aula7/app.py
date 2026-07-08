from flask import Flask, request
from calculadora import calcular, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return calcular()
    return render_template('calculadora.html', etapas="", resultados="")


if __name__ == '__main__':
    app.run(debug=True)
