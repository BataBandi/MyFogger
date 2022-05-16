import sys
import pygame
import random
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MyFogger')

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
VEL = 1
FPS = 60

pygame.key.set_repeat(1)

#Idő
clock = pygame.time.Clock() 

#Szöveg
font = pygame.font.Font('freesansbold.ttf', 48)
text_rect = pygame.Rect(300, 0, 48, 50)
##parameterek
direction = 1
speed_x = 5
speed_y = 4
test = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Hatterkep betoltese
background_filename ='./kepek/bg.jpg'
background = pygame.image.load('./kepek/bg.jpg')
background = pygame.transform.scale(background,(900, 900))
background_rect = pygame.Rect(0, 0, 900, 900)

#Beka
Frog_filename = './kepek/Frogg.png'
Frog = pygame.image.load('./kepek/Frogg.png')
Frog = pygame.transform.scale(Frog, (50, 50))
Frog_rect = pygame.Rect(400, 690, 90, 80)
#Autok
Auto1_filename ='.kepek/car1.png'
Auto2_filename ='.kepek/car2.png'
Auto3_filename ='.kepek/car3.png'
Auto4_filename ='.kepek/car4.png'
Auto5_filename ='.kepek/car5.png'
Auto1 = pygame.image.load('./kepek/car1.png')
Auto2 = pygame.image.load('./kepek/car2.png')
Auto3 = pygame.image.load('./kepek/car3.png')
Auto4 = pygame.image.load('./kepek/car4.png')
Auto5 = pygame.image.load('./kepek/car5.png')
Auto1 = pygame.transform.scale(Auto1, (90, 80))
Auto2 = pygame.transform.scale(Auto2, (90, 80))
Auto3 = pygame.transform.scale(Auto3, (90, 80))
Auto4 = pygame.transform.scale(Auto4, (90, 80))
Auto5 = pygame.transform.scale(Auto5, (90, 80))
Auto1_rect = pygame.Rect(-55, 580, 90, 80)
Auto2_rect = pygame.Rect(870, 480, 90, 80)
Auto3_rect = pygame.Rect(-70, 360, 90, 80)
Auto4_rect = pygame.Rect(870, 240, 90, 80)
Auto5_rect = pygame.Rect(-70, 130, 90, 80)

#Finish
Cel_filename = './kepek/cel.jpg'
Cel = pygame.image.load('./kepek/cel.jpg')
Cel = pygame.transform.scale(Cel, (30, 30))
Cel_rect = pygame.Rect(400, 70, 30, 30)
#Classok    
class Game():
    def __init__(self, Object):
        self.Object = Object

class Object(Game):
    def __init__(self, frog, Auto, Cel):
        self.frog = Frog
        self.Auto = Auto
        self.Cel = Cel

class frog(Object):
    def __init__(self, start_position, dead, lives):
        self.start_position = start_position
        self.move = move
        self.dead = dead
        self.lives = 3       
        
    def lives(self):
        if is_connected == False:
            lives -=1
            
        if lives == 0:
            return
    
    def start_position(self):
        self.start_position = Frog(400, 680)
                             
    
class Enemy(Object):
    def __init__(self, Autos: list, position, spawn):
        self.position = position
        self.spawn = rect              
        self.Autos = list
        
class Autos(Enemy):
    def __init__(self, spawn, position, move, collision):
        self.spawn = spawn
        self.position = position
        self.move = move
        self.collision = collide
        
    def spawn(Autos):
        if clock.tick(FPS) == True:
            Autos.rect, list.append(Autos)           
            
def main():
    
    Ido = 0
    Points = 0
    is_connected = False
    
    clock = pygame.time.Clock()
    
    run = True
    
    while run:
                
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.QUIT or 
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                return 
            
            if event.type == KEYDOWN:
                if event.key == K_d:
                    Frog_rect.x += VEL
                if event.key == K_a:
                    Frog_rect.x -= VEL
                if event.key == K_w:
                    Frog_rect.y -= VEL
                if event.key == K_s:
                    Frog_rect.y += VEL 
                    
        if Auto1_rect.x > -100:
            Auto1_rect.x += VEL
        elif Auto1_rect.x > 400:
            Auto1.get_rect()
        if Auto2_rect.x < 890:
            Auto2_rect.x -= VEL
        elif Auto2_rect.x < 400:
            Auto2.get_rect()
        if Auto3_rect.x > -100:
            Auto3_rect.x += VEL
        if Auto4_rect.x < 890:
            Auto4_rect.x -= VEL
        elif Auto4_rect.x < 400:
            Auto4.get_rect()
        if Auto5_rect.x > -100:
            Auto5_rect.x += VEL
        elif Auto5_rect.x > 400:
            Auto5.get_rect()
            
        if Auto1_rect.colliderect(Frog_rect) and (is_connected == False):
            is_connected = True
        
        if Auto2_rect.colliderect(Frog_rect) and (is_connected == False):
            is_connected = True
       
        if Auto3_rect.colliderect(Frog_rect) and (is_connected == False):
            is_connected = True
        
        if Auto4_rect.colliderect(Frog_rect) and (is_connected == False):
            is_connected = True
            
        if Auto5_rect.colliderect(Frog_rect) and (is_connected == False):
            is_connected = True

        if Cel_rect.colliderect(Frog_rect) and (is_connected == False):
            Points += 1
            is_connected = True

        if not Cel_rect.colliderect(Frog_rect):
            is_connected = False 
            
        pont_szamlalo = font.render(f'Points: {Points}', True, RED)
        pont_szamlalo_rect = pont_szamlalo.get_rect()
        pont_szamlalo_rect.x = 50
        pont_szamlalo_rect.y = 70
        
        if FPS == 60:
            Ido += 0.02
            
        ido_szamlalo = font.render(f'Time: {Ido}', True, RED)
        ido_szamlalo_rect = ido_szamlalo.get_rect()
        ido_szamlalo_rect.x = 700
        ido_szamlalo_rect.y = 70
              
        #Dolgok megjelenítése
        WIN.fill(WHITE)
        
        WIN.blit(background, (background_rect.x, background_rect.y))
        
        WIN.blit(Cel, (Cel_rect.x, Cel_rect.y))
        
        WIN.blit(Frog, (Frog_rect.x, Frog_rect.y))
       
        WIN.blit(Auto1, (Auto1_rect.x, Auto1_rect.y))  
        
        WIN.blit(Auto2, (Auto2_rect.x, Auto2_rect.y))
        
        WIN.blit(Auto3, (Auto3_rect.x, Auto3_rect.y))
        
        WIN.blit(Auto4, (Auto4_rect.x, Auto4_rect.y))
        
        WIN.blit(Auto5, (Auto5_rect.x, Auto5_rect.y))
        
        WIN.blit(pont_szamlalo, (pont_szamlalo_rect.x, pont_szamlalo_rect.y))
        
        WIN.blit(ido_szamlalo, (ido_szamlalo_rect.x, ido_szamlalo_rect.y))
        
        pygame.display.update()                 
        
    pygame.quit

    
if __name__ == '__main__':
    main()