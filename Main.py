from Events import Game
import pygame

g = Game()

pygame.mixer.music.load("assets/OST/Warhammer 40,000 Mechanicus Soundtrack - 10. Noosphere.mp3")
pygame.mixer.music.play(-1)

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()