import pygame


def drawEhitbox(win, enemy_hitbox):
    pygame.draw.rect(win, (255, 0, 0), enemy_hitbox, 3)

def drawErangebox(win, enemy_range):
    pygame.draw.rect(win, (0, 0, 255), enemy_range, 3)

def drawEguardbox(win, enemy_guard):
    pygame.draw.rect(win, (150, 150, 150), enemy_guard, 3)

def drawEatkleft(win, enemy_atkleft):
    pygame.draw.rect(win, (0, 255, 0), enemy_atkleft, 3)

def drawEatkright(win, enemy_atkright):
    pygame.draw.rect(win, (0, 255, 0), enemy_atkright, 3)