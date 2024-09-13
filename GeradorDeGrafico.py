import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definindo uma expressão simbólica

x = sp.symbols('x')
# Recebendo a expressão/função

entrada = input("Digite a expressão: \n") 
expr_simbolica = sp.sympify(entrada)
# Derivando a função (é passado como paramêtro a função e a variável x que é um simbolo, ou seja, algo simbólico)
derivada = sp.diff(expr_simbolica, x)

#Criando um array de -100 até 100
x_vals = np.linspace(-100, 100, 100)
# Convertendo para uma função numérica usando NumPy
f_numpy = sp.lambdify(x, expr_simbolica, 'numpy') 
y_numpy = sp.lambdify(x, derivada, 'numpy')
#Verificando se a derivada é um valor escalar (como 1, 2 3, etc)
if np.isscalar(derivada):
    y_vals = np.full_like(x_vals, derivada) # Caso for, será criado um array de mesmo tamanho de x_vals com o valor da derivada
else:
    y_vals = y_numpy(x_vals) # Caso não, feito o cálculo em relação a cada valor de x

#Plotando o gráfico

plt.figure("Gráfico")
plt.plot(x_vals, f_numpy(x_vals), label='Função Original')
plt.grid()
plt.plot(x_vals, y_vals, label='Derivada')
plt.legend()
plt.show()
