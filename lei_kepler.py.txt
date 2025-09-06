#Luas 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Dados fornecidos
T_days = np.array([1.7690, 3.5510, 7.1540, 16.689])  # Período em dias
R_km = np.array([421600, 670900, 1070400, 1882700])  # Raio em km


# Constantes de conversão
day_to_sec = 24 * 60 * 60  # 1 dia = 86400 segundos
km_to_m = 1e3  # 1 km = 1000 metros
G = 6.67430e-11  # Constante gravitacional (m³ kg⁻¹ s⁻²)


# Convertendo para unidades adequadas
T_sec = T_days * day_to_sec  # Convertendo o período para segundos
R_m = R_km * km_to_m  # Convertendo o raio para metros


# Aplicando a transformação para a Lei de Kepler
T_squared = T_sec**2  # T²
R_cubed = R_m**3  # R³


# Regressão linear usando scipy.stats.linregress
slope, intercept, _, _, _ = linregress(R_cubed, T_squared)


# Cálculo da massa M utilizando a equação K = 4π² / (G M)
M = (4 * np.pi**2) / (G * slope)


# Ajustando a legenda para notação científica com potência de 10
slope_str = f"{slope:.2e}"  # Notação científica para a inclinação
intercept_str = f"{intercept:.2e}"  # Notação científica para o intercepto
M_str = f"{M:.2e}"  # Notação científica para a massa


# Plotando os dados e a linha de ajuste
plt.figure(figsize=(8, 6))
plt.plot(R_cubed, T_squared, 'ko', label='Dados', markersize=5)  # Dados experimentais
plt.plot(R_cubed, slope * R_cubed + intercept, 'r--', label=f'$\mathrm{{y}} = ({slope_str}) x + ({intercept_str})$ \n Massa de Júpiter Encontrada= {M_str} kg')  # Linha tracejada com Massa de Júpiter na legenda


# Personalização do gráfico
plt.xlabel('$R^3$ (m³)', fontsize=12)
plt.ylabel('$T^2$ (s²)', fontsize=12)
plt.title('Luas Galileanas', fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.5)


# Ajustando a legenda para incluir a massa de Júpiter
plt.legend(fontsize=10, loc='upper left')


# Ajustando os eixos (sem notação científica)
plt.tight_layout()


# Mostrar o gráfico
plt.show()


# Resultados detalhados
print(f"Inclinação (a): {slope:.2e}")
print(f"Intercepto (b): {intercept:.2e}")
print(f"Massa do corpo central (M): {M_str} kg")





# Código do ajuste para o Sistema Solar:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Definir a função do modelo a ser ajustado
def model(x, a, b):
    return a * x + b


df = pd.DataFrame([
    ('Mercury', 0.387098, 0.240846),
    ('Venus', 0.723332, 0.615198),
    ('Earth', 1.0, 1.0),
    ('Mars', 1.523679, 1.88085),
    ('Jupiter', 5.2044, 11.862),
    ('Saturn', 9.5826, 29.4571),
    ('Uranus', 19.19126, 84.0205),
    ('Neptune', 30.07, 164.8),
], columns=['name', 'a', 'T'])


# Dados de entrada
x_data = df['a'].apply(np.log)  # Logaritmo do eixo x
y_data = df['T'].apply(np.log)  # Logaritmo do eixo y


# Ajuste usando mínimos quadrados
popt, _ = curve_fit(model, x_data, y_data)


# Parâmetros otimizados
a_opt, b_opt = popt


# Cálculo da massa do Sol a partir do coeficiente linear
import math
conversao = (math.exp(b_opt) * (3.156e7)**2) * (1 / (1.496e11)**3)
Massa = (4 * np.pi**2) / (conversao * 6.6743e-11)


# Plotar os dados originais e a curva ajustada em escala logarítmica
plt.scatter(x_data, y_data, color='black', label='Dados', zorder=3)  # Pontos pretos
plt.plot(x_data, model(x_data, a_opt, b_opt), 'r--', label=f'$y = {a_opt:.2f}x + ({b_opt:.6f})$\nMassa do Sol encontrada: {Massa:.2e} kg', zorder=2)  # Linha tracejada


plt.xlabel('ln(R) (UA)')
plt.ylabel('ln(T) (anos)')
plt.legend()
plt.title('Sistema Solar')
plt.grid(True, linestyle='--', alpha=0.6, zorder=1)  # Grade sutil


plt.show()


# Exibir valores
print(f"Parâmetros otimizados: a = {a_opt}, b = {b_opt}")
print(f"Massa do Sol encontrada: {Massa:.2e} kg")



## Código em Log para o Sistema da estrela TOI 700
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Definir a função do modelo a ser ajustado
def model(x, a, b):
    return a * x + b


# Criar DataFrame com os dados dos exoplanetas
df = pd.DataFrame([
    ('TOI-700b', 0.0677, 10),
    ('TOI-700c', 0.0929, 16.1),
    ('TOI-700d', 0.1633, 37.4),
    ('TOI-700e', 0.134, 27.8)],
    columns=['name', 'a', 'T'])


# Aplicação do logaritmo nos dados
x_data = df['a'].apply(np.log)  # Logaritmo do eixo x (raio orbital)
y_data = df['T'].apply(np.log)  # Logaritmo do eixo y (período orbital)


# Ajuste da reta usando mínimos quadrados
popt, _ = curve_fit(model, x_data, y_data)


# Parâmetros otimizados da reta de ajuste
a_opt, b_opt = popt


# Criar os valores para a reta de ajuste
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = model(x_fit, a_opt, b_opt)


# Cálculo da massa da TOI 700
conversao = (np.exp(2 * b_opt) * (86400)**2) * (1 / (1.496e11)**3)
massa_encontrada = (4 * np.pi**2) / (conversao * 6.6743e-11)


# Criar a figura do gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='black', label='Dados')  # Pontos pretos
plt.plot(x_fit, y_fit, 'r',
         label=f'Ajuste: $y = {a_opt:.2f}x + {b_opt:.2f}$\nMassa da TOI 700 encontrada: {massa_encontrada:.2e} kg')  # Equação da reta + massa na legenda


# Configurações do gráfico
plt.xlabel('log(R) (UA)')
plt.ylabel('log(T) (Dias)')
plt.legend()
plt.title('Sistema da estrela TOI 700')
plt.grid(True)


# Mostrar gráfico
plt.show()


# Impressão dos resultados numéricos
print(f"Parâmetros otimizados: a = {a_opt:.4f}, b = {b_opt:.4f}")
print(f'Massa da TOI 700 encontrada usando o coeficiente linear: {massa_encontrada:.2e} kg')


# Massa de TOI 700 conforme literatura
massa_TOI_NASA = 0.42 * 1.98892e30
print(f'Massa da TOI 700 na literatura: {massa_TOI_NASA:.2e} kg')


# Cálculo do erro percentual
erro = abs((massa_TOI_NASA - massa_encontrada) / massa_TOI_NASA) * 100
print(f'Erro associado (%): {erro:.2f}%')



