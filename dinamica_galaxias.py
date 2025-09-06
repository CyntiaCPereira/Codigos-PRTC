import numpy as np
import matplotlib.pyplot as plt


# Definir constantes
G = 1
M = 1
R = 1  # Raio da esfera


# Criar intervalo de valores para r
r_interno = np.linspace(0, R, 200, endpoint=False)  # Para r < R, evitando r=0
r_externo = np.linspace(R, 10, 200)  # Para r > R até 30


# Definir funções de velocidade
v_interno = np.sqrt((G * M / R**3)) * r_interno
v_externo = np.sqrt(G * M / r_externo)


# Criar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(r_interno, v_interno, label=r'$v(r) = \sqrt{\frac{GM}{R^3}} r, \quad r < R$', color='b')
plt.plot(r_externo, v_externo, label=r'$v(r) = \sqrt{\frac{GM}{r}}, \quad r > R$', color='r')


# Adicionar linha tracejada para R e um label separado para G e M
plt.axvline(R, linestyle='dashed', color='black', alpha=0.7, label=f'R = {R}')
plt.plot([], [], ' ', label=r'$G = 1, M = 1$')  # Adiciona G e M como legenda separada


# Configurações do gráfico
plt.xlabel(r'Raio $r$')
plt.ylabel(r'Velocidade $v(r)$')
plt.title('Distribuição da Velocidade Orbital')
plt.legend()
plt.grid(True)


# Mostrar gráfico
plt.show()



