"""
Nome do Projeto: Simulação queda livre de uma maça. 

Descrição: 

Autores: 
  Julia Marcolan Teixeira (inserir número USP)

Este projeto faz parte do processo avaliativo da disciplina 7600105 - Física Básica I (2024) da USP-São Carlos ministrada pela(o) [Prof. Krissia de Zawadzki/Esmerindo de Sousa Bernardes]
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def quedra_livre(z0, v0, g, t_max, num_points):
    """
    Calcula a posição de um objeto em queda livre ao longo do tempo.

    Parâmetros:

      z0 (float): Posição inicial do objeto em metros.
      v0 (float): Velocidade inicial do objeto em m/s.
      g (float): Aceleração da gravidade em m/s^2.
      t_max (float): Tempo máximo de simulação em segundos.
      num_points (int): Número de pontos para a geração do vetor de tempo.

    Retorna:
      t (numpy.ndarray): Vetor de tempo para a simulação do movimento do objeto.
      z (numpy.ndarray): Vetor de posições verticais ao longo do tempo.
    """
    t = np.linspace(0, t_max, num=num_points)

    z = z0 + v0 * t - 0.5 * g * t**2

    return t, z

def update(frame):
    """
    Atualiza o gráfico para cada quadro da animação, mostrando a posição de um objeto em queda livre
    sem resistência do ar, e reposicionando um marcador (imagem) para representar a posição atual.

    Parâmetros:

    frame (int): O índice do quadro atual na animação, usado para atualizar a posição do marcador.

    Funcionalidade:

        - Limpa o gráfico para redesenhar a altura do objeto.
        - Replota a linha de altura ao longo do tempo.
        - Ajusta o limite dos eixos x e y para manter a visualização focada.
        - Reaplica o título, legendas e grades do gráfico para manter a formatação original.
        - Adiciona um marcador de imagem que representa o objeto em queda na posição correspondente ao
         tempo `t[frame]` e altura `z[frame]`, permitindo uma visualização da posição atual do objeto.

    Variáveis globais:
    - t (array): Array de tempos correspondentes aos pontos da altura.
    - z (array): Array de alturas do objeto ao longo do tempo.
    - ax (matplotlib.axes.Axes): O eixo de plotagem onde o gráfico e o marcador são desenhados.
    - img_marker (ndarray): Imagem que representa o marcador do objeto, carregada com `mpimg.imread()`.
    """
    
    ax.clear()  # Limpa o gráfico para desenhar novamente
    
    # Replota a linha da altura
    ax.plot(t, z, label='Altura')
    
    # Replota a linha de referência
    ax.set_xlim((0, 5))
    ax.set_ylim((0, 120))
    # Reaplica o título e legendas
    ax.grid()
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Altura (m)')
    ax.set_title('Queda livre sem resistência do ar')

    # Adicionar a imagem no novo ponto
    imagebox = OffsetImage(img_marker, zoom=0.05)  # Ajuste o zoom conforme necessário
    ab = AnnotationBbox(imagebox, (t[frame], z[frame]), frameon=False)
    ax.add_artist(ab)


#Chamada da funcao 
t, z = quedra_livre(100, 0, 9.8, 5, 25)

# Carregar a imagem personalizada: Substitua pelo caminho da sua imagem
img_marker = mpimg.imread('figura_maca.png')  

fig, ax = plt.subplots()
line, = ax.plot(t, z, label='Altura')  # Plotando a linha principal

# Definindo um tamanho de escala para o marcador
marker_size = 30  # Ajuste o tamanho conforme necessário

# Plotando os pontos com a imagem personalizada como marcador
for i in range(len(t)):
    ax.imshow(img_marker, extent=(t[i] - 0.1, t[i] + 0.1, z[i] - 5, z[i] + 5), aspect='auto', zorder=10)

# Ajustar limites dos eixos
ax.set_xlim((0, 5))
ax.set_ylim((0, 120))
#ax.grid()
#ax.set_xlabel('Tempo (s)')
#ax.set_ylabel('Altura (m)')
#ax.set_title('Queda livre com ícone animado')



# Criar a animação
ani = FuncAnimation(fig, update, frames=len(t), interval=100)
plt.show()