import pygame
pygame.font.init()
pygame.init()
import os
import sqlite3

con = sqlite3.connect('winners.db')
cur = con.cursor()
#cur.execute('''CREATE TABLE stocks
#    (who_win text, numbers int, onewin int, twowin int)''')
scr_width = 500
scr_height= 500
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Ping_Pong")

FPS = 60

screen.fill((255, 255, 255))

game = True

clock = pygame.time.Clock()

path1 = os.path.join(os.getcwd(), "images")

mach = os.path.join(path1, "mach.png")
mach = pygame.image.load(mach)

palka = os.path.join(path1, "palka.png")
palka = pygame.image.load(palka)

numbers_win = 0
def numbers_win1():
    global numbers_win
    numbers_win += 1
numbers_win1()
numbers_win -= 1

one_win = 0
def one_win1():
    global one_win
    one_win += 1
one_win1()
one_win -= 1

two_win = 0
def two_win1():
    global two_win
    two_win += 1
two_win1()
two_win -= 1

end3 = 0
def end1():
    global end3
    end3 += 1
end1()
end3 -= 1

winner = 0
def winner1():
    global winner
    winner += 1
winner1()
winner -= 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (self.rect.w, self.rect.h))

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed, key_up, key_down):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def move(self):
        if (pygame.key.get_pressed()[self.key_up] and self.rect.y >= 0):
            self.rect.y -= self.speed
        if (pygame.key.get_pressed()[self.key_down] and self.rect.y <= 400):
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, x, y, w, h, image, speed_x, speed_y, end3):
        super().__init__(x, y, w, h, image)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        global end3
        global winner
        #Движение мяча
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #Нижняя граница
        if self.rect.y >= scr_height - self.rect.height:
            self.speed_y *= -(1)
        #Верхняя граница
        if self.rect.y <= 50 - self.rect.width:
            self.speed_y *= -(1)
        #Левый игрок
        if pygame.Rect.colliderect(self.rect, rocket1.rect):
            self.speed_x *= -(1)
        #Правый игрок
        if pygame.Rect.colliderect(self.rect, rocket2.rect):
            self.speed_x *= -(1)
        #who_win text, numbers int, onewin int, twowin int
        if self.rect.x >= 500:
            end3 = 2 
            winner = 1
            numbers_win1()
            one_win1()
            cur.execute("INSERT INTO stocks VALUES ('Player1', ?, ?, ?)", [numbers_win, one_win, two_win])
            cur.execute('''select * from stocks''')
            print(cur.fetchall())
        if self.rect.x <= -50:
            end3 = 2 
            winner = 2
            numbers_win1()
            two_win1()
            cur.execute("INSERT INTO stocks VALUES ('Player2', ?, ?, ?)", [numbers_win, one_win, two_win])
            cur.execute('''select * from stocks''')
            print(cur.fetchall())
        

ball = Ball(220, 200, 50, 50, mach, 2, 2, end3)
rocket1 = Player(50, 200, 10, 100, palka, 5, pygame.K_w, pygame.K_s)
rocket2 = Player(450, 200, 10, 100, palka, 5, pygame.K_UP, pygame.K_DOWN)

def numbers(text1, shirina, x_cord, y_cord, color, txt):                              
    f1 = pygame.font.SysFont("Arial", shirina)                                             
    text1 = f1.render(txt + str(text1), True, (color))                           
    screen.blit(text1, (x_cord, y_cord))      

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        end3 = 0
        winner = 0
        ball.rect.x = 200
        ball.rect.y = 200
    screen.fill((255, 255, 255))
    if end3 == 0:
        ball.move()
        ball.draw()
        print(end3)
    if winner != 0:
        if winner == 1:
            numbers(" 1 победил!", 30, 100, 250, (180, 0, 0), 'Игрок номер')
        if winner == 2:
            numbers(" 2 победил!", 35, 100, 200, (180, 0, 0), 'Игрок номер')
    rocket1.draw()
    rocket2.draw()
    rocket1.move()
    rocket2.move()
    pygame.display.update()
    clock.tick(FPS)
