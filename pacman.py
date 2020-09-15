import pygame
import os
import sys


#initialise the game 
pygame.init()
screen = pygame.display.set_mode((448, 576))
done = False

y = 416
x = 232

#sets up clock and loads pacman image
clock = pygame.time.Clock()
PACMANSPRITE = pygame.image.load("pacman.png").convert_alpha()
PACMAN_MAP = pygame.image.load("pacman_map.png").convert_alpha()

#gets pacman intro music, sets music to lower volume then plays it
pygame.mixer.music.load('pacman_beginning.WAV')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(0)


#box class, used for boxes to border pacmans map
class boxcollisions(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.rect = pygame.Rect(self.x, self.y, 12, 12)
        self.colour = (0, 128, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class pointclass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.rect = pygame.Rect(self.x, self.y, 12, 12)
        self.colour = (255, 204, 153)
        self.score=0

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def addpoint(self):
        self.score+=1
        print(self.score)
        self.colour= (0,0,0)
        print('why isnt it working')

#pacmans class
class pacman(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = image
        self.y=416
        self.x=216
        self.currentx=self.x
        self.currenty=self.y
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.rect.width=16
        self.rect.height=16

    # move pacman 
    def movement(self):
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.y -= 2
        if pressed[pygame.K_DOWN]:
            self.y += 2
        if pressed[pygame.K_LEFT]:
            self.x -= 2
        if pressed[pygame.K_RIGHT]:
            self.x += 2
        self.rect.left = self.x
        self.rect.top = self.y

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
        self.currentx=self.x
        self.currenty=self.y

    def outofbounds(self):
        self.y=self.currenty
        self.x=self.currentx
        self.rect.left = self.x
        self.rect.top = self.y

#instances the pacman class
sprite = pacman(PACMANSPRITE, x ,y)


#main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    sys.exit()


    screen.fill((0,0,0))
    screen.blit(PACMAN_MAP, (0, 0))

    #co-ordinates for boxes to set up map boundaries
    boxboundaries=[   
        [],
        [],
        [],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],
        [1,14,15,28], #5
        [1,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,28],
        [1,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,28],
        [1,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,28],
        [1,28],
        [1,3,4,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,28], #10
        [1,3,4,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,28],
        [1,8,9,14,15,20,21,28],
        [1,2,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,27,28],
        [1,2,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,27,28],
        [6,8,9,20,21,23], #15
        [6,8,9,11,12,13,14,15,16,17,18,20,21,23],
        [1,2,3,4,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,27,28],
        [1,11,12,13,14,15,16,17,18,28],
        [1,2,3,4,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,27,28],
        [6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,27,28], #20
        [6,8,9,20,21,23],
        [6,8,9,11,12,13,14,15,16,17,18,20,21,23],
        [1,2,3,4,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,25,26,27,28],
        [1,14,15,28],
        [1,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,28], #25
        [1,3,4,5,6,8,9,10,11,12,14,15,17,18,19,20,21,23,24,25,26,28],
        [1,5,6,23,24,28],
        [1,2,3,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,26,27,28],
        [1,2,3,5,6,8,9,11,12,13,14,15,16,17,18,20,21,23,24,26,27,28],
        [1,8,9,14,15,20,21,28], # 30
        [1,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20,21,22,23,24,25,26,28],
        [1,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20,21,22,23,24,25,26,28],
        [1,28],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],                   
      ]


    #point spawn locations
    pointspawns=[ 
        [],
        [],
        [],
        [],
        [2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27], #5
        [2,7,13,16,22,27],
        [2,7,13,16,22,27],
        [2,7,13,16,22,27],
        [2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], 
        [2,7,10,19,22,27], #10
        [2,7,10,19,22,27],
        [2,3,4,5,6,7,10,11,12,13,16,17,18,19,22,23,24,25,26,27],
        [7,22],
        [7,22],
        [7,22], #15
        [7,22],
        [7,22],
        [7,22],
        [7,22],
        [7,22], #20
        [7,22],
        [7,22],
        [7,22],
        [2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27],
        [2,7,13,16,22,27], #25
        [2,7,13,16,22,27],
        [2,3,4,7,8,9,10,11,12,13,16,17,18,19,20,21,22,25,26,27],
        [4,7,10,19,22,25],
        [4,7,10,19,22,25],
        [2,3,4,5,6,7,10,11,12,13,16,17,18,19,22,23,24,25,26,27],
        [2,13,16,27], # 30
        [2,13,16,27],
        [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],                       
      ]

    #moves pacman
    sprite.movement()

    px=0
    py=-16

    for row in pointspawns:
        #y co ordinate
        py=py+16    
        for n in row:
            #x co ordinate
            n=n-1
            px=n*16
            point=(pointclass(px, py))
            #used to draw points
            point.draw(screen)
            if pygame.sprite.collide_rect(sprite, point):
                point.addpoint()


    #builds the boxes
    bx=0
    by=-16


    for row in boxboundaries:
        #y co ordinate
        by=by+16    
        for n in row:
            #x co ordinate
            n=n-1
            bx=n*16
            box=(boxcollisions(bx, by))
            #used to draw boxes for visual repsentation
            #box.draw(screen)
            if pygame.sprite.collide_rect(sprite, box):
                sprite.outofbounds()



    #draws pacman
    sprite.draw(screen)


    pygame.display.flip()
    clock.tick(60)

