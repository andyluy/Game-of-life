import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Configuração do tabuleiro
n = 50  # tamanho do grid (50x50 células)

# Inicializa o grid com valores aleatórios (0 = morto, 1 = vivo)
grid = np.random.choice([0, 1], size=(n, n))

# Função para calcular o próximo estado do grid com base nas regras do Jogo da Vida
def update(grid):
    new_grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            # Conta os vizinhos vivos (considerando bordas com wrap-around)
            total = (
                grid[(i-1) % n, (j-1) % n] + grid[(i-1) % n, j] + grid[(i-1) % n, (j+1) % n] +
                grid[i, (j-1) % n] + grid[i, (j+1) % n] +
                grid[(i+1) % n, (j-1) % n] + grid[(i+1) % n, j] + grid[(i+1) % n, (j+1) % n]
            )
            # Aplica as regras do Jogo da Vida
            if grid[i, j] == 1 and (total == 2 or total == 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and total == 3:
                new_grid[i, j] = 1
            else:
                new_grid[i, j] = 0
    return new_grid

# Função para animar o grid usando matplotlib
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary')
plt.title("Jogo da Vida - Arte Generativa")
plt.axis('off')

def animate(frame_num):
    global grid
    grid = update(grid)
    img.set_data(grid)
    return img,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, blit=True)
plt.show()