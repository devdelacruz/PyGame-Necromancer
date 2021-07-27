import pygame


def drawPhitbox(win, player_hitbox):
    pygame.draw.rect(win, (255, 0, 0), player_hitbox, 3)

def drawPMeleeLeft(win, player_atkleft):
    pygame.draw.rect(win, (0, 255, 0), player_atkleft, 3)

def drawPMeleeRight(win, player_atkright):
    pygame.draw.rect(win, (0, 255, 0), player_atkright, 3)

