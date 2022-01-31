__author__ = 'A. Sangha'
"""
Date: Jan 25, 2022
File Name: Platformer
Description: Simple 1 level platformer
"""

import pygame

pygame.init()

#Colours if needed
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)

#Screen size
size = (width,height) = (800,800)

#Variables for scrren and game
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2D Platfromer")
clock = pygame.time.Clock()
fps = 120

running = True

#Load background image
bg = pygame.image.load('Background/background_0001.png')
background = pygame.transform.scale(bg, (height, width))

#Create the player object
class Player():
    def __init__(self, x, y):
        char = pygame.image.load('Characters/character_0000.png')
        self.image = pygame.transform.scale(char, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx = 0
        dy = 0

        #What to do when keys are pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_a]:
            dx -= 5
        if key[pygame.K_d]:
            dx += 5

        #Gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #Collision
        self.in_air = True
        for tile in level.grid:
     
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
          
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
               
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
             
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False

        #Update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0

        screen.blit(self.image, self.rect)
        
#Create size for grid and map
tile_size = 40

#Create the map object
class Map():
    def __init__(self,data):
        grass = pygame.image.load('Tiles/tile_0000.png')
        dirt = pygame.image.load('Tiles/tile_0029.png')
        water = pygame.image.load('Tiles/tile_0053.png')
        box = pygame.image.load('Tiles/tile_0047.png')
        pipe = pygame.image.load('Tiles/tile_0095.png')
        side_tube = pygame.image.load('Tiles/tile_0113.png')
        flag_base = pygame.image.load('Tiles/tile_0131.png')
        flag_top = pygame.image.load('Tiles/tile_0111.png')
        self.grid = []

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(water, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(box, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(pipe, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(side_tube, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(flag_base, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(flag_top, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.grid.append(tile)
                col_count += 1
            row_count += 1
    
    #Draw the images on the map
    def draw_map(self):
        for tile in self.grid:
            screen.blit(tile[0], tile[1])

#Map level
level_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,0,0,0,0,4,0,0,0,0,4,0,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [0,0,0,0,0,4,4,0,0,0,4,0,0,4,0,0,0,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,4,0,0,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
    [0,0,0,0,0,2,2,2,0,0,0,0,2,2,2,2,2,1,1,1],
    [2,2,2,2,2,1,1,1,3,3,3,3,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

#Spawn player
player = Player(100, height - 130)
level = Map(level_map)

#Game loop
while running:

    clock.tick(fps)
    screen.blit(background, (0,0))
    level.draw_map()
    player.update()

    #Keep player on the screen
    if player.rect.x > 760:
        player.rect.x = 760
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.y < 0:
        player.rect.y = 0
    
    #Respawn player if they touch the water
    if 640 < player.rect.y < 800 and 320 < player.rect.x < 480:
        player.rect.y = 680
        player.rect.x = 80

    #End the game and show the end screen
    if 40 < player.rect.x < 120 and 40 < player.rect.y < 120:
        Win_Image = pygame.image.load('PngItem_1725256.png')
        Win_Image = pygame.transform.scale(Win_Image, (800,800))
        screen.blit(Win_Image, (0,0))
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    pygame.display.update()

pygame.time.wait(5000)
print('Program ended.')
