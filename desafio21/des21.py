import pygame
import os

# Inicializar o Pygame
pygame.init()

# Definir o diretório atual
diretorio_atual = os.path.dirname(__file__)

# Carregar a música
caminho_musica = os.path.join(diretorio_atual, "ocean.mp3")
pygame.mixer.music.load(caminho_musica)

# Tocar a música
pygame.mixer.music.play()

# Manter o programa em execução até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)








