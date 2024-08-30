from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generar_combinacion():
    numeros_principales = random.sample(range(1, 41), 6)
    numero_extra_1 = random.choice(range(1, 13))
    numero_extra_2 = random.choice(range(1, 16))
    return numeros_principales, numero_extra_1, numero_extra_2

def calcular_probabilidad_combinacion(combinacion_usuario, combinacion_generada):
    return combinacion_usuario == combinacion_generada

@app.route('/', methods=['GET', 'POST'])
def index():
    combinaciones_usuario = []
    resultado = None

    if request.method == 'POST':
        for i in range(5):
            numeros_principales = list(map(int, request.form.getlist(f'numeros{i+1}')))
            numero_extra_1 = int(request.form[f'numero_extra_1_{i+1}'])
            numero_extra_2 = int(request.form[f'numero_extra_2_{i+1}'])
            combinaciones_usuario.append((numeros_principales, numero_extra_1, numero_extra_2))

        numeros_principales, numero_extra_1, numero_extra_2 = generar_combinacion()

        for combinacion in combinaciones_usuario:
            if calcular_probabilidad_combinacion(combinacion, (numeros_principales, numero_extra_1, numero_extra_2)):
                resultado = f"¡La combinación generada coincide con una de las combinaciones ingresadas!"
                break
        else:
            resultado = "La combinación generada no coincide con ninguna de las combinaciones ingresadas."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
