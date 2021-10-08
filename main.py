# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 23:00:40 2021

@author: ESHAN
"""


import pygame
import random
pygame.font.init()
pygame.mixer.init()

HIT_SOUND = pygame.mixer.Sound("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/Gun+Silencer.mp3")

WIDTH, HEIGHT = 1050, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND = pygame.Rect(0, 410, WIDTH, 4)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CHIP_1 = pygame.Rect(1050 - 50, 420, 6, 3)
CHIP_2 = pygame.Rect(1050 - 200, 430, 8, 4)
CHIP_3 = pygame.Rect(1050 - 350, 425, 5, 3)
CHIP_4 = pygame.Rect(1050 - 400, 435, 9, 4)
CHIP_5 = pygame.Rect(1050 - 500, 430, 8, 4)
CHIP_6 = pygame.Rect(1050 - 550, 425, 5, 3)
CHIP_7 = pygame.Rect(1050 - 100, 435, 9, 4)
pygame.display.set_caption("DINOSAUR GAME")

HIT = pygame.USEREVENT + 1

FPS = 120

DINO_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/dino.png"), (60,65))
DINO = DINO_IMAGE.get_rect()
DINO.center = (200,381)

UPPER_BIRD_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/bird.png"), (30, 25))
UPPER_BIRD = UPPER_BIRD_IMAGE.get_rect()

BIG_CACTUS_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/small cactus.png"), (30, 50))
BIG_CACTUS = BIG_CACTUS_IMAGE.get_rect()

SMALL_CACTUS_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/small cactus.png"), (20, 40))
SMALL_CACTUS = SMALL_CACTUS_IMAGE.get_rect()

LOWER_BIRD_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/bird.png"), (30, 25))
LOWER_BIRD = LOWER_BIRD_IMAGE.get_rect()

TREE_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/tree.png"), (25, 40))
TREE = TREE_IMAGE.get_rect()

HUGE_CACTUS_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/huge cactus.png"), (65, 50))
HUGE_CACTUS = HUGE_CACTUS_IMAGE.get_rect()

TWO_CACTUS_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/two cactus.png"), (65, 50))
TWO_CACTUS = TWO_CACTUS_IMAGE.get_rect()

PLANE_1_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/plane 1.png"), (85, 70)), -30)
PLANE_1 = PLANE_1_IMAGE.get_rect()
PLANE_1.center = (-800, 100)

PLANE_2_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/plane 2.png"), (50, 80)), 90)
PLANE_2 = PLANE_2_IMAGE.get_rect()
PLANE_2.center = (WIDTH + 20, 150)

CLOUD_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/GOOGLE DINOSAUR GAME/MAIN CODE FILE/data/cloud.png"), (75, 50))
CLOUD_IMAGE_x = WIDTH
CLOUD = CLOUD_IMAGE.get_rect()



OBJECTS = [UPPER_BIRD_IMAGE, LOWER_BIRD_IMAGE, BIG_CACTUS_IMAGE, 
           SMALL_CACTUS_IMAGE, TREE_IMAGE, HUGE_CACTUS_IMAGE, TWO_CACTUS_IMAGE]
RANDOM_OBJECT_IMAGE = random.choice(OBJECTS)
RANDOM_OBJECT = RANDOM_OBJECT_IMAGE.get_rect()

RANDOM_OBJECT_IMAGE_x = WIDTH




def chips_formation():  
    global CHIP_1   
    pygame.draw.rect(WINDOW, BLACK, CHIP_1)
    CHIP_1.x -= 3
    if CHIP_1.x < 5:
        CHIP_1_X = random.randint(400, 1000)
        CHIP_1 = pygame.Rect(CHIP_1_X, 420, 6, 3)
        pygame.draw.rect(WINDOW, BLACK, CHIP_1)
        CHIP_1.x -= 3

    global CHIP_2   
    pygame.draw.rect(WINDOW, BLACK, CHIP_2)
    CHIP_2.x -= 3
    if CHIP_2.x < 10:
        CHIP_2_X = random.randint(800, 1000)
        CHIP_2 = pygame.Rect(CHIP_2_X, 430, 8, 4)
        pygame.draw.rect(WINDOW, BLACK, CHIP_2)
        CHIP_2.x -= 3

    global CHIP_3   
    pygame.draw.rect(WINDOW, BLACK, CHIP_3)
    CHIP_3.x -= 3
    if CHIP_3.x < 0:
        CHIP_3_X = random.randint(600, 1000)
        CHIP_3 = pygame.Rect(CHIP_3_X, 425, 5, 3)
        pygame.draw.rect(WINDOW, BLACK, CHIP_3)
        CHIP_3.x -= 3

    global CHIP_4   
    pygame.draw.rect(WINDOW, BLACK, CHIP_4)
    CHIP_4.x -= 3 
    if CHIP_4.x < 50:
        CHIP_4_X = random.randint(300, 1000)
        CHIP_4 = pygame.Rect(CHIP_4_X, 435, 9, 4)
        pygame.draw.rect(WINDOW, BLACK, CHIP_4)
        CHIP_4.x -= 3

    global CHIP_5 
    pygame.draw.rect(WINDOW, BLACK, CHIP_5)
    CHIP_5.x -= 3
    if CHIP_5.x < 100:
        CHIP_5_X = random.randint(700, 1000)
        CHIP_5 = pygame.Rect(CHIP_5_X, 430, 8, 4)
        pygame.draw.rect(WINDOW, BLACK, CHIP_5)
        CHIP_5.x -= 3
 
    global CHIP_6   
    pygame.draw.rect(WINDOW, BLACK, CHIP_6)
    CHIP_6.x -= 3
    if CHIP_6.x < 0:
        CHIP_6_X = random.randint(200, 1000)
        CHIP_6 = pygame.Rect(CHIP_6_X, 425, 5, 3)
        pygame.draw.rect(WINDOW, BLACK, CHIP_6)
        CHIP_6.x -= 3

    global CHIP_7    
    pygame.draw.rect(WINDOW, BLACK, CHIP_7)
    CHIP_7.x -= 3
    if CHIP_7.x < 80:
        CHIP_7_X = random.randint(600, 1000)
        CHIP_7 = pygame.Rect(CHIP_7_X, 435, 9, 4)
        pygame.draw.rect(WINDOW, BLACK, CHIP_7)
        CHIP_7.x -= 3
 



def draw_board():
    WINDOW.fill(WHITE)
    
    WINDOW.blit(DINO_IMAGE, DINO)
    
    WINDOW.blit(PLANE_1_IMAGE, PLANE_1)
    PLANE_1.x += 1
    if PLANE_1.x > WIDTH + 300:
        WINDOW.blit(PLANE_2_IMAGE, PLANE_2)
        PLANE_2.x -= 1
    
    pygame.draw.rect(WINDOW, BLACK, GROUND)
    
    
    global RANDOM_OBJECT_IMAGE_x
    global RANDOM_OBJECT_IMAGE
    RANDOM_OBJECT_IMAGE_x -= 3
    if RANDOM_OBJECT_IMAGE == UPPER_BIRD_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 352
    if RANDOM_OBJECT_IMAGE == LOWER_BIRD_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 367
    if RANDOM_OBJECT_IMAGE == BIG_CACTUS_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 365
    if RANDOM_OBJECT_IMAGE == SMALL_CACTUS_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 375
    if RANDOM_OBJECT_IMAGE == TREE_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 372
    if RANDOM_OBJECT_IMAGE == HUGE_CACTUS_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 373
    if RANDOM_OBJECT_IMAGE == TWO_CACTUS_IMAGE:
        RANDOM_OBJECT_IMAGE_y = 370
    RANDOM_OBJECT.topleft = (RANDOM_OBJECT_IMAGE_x, RANDOM_OBJECT_IMAGE_y)

    
    if DINO.colliderect(RANDOM_OBJECT):
        pygame.event.post(pygame.event.Event(HIT))
        
    WINDOW.blit(RANDOM_OBJECT_IMAGE, RANDOM_OBJECT)
    UPPER_BIRD.x -= 3
    LOWER_BIRD.x -= 3
    BIG_CACTUS.x -= 3
    SMALL_CACTUS.x -= 3
    TWO_CACTUS.x -= 3 
    TREE.x -= 3
    HUGE_CACTUS.x -= 3
        
    if RANDOM_OBJECT_IMAGE_x < -20:
        RANDOM_OBJECT_IMAGE_x = WIDTH 
        RANDOM_OBJECT_IMAGE = random.choice(OBJECTS)
        WINDOW.blit(RANDOM_OBJECT_IMAGE, (RANDOM_OBJECT_IMAGE_x, RANDOM_OBJECT_IMAGE_y))


    global CLOUD_IMAGE_x
    CLOUD_IMAGE_x -= 1
    WINDOW.blit(CLOUD_IMAGE, (CLOUD_IMAGE_x, 200)) 
    if CLOUD_IMAGE_x < -60:
        CLOUD_IMAGE_x = WIDTH
    
    chips_formation()    
    pygame.display.update()



def main(): 
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == HIT:
                HIT_SOUND.play()
                pygame.time.delay(3000)
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and DINO.y > 348  :
                    WINDOW.blit(DINO_IMAGE, DINO)
                    DINO.y -= 75
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if DINO.y < 348:
                        DINO.y += 75    
                    else:
                        continue
     
        
        draw_board()
    pygame.quit()
    
if __name__ == "__main__":
    main()