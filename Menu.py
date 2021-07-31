import pygame
import sys
import csv

intro_BG = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 00.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 01.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 02.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 03.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 04.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 05.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 06.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 08.png'),
            pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 09.png')]
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
intro_BGs = [pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png'),
             pygame.image.load('assets/Pixel/Sprites/Necromancer/Intro/v1/Necromancer Intro 07.png')]

win = pygame.display.set_mode((1280, 720))  # Resolution


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -80

        self.x = 535
        self.y = 150
        self.introChar = True
        self.introCount = 0

        self.torch_x = 200
        self.torch_y = 200
        self.torchCount = 0
        self.torch1 = True

    def draw(self):
        if self.introCount + 1 >= 30:
            self.introCount = 0

        if self.torchCount + 1 >= 30:
            self.torchCount = 0

        if self.introChar:
            win.blit(intro_BGs[self.introCount // 3], (self.x, self.y))

        if self.torch1:
            win.blit(torch_BG[self.torchCount // 3], (self.torch_x - 100, self.torch_y))
            win.blit(torch_BG[self.torchCount // 3], (self.torch_x + 800, self.torch_y))

        self.torchCount += 1
        self.introCount += 1

    def draw_cursor(self):
        self.game.draw_text('->', 20, self.cursor_rect.x, self.cursor_rect.y + 20)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        self.draw()
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.leaderx, self.leadery = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLUE)
            self.game.draw_text('Necromancer', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty + 20)
            self.game.draw_text("Controls", 20, self.optionsx, self.optionsy + 20)
            self.game.draw_text("Leaderboards", 20, self.leaderx, self.leadery + 20)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy + 20)
            self.game.draw_text("v0.2.1", 20, 35, 705)
            self.game.draw_text("ESC to exit", 20, 1220, 705)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.leaderx + self.offset, self.leadery)
                self.state = 'Leaderboards'
            elif self.state == 'Leaderboards':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Leaderboards':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Controls'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.leaderx + self.offset, self.leadery)
                self.state = 'Leaderboards'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.options
            elif self.state == 'Leaderboards':
                self.game.curr_menu = self.game.leaderboards
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False
        elif self.game.ESC_KEY:
            pygame.quit()
            sys.exit()


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((26, 33, 41))
            self.game.draw_text(" Use WASD keys to move.", 20, 625, 360)
            self.game.draw_text(" Use SPACE to jump.", 20, 625, 400)
            self.game.draw_text(" Use LEFT SHIFT to dash.", 20, 625, 440)
            self.game.draw_text(" Use J to attack.", 20, 625, 480)
            self.game.draw_text(" System Debug Controls:", 20, 250, 360)
            self.game.draw_text(" Use P to Toggle GodMode", 20, 250, 390)
            self.game.draw_text(" Use O to Un-Toggle GodMode", 20, 250, 410)
            self.game.draw_text(" Use M to Turn Music On/Off GodMode", 20, 250, 430)
            self.game.draw_text(" Graphics Debug Controls:", 20, 1000, 360)
            self.game.draw_text(" Hold G to show Playable Grid", 20, 1000, 390)
            self.game.draw_text(" Hold H to show Hitboxes", 20, 1000, 410)
            self.game.draw_text(" Hold V to show Tile Maps", 20, 1000, 430)
            self.game.draw_text(" BACKSPACE or ENTER to go back.", 20, 1110, 705)
            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY or self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False


class LeaderboardsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.List = []
        self.appendY = 0
        self.top1 = " "
        self.top2 = " "
        self.top3 = " "
        self.top4 = " "
        self.top5 = " "

        with open("gamelogs.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for lines in csv_reader:
                x = lines['Name']
                y = lines['Points']
                self.List.append(y + '        ' + x)

        for i in range(0, len(self.List) - 1):
            for j in range(len(self.List) - 1):
                if self.List[j] > self.List[j + 1]:
                    self.List[j], self.List[j + 1] = self.List[j + 1], self.List[j]

        self.List.reverse()
        self.top1 = self.List[1]
        self.top2 = self.List[2]
        self.top3 = self.List[3]
        self.top4 = self.List[4]
        self.top5 = self.List[5]

    def display_menu(self):

        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLUE)
            self.game.draw_text('TOP 5 LEADERBOARDS', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)

            # for y in range(5): print(self.List[y]) self.top = self.List[y] self.game.draw_text(self.top, 20,
            # self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30 + self.appendY) self.appendY += 20

            self.game.draw_text(self.top1, 20, self.game.DISPLAY_W / 2, 380)
            self.game.draw_text(self.top2, 20, self.game.DISPLAY_W / 2, 400)
            self.game.draw_text(self.top3, 20, self.game.DISPLAY_W / 2, 420)
            self.game.draw_text(self.top4, 20, self.game.DISPLAY_W / 2, 440)
            self.game.draw_text(self.top5, 20, self.game.DISPLAY_W / 2, 460)
            self.game.draw_text(" BACKSPACE or ENTER to go back.", 20, 1110, 705)
            self.blit_screen()


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLUE)
            self.game.draw_text('NECROMANCER', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Developers:', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('Dela Cruz, Prince Kyle', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Mon, Jemaica', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text(" BACKSPACE or ENTER to go back.", 20, 1110, 705)
            self.blit_screen()
