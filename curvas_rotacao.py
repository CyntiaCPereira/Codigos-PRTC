import requests
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


# Função para baixar e processar os dados
def carregar_dados(url):
    response = requests.get(url)
    data = response.text.split("\n")


    # Filtrar linhas vazias e comentários
    data = [line for line in data if line.strip() and not line.startswith("#")]


    column1 = []
    column2 = []


    # Processar os dados
    for line in data:
        values = line.split()
        column1.append(float(values[0]))  # Raio em Kpc
        column2.append(float(values[1]))  # Velocidade em Km/s


    return np.array(column1), np.array(column2)


# URLs dos dados
url_via_lactea = "http://www.ioa.s.u-tokyo.ac.jp/~sofue/RC99/0000.dat"
url_m31 = "http://www.ioa.s.u-tokyo.ac.jp/~sofue/RC99/0224.dat"


# Carregar dados
R_via_lactea, V_via_lactea = carregar_dados(url_via_lactea)
R_m31, V_m31 = carregar_dados(url_m31)


# Criar interpolação para suavização
def suavizar_curva(R, V):
    R_smooth = np.linspace(R.min(), R.max(), 300)
    spline = make_interp_spline(R, V, k=3)  # Interpolação cúbica
    V_smooth = spline(R_smooth)
    return R_smooth, V_smooth


# Suavizar os dados
R_smooth_via_lactea, V_smooth_via_lactea = suavizar_curva(R_via_lactea, V_via_lactea)
R_smooth_m31, V_smooth_m31 = suavizar_curva(R_m31, V_m31)


# Criar subplots lado a lado
fig, axs = plt.subplots(1, 2, figsize=(14, 6))


# Gráfico da Via Láctea
axs[0].scatter(R_via_lactea, V_via_lactea, label="Dados Observacionais", marker="o", s=10, color="black", alpha=0.6)
axs[0].plot(R_smooth_via_lactea, V_smooth_via_lactea, label="Curva Suavizada (Spline)", color="red", linewidth=2)
axs[0].set_title("Curva de Rotação da Via Láctea", fontsize=14)
axs[0].set_xlabel("Raio $R$ (kpc)", fontsize=12)
axs[0].set_ylabel("Velocidade Orbital $V$ (km/s)", fontsize=12)
axs[0].set_ylim(0, 265)
axs[0].set_xlim(-1, R_via_lactea.max() + 1)
axs[0].grid(True, linestyle="--", alpha=0.6)
axs[0].legend(fontsize=10)


# Gráfico da M31
axs[1].scatter(R_m31, V_m31, label="Dados Observacionais", marker="o", s=10, color="black", alpha=0.6)
axs[1].plot(R_smooth_m31, V_smooth_m31, label="Curva Suavizada (Spline)", color="red", linewidth=2)
axs[1].set_title("Curva de Rotação da M31", fontsize=14)
axs[1].set_xlabel("Raio $R$ (kpc)", fontsize=12)
axs[1].set_ylabel(" ", fontsize=12)
axs[1].set_ylim(-10, 300)
axs[1].set_xlim(-1, R_m31.max() + 1)
axs[1].grid(True, linestyle="--", alpha=0.6)
axs[1].legend(fontsize=10)


# Ajustar espaçamento entre os gráficos
plt.tight_layout()


# Mostrar gráfico
plt.show()



