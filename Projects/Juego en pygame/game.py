import pygame
from sys import exit
from time import sleep
from random import randint

class Player:

    speed = 4
    directions = {"down":False, "up":False, "right":False, "left":False}

    def __init__(self, x, y, direction = True, life=100, score=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.life = life
        self.score = score
    
    def move(self):
        if Player.directions["down"]:
            player_obj.y += Player.speed
        if Player.directions["up"]: 
            player_obj.y -= Player.speed
        if Player.directions["right"]:
            player_obj.x += Player.speed
        if Player.directions["left"]:
            player_obj.x -= Player.speed
    
class Enemy:

    speed = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def follow(self,x_obj, y_obj):
        if x_obj > self.x:
            self.x += Enemy.speed
        if x_obj < self.x:
            self.x -= Enemy.speed
        if y_obj > self.y:
            self.y += Enemy.speed
        if y_obj < self.y:
            self.y -= Enemy.speed

class Bullet:

    speed = 5
    bullets = {"L":[], "R":[]}

    def __init__(self, x, y, direction="R"):
        self.x = x
        self.y = y
        self.speed = Bullet.speed
        self.direction = direction

    def update(self):
        if self.direction == "R":
            self.x += self.speed
        elif self.direction == "L":
            self.x -= self.speed  

    def shoot(self, enemys, player):
        self.update()
        for enemy in enemys:
            if enemy.x == self.x and (enemy.y >= self.y - 40 and enemy.y <= self.y + 40):
                enemys.remove(enemy)
                player.score += 1
    
    def show(self):
        screen.blit(bullet, (self.x, self.y))

def read_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Player.directions["down"] = True
            if event.key == pygame.K_UP:
                Player.directions["up"] = True
            if event.key == pygame.K_RIGHT:
                Player.directions["right"], player_obj.direction = True, True
            if event.key == pygame.K_LEFT:
                Player.directions["left"], player_obj.direction = True, False

            if event.key == pygame.K_SPACE:
                bullet_obj = Bullet(player_obj.x, player_obj.y)
                if player_obj.direction:
                    bullet_obj.x = player_obj.x + 20
                    Bullet.bullets["R"].append(bullet_obj)
                else:
                    bullet_obj.direction="L"
                    Bullet.bullets["L"].append(bullet_obj)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                Player.directions["down"] = False
            if event.key == pygame.K_UP:
                Player.directions["up"] = False
            if event.key == pygame.K_RIGHT:
                Player.directions["right"] = False
            if event.key == pygame.K_LEFT:
                Player.directions["left"] = False


def final_state(player):
    score_rend = score.render(str(player.score), False, "Black")
    score_rect = score_rend.get_rect(midtop = (750,30))
    screen.blit(score_rend, score_rect)

    if player.score >= 10:
        enemy_obj.clear()
        title_rend = title.render("You won! :)", False, "Green")
        screen.blit(title_rend, (300, 200))

    if player.life <=0:
        title_rend = title.render("You lose :(", False, "Red")
        screen.blit(title_rend, (300, 200))    
        


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Test game")

clock = pygame.time.Clock()
title = pygame.font.Font("projects\\BirdGame\\Minecraft.ttf", 50) # argumentos: tipo de letra y tamaño
score = pygame.font.Font("projects\\BirdGame\\Minecraft.ttf", 30)

sky = pygame.image.load("projects\\BirdGame\\cielo.png").convert() # directorio e imagen
player = pygame.image.load("projects\\BirdGame\\patoframe0.png").convert_alpha() # conversión para manejar los canales alfa
enemy = pygame.image.load("projects\\BirdGame\\frame1z.png").convert_alpha()
bullet = pygame.image.load("projects\\BirdGame\\bala.png").convert_alpha()

title_rend = title.render("First Game", False, "Black") # texto, antialiasing, color

player_obj = Player(randint(10,789),randint(10,389))
enemy_obj = [Enemy(randint(10,789),randint(10,389)) for _ in range(11)]

def main():

    initial_time = pygame.time.get_ticks()

    while True:
        in_game_time = (pygame.time.get_ticks() - initial_time )/1000

        if in_game_time > 5 and in_game_time < 10:
            Enemy.speed = 1.5
        elif in_game_time > 10 and in_game_time < 15:
            Enemy.speed = 1.8
        elif in_game_time > 15:
            Enemy.speed = 2.5

        screen.blit(sky, (0,0))
        pygame.draw.rect(screen,"Red",pygame.Rect(10,10,player_obj.life, 20)) # display_surface, color, surface
        screen.blit(player, (player_obj.x, player_obj.y))

        for i in enemy_obj:
            screen.blit(enemy, (i.x, i.y))
            i.follow(player_obj.x, player_obj.y)
        
        read_input()
        player_obj.move()

        for element in Bullet.bullets.values():
            for i in element:
                i.shoot(enemy_obj, player_obj)
            for i in element:
                i.show()

        for i in enemy_obj:
            if (i.x <= player_obj.x + 15 and i.x >= player_obj.x - 15) and (i.y <= player_obj.y + 15 and i.y >= player_obj.y - 15 ):
                player_obj.life -= 1
        
        final_state(player_obj)
        pygame.display.update()
        clock.tick(60)

main()