# Team: SciPy
import pygame
from numpy import random
import sys
import csv
import threading
from datetime import datetime
from drawPlayground import drawPg
from drawTile import drawTl
from drawPlayerHitbox import drawPhitbox
from drawPlayerHitbox import drawPMeleeLeft
from drawPlayerHitbox import drawPMeleeRight
from drawEnemyHitbox import drawEhitbox
from drawEnemyHitbox import drawErangebox
from drawEnemyHitbox import drawEguardbox
from drawEnemyHitbox import drawEatkleft
from drawEnemyHitbox import drawEatkright

# initialize pygame
pygame.init()
clock = pygame.time.Clock()
now = datetime.now()
sfx = True


def Start():
    # display game window
    canvas_w, canvas_h = 1280, 720
    win = pygame.display.set_mode((1280, 720))  # Resolution
    pygame.display.set_caption("Necromancer")  # Name of window
    gameVersion = "v0.1.8"

    # Sprite imports
    player_wRight = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 0.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 1.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 2.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 3.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 4.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 0.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 1.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 2.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 3.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Right/Necromancer Walk Right 4.png')]

    player_wLeft = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 4.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Walk/Left/Necromancer Walk Left 4.png')]

    player_idleR = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Right/Necromancer Idle Right 0.png')]

    player_idleL = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Idle/Left/Necromancer Idle Left 0.png')]

    player_hurtL = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Left/Necromancer Hurt Left 2.png')]

    player_hurtR = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Hurt/Right/Necromancer Hurt Right 2.png')]

    player_aRight = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 0.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 0.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 0.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 1.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 1.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 2.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 3.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 4.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 4.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Right/Necromancer Attack Right 4.png')]

    player_aLeft = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 4.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/Left/Necromancer Attack Left 4.png')]

    player_aGRight = [
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right1.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right1.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right2.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right3.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right3.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right4.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Right/Necromancer Gattack Right4.png')]

    player_aGLeft = [
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 0.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 1.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 1.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 2.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 3.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 3.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 4.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Attack/gAttack/Left/Necromancer gAttack Left 4.png')]

    player_rRight = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 00.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 01.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 02.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 03.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 04.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 05.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 06.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 07.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 08.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Right/Necromancer Run Right 09.png')]

    player_rLeft = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 00.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 01.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 02.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 03.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 04.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 05.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 06.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 07.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 08.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Run/Left/Necromancer Run Left 09.png')]

    player_jRight = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 00.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 01.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 02.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 03.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 04.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 05.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 06.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 07.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 08.png'),
                     pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Right/Necromancer Fly Right 09.png')]

    player_jLeft = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 00.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 01.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 02.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 03.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 04.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 05.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 06.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 07.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 08.png'),
                    pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump/v2/Left/Necromancer Fly Left 09.png')]

    player_jdRight = [
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 00.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 01.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 02.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 03.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 04.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 05.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 06.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 07.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 08.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Right/Necromancer Jump Dash Right 09.png')]

    player_jdLeft = [
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 00.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 01.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 02.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 03.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 04.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 05.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 06.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 07.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 08.png'),
        pygame.image.load('assets/Pixel/Sprites/Necromancer/Jump Dash/Left/Necromancer Dash Jump Left 09.png')]

    enemy_idleR = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Right/Templar Idle Right0.png')]

    enemy_idleL = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Idle/Left/Templar Idle Left 0.png')]

    enemy_hurtR = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Right/Templar Hurt Right 2.png')]

    enemy_hurtL = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Hurt/Left/Templar Hurt Left 2.png')]

    enemy_wRight = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Right/Templar Walk Right 1.png')]

    enemy_wLeft = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 3.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 3.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Walk/Left/Templar Walk Left 1.png')]

    enemy_aRight = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 0.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 2.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 3.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 1.png'),
                    pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Right/Templar Attack Right 1.png')]

    enemy_aLeft = [pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 3.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 3.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/Templar/Templar Attack/Left/Templar Attack Left 1.png')]

    enemy_death = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 01.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 02.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 03.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 04.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 05.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 06.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 07.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 08.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 09.png'),
                   pygame.image.load('assets/Pixel/Sprites/Necromancer/Death/Right/Necromancer Death Right 13.png')]
    torch_BG = [pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 0.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 1.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 2.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 3.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 4.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 0.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 1.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 2.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 3.png'),
                pygame.image.load('assets/Pixel/Sprites/BG/Torch/Torch 4.png')]

    HeadSprites = [pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head/Head 0.png')]
    HandSprites = [pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 0.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 1.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 2.png'),
                   pygame.image.load('assets/Pixel/Sprites/BG/Floor/Hand/Hand 0.png')]

    # Background
    floor_BGMid = pygame.image.load('assets/Pixel/Sprites/BG/Floor/200Mid.png')
    floor_BGEnd = pygame.image.load('assets/Pixel/Sprites/BG/Floor/200End.png')
    floor_BGEnd2 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/200End2.png')
    floor_Man1 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/ManCorpse.png')
    floor_Man2 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan2.png')
    floor_Man3 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan3.png')
    floor_Man4 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan4.png')
    floor_Man5 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan5.png')
    floor_Man6 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan6.png')
    floor_Man7 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/FloorMan7.png')
    wall1 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall1.png')
    wall2 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall2.png')
    wall3 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall3.png')
    wall4 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall4.png')
    wall5 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall5.png')
    wall6 = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Wall/Wall6.png')

    # headCthulu = pygame.image.load('assets/Pixel/Sprites/BG/Floor/Head.png')

    def ThreadSprites():
        th1 = threading.Thread(target=torchBG.draw)
        th2 = threading.Thread(target=Cthulu.draw)
        th1.start()
        th2.start()

    def ThreadEnemy():
        th3 = threading.Thread(target=enemyFollow)
        th3.start()

    def ThreadPlayer():
        th4 = threading.Thread(target=necromancer.draw)
        th4.start()

    def floorDraw():
        win.blit(floor_BGEnd, (50, 400))
        win.blit(floor_BGMid, (200, 400))
        win.blit(floor_BGMid, (300, 400))
        win.blit(floor_BGMid, (400, 400))
        win.blit(floor_BGMid, (500, 400))
        win.blit(floor_BGMid, (600, 400))
        win.blit(floor_BGMid, (700, 400))
        win.blit(floor_BGMid, (800, 400))
        win.blit(floor_BGEnd2, (1050, 400))
        win.blit(floor_BGMid, (900, 400))
        win.blit(wall1, (50, 280))
        win.blit(wall2, (250, 280))
        win.blit(wall3, (450, 280))
        win.blit(wall4, (650, 280))
        win.blit(wall5, (850, 280))
        win.blit(wall6, (1050, 280))

    def floorCorpse():
        win.blit(floor_Man1, (100, 400))
        win.blit(floor_Man2, (50, 400))
        win.blit(floor_Man3, (1050, 400))
        win.blit(floor_Man4, (1000, 400))
        win.blit(floor_Man5, (900, 400))
        win.blit(floor_Man6, (170, 400))
        win.blit(floor_Man7, (850, 400))
        # win.blit(Head, (550, 100))

    class torch:
        def __init__(self, torch_x, torch_y):
            self.torch_x = torch_x
            self.torch_y = torch_y
            self.torchCount = 0
            self.torch1 = True

        def draw(self):
            if self.torchCount + 1 >= 30:
                self.torchCount = 0

            if self.torch1:
                # win.blit(torch_BG[self.torchCount // 3], (self.torch_x, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 150, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 300, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 450, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 600, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 750, self.torch_y))
                win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 900, self.torch_y))
                # win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 1050, self.torch_y))

            self.torchCount += 1

    class cthuluhu:
        def __init__(self, headx, heady, handx, handy):
            self.headx = headx
            self.heady = heady
            self.handx = handx
            self.handy = handy
            self.headCount = 0
            self.isHead = True

        def draw(self):
            if self.headCount + 1 >= 30:
                self.headCount = 0

            if self.isHead:
                win.blit(HeadSprites[self.headCount // 3], (self.headx, self.heady))
                win.blit(HandSprites[self.headCount // 3], (self.handx - 50, self.handy - 50))

            self.headCount += 1

    class mixerWrapper:
        def __init__(self):
            self.IsPaused = False

        def toggleMusic(self):
            if self.IsPaused:
                pygame.mixer.music.unpause()
                self.IsPaused = False
            else:
                pygame.mixer.music.pause()
                self.IsPaused = True

        def drawMusic(self):
            if self.IsPaused:
                SFX = Pixel.render("Music: OFF", True, (252, 252, 252))
                win.blit(SFX, (10, 690))
            else:
                SFX = Pixel.render("Music: On", True, (252, 252, 252))
                win.blit(SFX, (10, 690))

    class levelIn:
        def __init__(self):
            self.animation = False
            self.timer = 10
            self.timerCount = 0

        # def levelInDraw

    class GameEnd:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.gameOver = False
            self.gameOverCount = 0
            self.date = now

        def draw(self):

            if self.gameOverCount + 1 >= 30:
                self.gameOverCount = 0

            if self.gameOver:
                win.blit(enemy_death[self.gameOverCount // 3], (self.x, self.y))

            self.gameOverCount += 1

    # Fonts
    # celticRune = pygame.font.Font("assets/Fonts/CelticRune.ttf", 25)
    # ancientRune = pygame.font.Font("assets/Fonts/AncientRunes.ttf", 25)
    Pixel = pygame.font.Font("assets/Fonts/Pixel.ttf", 25)
    Pixel2 = pygame.font.Font("assets/Fonts/Pixel.ttf", 50)
    Pixel3 = pygame.font.Font("assets/Fonts/Pixel.ttf", 100)

    # character attributes
    class player:
        def __init__(self, player_x, player_y):
            self.player_x = player_x
            self.player_y = player_y
            self.player_location = player_x, player_y
            self.player_v = 5  # Velocity

            # player stats
            self.maxHealth = 100
            self.health = 100
            self.maxStamina = 100
            self.stamina = 100
            self.atkDamage = 40
            self.name = "Necromancer"

            # animation state booleans
            self.isRight = False
            self.isLeft = False
            self.isFacingRight = True
            self.isFacingLeft = False
            self.isAttacking = False
            self.isDashing = False
            self.isJumping = False
            self.isJumpingDash = True
            self.isTired = False
            self.isHurt = False

            # spell book
            self.spellBlade = True
            self.spellSpike = False
            self.spellBomb = False

            # cooldown state booleans
            self.damageImmune = False
            self.cooldownDash = False
            self.pointsVisible = False

            # statistics
            self.isDamaged10 = False
            self.points = 0
            self.pointsMultiplier = 0
            self.corpseNum = 0
            self.levelCounter = 1
            self.hasName = False

            # timers
            self.damageImmuneTimer = 70
            self.damageImmuneCounter = 0
            self.cooldownDashTimer = 100
            self.dashCounterCooldown = 0

            # animation counts
            self.walkCount = 0
            self.idleCount = 0
            self.attackCount = 0
            self.runDashCount = 0
            self.jumpCount = 10
            self.jumpDashCount = 0
            self.hurtCount = 0

            # Debugs
            self.godMode = False

        def draw(self):

            # Attack counter loop limit
            if self.attackCount + 1 >= 30:
                self.attackCount = 0
                self.isAttacking = False

            # Walk counter loop limit
            if self.walkCount + 1 >= 30:
                self.walkCount = 0

            # Run counter loop limit
            if self.runDashCount + 1 >= 30:
                self.runDashCount = 0
                self.isDashing = False

            # Idle counter loop limit
            if self.idleCount + 1 >= 30:
                self.idleCount = 0

            # Hurt counter loop limit
            if self.hurtCount + 1 >= 30:
                self.hurtCount = 0
                self.isHurt = False
                self.isDamaged10 = False

            # Jump counter loop limit
            if self.jumpCount + 1 >= 30:
                self.jumpCount = 0

            # Jump counter loop limit
            if self.jumpDashCount + 1 >= 30:
                self.jumpDashCount = 0

            # Walk Animation
            if self.isLeft:  # If facing left image shown 3 times every animation
                win.blit(player_wLeft[self.walkCount // 3], (self.player_x, self.player_y))
            elif self.isRight:
                win.blit(player_wRight[self.walkCount // 3], (self.player_x, self.player_y))

            # Dash Animation
            elif self.isDashing:
                if not self.isJumpingDash:
                    if self.isFacingLeft:
                        win.blit(player_rLeft[self.runDashCount // 3], (self.player_x, self.player_y))
                    elif self.isFacingRight:
                        win.blit(player_rRight[self.runDashCount // 3], (self.player_x, self.player_y))
                # Jump Dash Animation
                elif self.isJumpingDash:
                    if self.isFacingLeft:
                        win.blit(player_jdLeft[self.jumpDashCount // 3], (self.player_x, self.player_y))
                    elif self.isFacingRight:
                        win.blit(player_jdRight[self.jumpDashCount // 3], (self.player_x, self.player_y))

            # Jump Animation
            elif self.isJumping:
                if self.isFacingLeft:
                    win.blit(player_jLeft[self.jumpCount // 3], (self.player_x, self.player_y))
                elif necromancer.isFacingRight:
                    win.blit(player_jRight[self.jumpCount // 3], (self.player_x, self.player_y))

            # Attack Animation
            elif self.isAttacking:
                if self.isFacingRight and not self.isJumping:
                    win.blit(player_aRight[self.attackCount // 3], (self.player_x, self.player_y))
                    win.blit(player_aGRight[self.attackCount // 3], (self.player_x + 100, self.player_y))
                elif self.isFacingLeft:
                    win.blit(player_aLeft[self.attackCount // 3], (self.player_x, self.player_y))
                    win.blit(player_aGLeft[self.attackCount // 3], (self.player_x - 100, self.player_y))

            # Hurt Animation
            elif self.isHurt:
                if self.isFacingRight:
                    win.blit(player_hurtR[self.hurtCount // 3], (self.player_x, self.player_y))
                elif self.isFacingLeft:
                    win.blit(player_hurtL[self.hurtCount // 3], (self.player_x, self.player_y))

            # Idle Animation
            else:
                if self.isFacingRight:
                    win.blit(player_idleR[self.idleCount // 3], (self.player_x, self.player_y))
                if self.isFacingLeft:
                    win.blit(player_idleL[self.idleCount // 3], (self.player_x, self.player_y))
                else:
                    win.blit(player_idleR[self.idleCount // 3], (self.player_x, self.player_y))

            # update current frames
            self.walkCount += 1
            self.idleCount += 1
            self.attackCount += 1
            self.runDashCount += 1
            self.jumpDashCount += 1
            self.hurtCount += 1

        def godModeToggle(self):

            if self.godMode:
                GodMode = Pixel.render("God Mode On", True, (107, 238, 77))
                win.blit(GodMode, (self.player_x + 25, self.player_y - 10))

    def damageHandler():
        # Player touch damage
        if not crusader.isDead:
            if player_hitbox.colliderect(enemy_hitbox) and not necromancer.isDashing and not necromancer.damageImmune:
                # print("Hit")
                necromancer.health -= 10
                necromancer.pointsMultiplier = 0
                necromancer.damageImmune = True
                necromancer.isHurt = True
                necromancer.isDamaged10 = True

    def pointsHandler():
        rx = random.randint(80, 100)
        ry = random.randint(80, 100)
        PointsIndicator = Pixel.render("Points: " + str(necromancer.points), True, (107, 238, 77))
        win.blit(PointsIndicator, (1100, 10))

        if necromancer.pointsMultiplier != 0 and necromancer.pointsVisible:
            pointsMult = Pixel3.render("x" + str(necromancer.pointsMultiplier), True, (0, 255, 0))
            win.blit(pointsMult, (1020 + rx, 520 + ry))
        if necromancer.pointsMultiplier >= 5 and necromancer.pointsVisible:
            pointsMult = Pixel3.render("x" + str(necromancer.pointsMultiplier), True, (203, 160, 38))
            win.blit(pointsMult, (1020 + rx, 520 + ry))
        if necromancer.pointsMultiplier >= 8 and necromancer.pointsVisible:
            pointsMult = Pixel3.render("x" + str(necromancer.pointsMultiplier), True, (252, 74, 30))
            win.blit(pointsMult, (1020 + rx, 520 + ry))
        if necromancer.pointsMultiplier >= 10 and necromancer.pointsVisible:
            pointsMult = Pixel3.render("x" + str(necromancer.pointsMultiplier), True, (252, 0, 0))
            win.blit(pointsMult, (1020 + rx, 520 + ry))

    def pointsAdd():
        necromancer.pointsMultiplier += 1
        if necromancer.pointsMultiplier != 0:
            necromancer.points += necromancer.pointsMultiplier * 50
        elif necromancer.pointsMultiplier == 0:
            necromancer.points += 50
        necromancer.pointsVisible = True

    def playerDamageHealth():
        # Show player touch damage
        rx = random.randint(50, 100)
        ry = random.randint(80, 100)
        if necromancer.isDamaged10:
            HealthDamage = Pixel.render("-" + str(crusader.damage), True, (255, 50, 77))
            win.blit(HealthDamage, (necromancer.player_x + rx, necromancer.player_y + ry))
            necromancer.pointsMultiplier = 0
            necromancer.pointsVisible = False

    def playerHealth():
        HealthIndicator = Pixel.render("Health: " + str(necromancer.health), True, (107, 238, 77))
        win.blit(HealthIndicator, (10, 10))

    def playerStamina():
        # r = random.randint(80, 100)
        if necromancer.isDashing or necromancer.isJumpingDash:
            necromancer.stamina -= 4
        elif necromancer.stamina < necromancer.maxStamina:
            necromancer.stamina += 1

        if necromancer.cooldownDash:
            StaminaLow = Pixel.render("Low stamina!", True, (107, 238, 77))
            win.blit(StaminaLow, (necromancer.player_x + 35, necromancer.player_y + 10,))

        StaminaIndicator = Pixel.render("Stamina: " + str(necromancer.stamina), True, (107, 238, 77))
        win.blit(StaminaIndicator, (10, 50))

    def playerAttackLeft():
        if player_atkleft.colliderect(enemy_hitbox) and not crusader.isDead:
            necromancer.isAttacking = True

            crusader.health -= necromancer.atkDamage
            crusader.isHurt = True
            crusader.isDamaged = True
            pointsAdd()

    def playerAttackRight():
        if player_atkright.colliderect(enemy_hitbox) and not crusader.isDead:
            necromancer.isAttacking = True
            crusader.isFollowing = False

            crusader.health -= necromancer.atkDamage
            crusader.isHurt = True
            crusader.isDamaged = True
            pointsAdd()

    class enemy(object):
        def __init__(self, enemy_x, enemy_y):
            self.enemy_x = enemy_x
            self.enemy_y = enemy_y
            self.width = 50
            self.height = 120
            self.enemy_location = enemy_x, enemy_y
            self.enemy_v = 5  # Velocity

            # enemy stats
            self.maxHealth = 100
            self.health = 100
            self.damage = 10
            self.isDamaged = False

            # animation state booleans
            self.isFollowing = False
            self.isFacingRight = False
            self.isFacingLeft = True
            self.isAttacking = False
            self.isIdle = True
            self.isReady = False
            self.isHurt = False
            self.isDead = False
            self.isDying = False

            # animation counts
            self.idleCount = 0
            self.walkCount = 0
            self.attackCount = 0
            self.hurtCount = 0
            self.dyingCount = 0

        def draw(self):

            if self.idleCount + 1 >= 30:
                self.idleCount = 0

            if self.walkCount + 1 >= 30:
                self.walkCount = 0

            if self.attackCount + 1 >= 30:
                self.attackCount = 0
                self.isAttacking = False

            if self.hurtCount + 1 >= 30:
                self.hurtCount = 0
                self.isHurt = False
                self.isDamaged = False

            if self.dyingCount + 1 >= 30:
                self.dyingCount = 0
                self.isDying = False

            if self.isFollowing:
                if self.isFacingRight:
                    win.blit(enemy_wRight[self.walkCount // 3], (self.enemy_x, self.enemy_y))
                elif self.isFacingLeft:
                    win.blit(enemy_wLeft[self.walkCount // 3], (self.enemy_x, self.enemy_y))

            elif self.isAttacking:
                if self.isFacingRight:
                    win.blit(enemy_aRight[self.attackCount // 3], (self.enemy_x, self.enemy_y))
                elif self.isFacingLeft:
                    win.blit(enemy_aLeft[self.attackCount // 3], (self.enemy_x, self.enemy_y))

            elif self.isHurt:
                if self.isFacingRight:
                    win.blit(enemy_hurtR[self.hurtCount // 3], (self.enemy_x, self.enemy_y))
                elif self.isFacingLeft:
                    win.blit(enemy_hurtL[self.hurtCount // 3], (self.enemy_x, self.enemy_y))

            else:
                if self.isFacingRight:
                    win.blit(enemy_idleR[self.idleCount // 3], (self.enemy_x, self.enemy_y))
                if self.isFacingLeft:
                    win.blit(enemy_idleL[self.idleCount // 3], (self.enemy_x, self.enemy_y))
                else:
                    win.blit(enemy_idleR[self.idleCount // 3], (self.enemy_x, self.enemy_y))

            # update current frames
            self.idleCount += 1
            self.walkCount += 1
            self.attackCount += 1
            self.hurtCount += 1

    def enemyFollow():
        if not crusader.isDead:
            if player_hitbox.colliderect(enemy_guard) and not necromancer.isDashing:
                crusader.walkCount = 0
                crusader.hurtCount = 0
                crusader.dyingCount = 0
                crusader.deadCount2 = 0
                crusader.isReady = True
                crusader.isFollowing = False
                enemyAttack()

            elif not crusader.isHurt:
                if player_hitbox.colliderect(enemy_range):
                    if crusader.enemy_x > necromancer.player_x:
                        crusader.enemy_x -= crusader.enemy_v - 2
                        crusader.idleCount = 0
                        crusader.attackCount = 0
                        crusader.isFacingRight = False
                        crusader.isAttacking = False

                        crusader.isFacingLeft = True
                        crusader.isFollowing = True
                        # print("IsFacing Left:", crusader.isFacingLeft)

                    elif crusader.enemy_y < necromancer.player_x:
                        crusader.enemy_x += crusader.enemy_v - 2
                        crusader.idleCount = 0
                        crusader.attackCount = 0
                        crusader.isFacingLeft = False
                        crusader.isAttacking = False

                        crusader.isFollowing = True
                        crusader.isFacingRight = True
                        # print("IsFacing Right:", crusader.isFacingRight)

            if not player_hitbox.colliderect(enemy_range):
                crusader.hurtCount = 0
                crusader.isFollowing = False
                crusader.isAttacking = False
                crusader.isDamaged = False
                crusader.isHurt = False

    def enemyAttack():
        if player_hitbox.colliderect(enemy_atkleft) and not necromancer.damageImmune and not crusader.isDamaged:
            crusader.walkCount = 0
            crusader.isAttacking = True
            crusader.isFacingLeft = True

            crusader.isFacingRight = False
            crusader.isReady = False
            crusader.isFollowing = False

            if crusader.attackCount == 6:
                necromancer.health -= crusader.damage
                necromancer.damageImmune = True
                necromancer.isHurt = True
                necromancer.isDamaged10 = True

        elif player_hitbox.colliderect(enemy_atkright) and not necromancer.damageImmune and not crusader.isDamaged:
            crusader.walkCount = 0
            crusader.isAttacking = True
            crusader.isFacingRight = True

            crusader.isFacingLeft = False
            crusader.isReady = False
            crusader.isFollowing = False

            if crusader.attackCount == 6:
                necromancer.health -= crusader.damage
                necromancer.damageImmune = True
                necromancer.isHurt = True
                necromancer.isDamaged10 = True

    def enemyDamageHealth():
        if not crusader.isDead:
            rx = random.randint(80, 100)
            ry = random.randint(80, 100)
            if crusader.isDamaged:
                EnemyHealthDamage = Pixel.render("-40", True, (255, 50, 77))
                win.blit(EnemyHealthDamage, (crusader.enemy_x + rx, crusader.enemy_y + ry))
                EnemyHealthDamage = Pixel.render("!!!", True, (255, 50, 77))
                win.blit(EnemyHealthDamage, (crusader.enemy_x + rx + 10, crusader.enemy_y + ry - 70))
            if crusader.health <= 0:
                crusader.isDead = True

    def debugKeys():
        if toggleTiles:  # render tiles
            drawTl(win, canvas_w, canvas_h, size=100)
        if toggleGrid:  # render playgrounds
            drawPg(win)
        if toggleHitbox:  # render player hitbox
            drawPhitbox(win, player_hitbox)
            drawPMeleeLeft(win, player_atkleft)
            drawPMeleeRight(win, player_atkright)
            drawEhitbox(win, enemy_hitbox)
            drawErangebox(win, enemy_range)
            drawEguardbox(win, enemy_guard)
            drawEatkleft(win, enemy_atkleft)
            drawEatkright(win, enemy_atkright)

    def spawnEnemy():
        x = random.randint(0, 1200)
        crusader.enemy_x = x
        crusader.draw()
        crusader.health = 100
        crusader.health += 50
        crusader.enemy_v += 1
        crusader.damage += 10
        crusader.isDead = False
        necromancer.health = necromancer.maxHealth

    def nextLevel():
        if not crusader.isDead:
            crusader.draw()
        elif crusader.isDead:
            necromancer.levelCounter += 1
            spawnEnemy()

    def levelIndicator():
        levelIndicatorText = Pixel2.render("Level: " + str(necromancer.levelCounter), True, (252, 252, 252))
        win.blit(levelIndicatorText, (550, 10))

    def pause():
        isPaused = True
        while isPaused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPaused = False
                    if event.key == pygame.K_r:
                        Start()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            s = pygame.Surface((1280, 720))

            s.fill((0, 0, 0))
            s.set_alpha(150)
            win.blit(s, (0, 0))
            drawText = Pixel.render('Paused', True, (26, 33, 41))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 50))
            drawText = Pixel.render('Press ESC again to resume', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 200))
            drawText = Pixel.render('Press R again to restart', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 300))
            drawText = Pixel.render('Press Q to quit', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 500))
            pygame.display.update()
            clock.tick(5)

    def gamelogs():
        # try:
        with open('gamelogs.csv') as csv_file:
            reader = csv.reader(csv_file)
            for i, _ in enumerate(reader):
                if i:  # found the second row
                    append()

    # except:
    #     gameV = gameVersion
    #     name = necromancer.name
    #     points = str(necromancer.points)
    #     levels = necromancer.levelCounter
    #     timestamp = str(gO.date)
    #     logs = ['Name', 'Points','Levels Cleared','Start Timestamp', 'Game Version']
    #     value = [name, points, levels, timestamp, gameV]
    #     with open('gamelogs.csv', 'w') as csv_file:
    #         csv_writer = csv.writer(csv_file, delimiter=',')
    #         csv_writer.writerow(logs)
    #         csv_writer.writerow(value)
    #     sys.exit()

    def append():
        name = necromancer.name
        points = str(necromancer.points)
        levels = str(necromancer.levelCounter)
        timestamp = str(gO.date)
        value = [name, points, levels, timestamp, gameVersion]
        with open('gamelogs.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(value)
        sys.exit()

    def gamelogsRestart():
        # try:
        with open('gamelogs.csv') as csv_file:
            reader = csv.reader(csv_file)
            for i, _ in enumerate(reader):
                if i:  # found the second row
                    appendRestart()
        # except:
        #     gameV = gameVersion
        #     name = necromancer.name
        #     points = str(necromancer.points)
        #     levels = necromancer.levelCounter
        #     timestamp = str(gO.date)
        #     logs = ['Name', 'Points','Levels Cleared','Start Timestamp', 'Game Version']
        #     value = [name, points, levels, timestamp, gameV]
        #     with open('gamelogs.csv', 'w') as csv_file:
        #         csv_writer = csv.writer(csv_file, delimiter=',')
        #         csv_writer.writerow(logs)
        #         csv_writer.writerow(value)
        #     sys.exit()

    def appendRestart():
        name = necromancer.name
        points = str(necromancer.points)
        levels = str(necromancer.levelCounter)
        timestamp = str(gO.date)
        value = [name, points, levels, timestamp, gameVersion]
        with open('gamelogs.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(value)
        Start()

    def gameOver():
        isPaused = True
        GameEnd.gameOver = True
        while isPaused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPaused = False
                    if event.key == pygame.K_r:
                        gamelogsRestart()
                    elif event.key == pygame.K_q:
                        gamelogs()
                        pygame.quit()

            s = pygame.Surface((1280, 720))
            s.fill((26, 33, 41))
            s.set_alpha(150)
            win.blit(s, (0, 0))

            gO.draw()

            drawText = Pixel2.render('Game Over', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 50))
            drawText = Pixel.render(necromancer.name, True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 200))
            drawText = Pixel.render('Overall Points:' + str(necromancer.points), True, (255, 0, 0))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 400))
            drawText = Pixel.render('Starting Timestamp: ' + str(gO.date), True, (255, 0, 0))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 450))
            drawText = Pixel.render('Press R to restart', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 500))
            drawText = Pixel.render('Press Q to quit', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 600))
            pygame.display.update()
            clock.tick(30)

    def getName():
        isPaused = True
        text = ""
        while isPaused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[0:-1]
                    elif event.key == pygame.K_RETURN:
                        if text == "":
                            necromancer.name = "Unknown Necromancer"
                        else:
                            necromancer.name = text
                        isPaused = False
                        necromancer.hasName = True
                    else:
                        text += event.unicode
                    # elif event.key == pygame.K_q:
                    #     pygame.quit()
                    #     gamelogs()

            s = pygame.Surface((1280, 720))
            s.fill((26, 33, 41))
            s.set_alpha(150)
            win.blit(s, (0, 0))

            drawText = Pixel.render('Enter your name', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 50))
            drawText = Pixel.render('Name: ', True, (255, 0, 0))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2) - 100, 200))
            drawText = Pixel.render(text, True, (0, 255, 0))
            win.blit(drawText, (600, 200))
            drawText = Pixel.render('Press ENTER to start game', True, (255, 255, 255))
            win.blit(drawText, ((1280 / 2) - (drawText.get_width() / 2), 500))
            pygame.display.update()
            clock.tick(30)

    def redrawGameWindow():
        win.fill((26, 33, 41))
        ThreadSprites()
        floorCorpse()
        floorDraw()
        nextLevel()
        # necromancer.draw()
        ThreadPlayer()
        musicPause.drawMusic()
        playerHealth()
        playerStamina()
        playerDamageHealth()
        enemyDamageHealth()
        pointsHandler()
        levelIndicator()
        debugKeys()
        necromancer.godModeToggle()
        pygame.display.update()

    # Main Loop
    necromancer = player(50, 400)
    crusader = enemy(500, 400)
    torchBG = torch(0, 400)
    Cthulu = cthuluhu(550, 140, 400, 100)
    gO = GameEnd(700, 200)
    musicPause = mixerWrapper()
    run = True
    while run:
        # The exit function
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_m:
                    musicPause.toggleMusic()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if necromancer.health <= 0:
            gameOver()
            gO.date = datetime.timestamp(now)

        if not necromancer.hasName:
            getName()

        clock.tick(30)

        # Hitboxes
        player_hitbox = pygame.draw.rect(win, (255, 0, 0),
                                         (necromancer.player_x + 80, necromancer.player_y + 45, 45, 120))
        player_atkleft = pygame.draw.rect(win, (255, 0, 0),
                                          (necromancer.player_x - 95, necromancer.player_y + 45, 175, 120))
        player_atkright = pygame.draw.rect(win, (255, 0, 0),
                                           (necromancer.player_x + 125, necromancer.player_y + 45, 175, 120))
        enemy_hitbox = pygame.draw.rect(win, (255, 0, 0),
                                        (crusader.enemy_x + 70,
                                         crusader.enemy_y + 45,
                                         crusader.width,
                                         crusader.height))
        enemy_range = pygame.draw.rect(win, (255, 0, 0),
                                       # -300
                                       (crusader.enemy_x - 1200,
                                        crusader.enemy_y - 250,
                                        crusader.width + 2400,
                                        crusader.height + 300))
        enemy_guard = pygame.draw.rect(win, (255, 0, 0),
                                       (crusader.enemy_x + 20,
                                        crusader.enemy_y - 250,
                                        crusader.width + 100,
                                        crusader.height + 300))
        enemy_atkleft = pygame.draw.rect(win, (255, 0, 0),
                                         (crusader.enemy_x + 20,
                                          crusader.enemy_y,
                                          crusader.width + 10,
                                          crusader.height + 50))
        enemy_atkright = pygame.draw.rect(win, (255, 0, 0),
                                          (crusader.enemy_x + 110,
                                           crusader.enemy_y,
                                           crusader.width + 10,
                                           crusader.height + 50))

        keys = pygame.key.get_pressed()
        # Move left
        if keys[pygame.K_a] and necromancer.player_x + 80 > 50 \
                and not necromancer.isAttacking and not necromancer.isHurt:
            necromancer.player_x -= necromancer.player_v

            necromancer.isLeft = True
            necromancer.isRight = False
            necromancer.idleCount = 0
            necromancer.attackCount = 0
            necromancer.runDashCount = 0
            necromancer.hurtCount = 0

            necromancer.isDashing = False
            necromancer.isFacingLeft = True
            necromancer.isFacingRight = False

        # Move right
        elif keys[pygame.K_d] and necromancer.player_x < 1120 \
                and not necromancer.isAttacking and not necromancer.isHurt:
            necromancer.player_x += necromancer.player_v

            necromancer.isRight = True
            necromancer.isLeft = False
            necromancer.idleCount = 0
            necromancer.attackCount = 0
            necromancer.runDashCount = 0
            necromancer.hurtCount = 0

            necromancer.isDashing = False
            necromancer.isFacingRight = True
            necromancer.isFacingLeft = False

        # Idle
        else:  # Idle
            necromancer.isLeft = False
            necromancer.isRight = False
            necromancer.walkCount = 0
            necromancer.runDashCount = 0
            necromancer.jumpDashCount = 0
            necromancer.isDashing = False
            necromancer.isJumpingDash = False

        # Toggle Dash
        if not necromancer.isHurt:
            if necromancer.stamina > 0 and not necromancer.cooldownDash:
                # Toggle Dash Left
                if keys[
                    pygame.K_LSHIFT] and necromancer.isFacingLeft \
                        and necromancer.player_x + 80 > 50 and not necromancer.isAttacking:
                    necromancer.player_x -= 50

                    necromancer.isRight = False
                    necromancer.isLeft = False
                    necromancer.isFacingLeft = True
                    necromancer.isFacingRight = False
                    necromancer.idleCount = 0
                    necromancer.attackCount = 0
                    necromancer.walkCount = 0
                    necromancer.jumpDashCount = 0
                    necromancer.isDashing = True
                    necromancer.isTired = True

                # Toggle Dash Right
                elif keys[pygame.K_LSHIFT] and necromancer.isFacingRight \
                        and necromancer.player_x < 1120 and not necromancer.isAttacking:
                    necromancer.player_x += 50

                    necromancer.isRight = False
                    necromancer.isLeft = False
                    necromancer.isFacingLeft = False
                    necromancer.isFacingRight = True
                    necromancer.idleCount = 0
                    necromancer.attackCount = 0
                    necromancer.walkCount = 0
                    necromancer.jumpDashCount = 0
                    necromancer.hurtCount = 0
                    necromancer.isDashing = True
                    necromancer.isTired = True

            elif necromancer.cooldownDash:
                if necromancer.dashCounterCooldown >= necromancer.cooldownDashTimer:
                    necromancer.cooldownDash = False
                    necromancer.dashCounterCooldown = 0
                    # print("Cooldown Dash lifted")
                else:
                    necromancer.dashCounterCooldown += 1
                    # print(necromancer.counter)
            else:
                necromancer.isJumpingDash = False
                necromancer.isDashing = False
                necromancer.isTired = True
                necromancer.cooldownDash = True
                # print("Cooldown Dash applied")

        # Attack
        if keys[pygame.K_j] and not necromancer.isHurt:
            if not necromancer.isAttacking and not necromancer.isJumping:
                necromancer.isAttacking = True
                if necromancer.isFacingLeft:
                    playerAttackLeft()
                elif necromancer.isFacingRight:
                    playerAttackRight()

        # Jump
        if not necromancer.isJumping:  # Jump
            if keys[pygame.K_SPACE]:
                necromancer.isJumping = True

                necromancer.isLeft = False
                necromancer.isRight = False
                necromancer.isAttacking = False
                necromancer.walkCount = 0
                necromancer.attackCount = 0
                necromancer.runDashCount = 0
                necromancer.hurtCount = 0
                necromancer.isDashing = False

        # Jump Physics
        else:  # Jump Physics
            if necromancer.jumpCount >= -10:
                necromancer.player_y -= (necromancer.jumpCount * abs(necromancer.jumpCount)) * .5
                necromancer.jumpCount -= 1
            else:
                necromancer.jumpCount = 10
                necromancer.attackCount = 0
                necromancer.isJumping = False

        # Jump facing left Animation
        if necromancer.isJumping and keys[pygame.K_a]:
            necromancer.isJumping = True
            necromancer.isLeft = False
            necromancer.isFacingLeft = True
            necromancer.isFacingRight = False

        # Jump facing right Animation
        elif necromancer.isJumping and keys[pygame.K_d]:
            necromancer.isJumping = True
            necromancer.isRight = False
            necromancer.isFacingLeft = False
            necromancer.isFacingRight = True

        # Dash direction animation
        if not necromancer.isTired:
            # Dash facing left Animation
            if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                # Toggle Dash Left
                if keys[pygame.K_LSHIFT] and necromancer.isFacingLeft \
                        and necromancer.player_x + 80 > 50 and not necromancer.isAttacking:
                    necromancer.player_x -= 50

                    necromancer.isRight = False
                    necromancer.isLeft = False
                    necromancer.isFacingLeft = True
                    necromancer.isFacingRight = False
                    necromancer.idleCount = 0
                    necromancer.attackCount = 0
                    necromancer.walkCount = 0
                    necromancer.isDashing = True

            # Dash facing Right Animation
            elif keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
                # Toggle Dash Right
                if keys[pygame.K_LSHIFT] and necromancer.isFacingRight \
                        and necromancer.player_x < 1020 and not necromancer.isAttacking:
                    necromancer.player_x += 50

                    necromancer.isRight = False
                    necromancer.isLeft = False
                    necromancer.isFacingLeft = False
                    necromancer.isFacingRight = True
                    necromancer.idleCount = 0
                    necromancer.attackCount = 0
                    necromancer.walkCount = 0
                    necromancer.isDashing = True

        # Jump Dash direction animation
        if not necromancer.isTired and necromancer.isJumping and necromancer.isDashing:
            # Jump Dash facing left Animation
            if necromancer.isFacingLeft:
                necromancer.isJumpingDash = True
                necromancer.isLeft = False
                necromancer.isFacingLeft = True
                necromancer.isFacingRight = False

            # Jump Dash facing right Animation
            elif necromancer.isFacingRight:
                necromancer.isJumpingDash = True
                necromancer.isRight = False
                necromancer.isFacingLeft = False
                necromancer.isFacingRight = True

        # Toggle GUI Debug
        if keys[pygame.K_h]:  # toggle player hitbox
            toggleHitbox = True
        else:
            toggleHitbox = False
        if keys[pygame.K_g]:  # toggle grid playgrounds
            toggleGrid = True
        else:
            toggleGrid = False
        if keys[pygame.K_v]:  # toggle tile playgrounds
            toggleTiles = True
        else:
            toggleTiles = False
        if keys[pygame.K_p]:
            necromancer.health = 9999
            necromancer.maxHealth = 9999
            necromancer.stamina = 9999
            necromancer.maxStamina = 9999
            necromancer.godMode = True
        if keys[pygame.K_o]:
            necromancer.health = 100
            necromancer.maxHealth = 100
            necromancer.stamina = 100
            necromancer.maxStamina = 100
            necromancer.godMode = False

        # Damage Cooldown
        if necromancer.damageImmune:
            if necromancer.damageImmuneCounter >= necromancer.damageImmuneTimer:
                necromancer.damageImmuneCounter = 0
                necromancer.damageImmune = False
            else:
                necromancer.damageImmuneCounter += 1

        if not necromancer.damageImmune:
            damageHandler()

        # Enemy Handlers
        ThreadEnemy()
        redrawGameWindow()

    pygame.quit()
