import math
from flask import render_template, request


def pegar_numero(campo):
    """Lê um campo do form e converte pra float. Retorna None se estiver vazio."""
    valor = request.form.get(campo, "").strip()
    if not valor:
        return None
    return float(valor)


def calcular():
    operacao = request.form.get("operacao")
    num1 = pegar_numero("num1")

    if num1 is None:
        return render_template(
            "calculadora.html",
            etapas="Informe o primeiro número.",
            resultados="",
        )

    # ---------- RAIZ QUADRADA (só usa num1) ----------
    if operacao == "sqrt":
        if num1 < 0:
            etapas = f"√{num1}"
            resultados = "Erro: não existe raiz real de número negativo."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1}"
            resultados = f"{resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)

    # ---------- LOGARITMO (só usa num1, base 10) ----------
    if operacao == "log":
        if num1 <= 0:
            etapas = f"log({num1})"
            resultados = "Erro: logaritmo só existe para números maiores que zero."
        else:
            resultado = math.log10(num1)
            etapas = f"log({num1})"
            resultados = f"{resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)

    # ---------- BHASKARA (usa num1=a, num2=b, num3=c) ----------
    if operacao == "bhaskara":
        num2 = pegar_numero("num2")
        num3 = pegar_numero("num3")

        if num2 is None or num3 is None:
            return render_template(
                "calculadora.html",
                etapas="Informe os coeficientes a, b e c.",
                resultados="",
            )

        a, b, c = num1, num2, num3
        etapas = f"{a}x² + {b}x + {c} = 0"

        if a == 0:
            resultados = "Erro: coeficiente 'a' não pode ser zero (não é equação do 2º grau)."
        else:
            delta = (b ** 2) - (4 * a * c)
            if delta < 0:
                resultados = f"Erro: delta = {delta}, não existem raízes reais."
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                resultados = f"delta = {delta} | x1 = {x1} | x2 = {x2}"

        return render_template("calculadora.html", etapas=etapas, resultados=resultados)

    # ---------- OPERAÇÕES QUE PRECISAM DE num1 E num2 ----------
    num2 = pegar_numero("num2")
    if num2 is None:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2}"

    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2}"

    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2}"

    elif operacao == "/":
        if num2 == 0:
            etapas = f"{num1} ÷ {num2}"
            resultados = "Erro: divisão por zero não é permitida."
            return render_template("calculadora.html", etapas=etapas, resultados=resultados)
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2}"

    elif operacao == "**":
        resultado = math.pow(num1, num2)
        etapas = f"{num1} ^ {num2}"

    else:
        return render_template(
            "calculadora.html",
            etapas="Operação inválida.",
            resultados="",
        )

    resultados = f"{resultado}"
    return render_template("calculadora.html", etapas=etapas, resultados=resultados)
