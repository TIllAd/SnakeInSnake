import pygame

WIDTH  = 800
HEIGHT = 600

BG = pygame.image.load("Media/background.jpg")
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))

pygame.font.init()
pygame.display.set_caption("looool")

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)

def draw():

   # WIN.blit(background,(0,0))

    displaytext = FONT.render(f"Hallo",1,"white")

    WIN.blit(displaytext,(10,10))
    

    #t4wt4

    pygame.display.update()

def draw_menu(BG):

    WIN.blit(BG,(0,0))
    pygame.display.update()

def play():

    while True:

        print("heöloo")
        
    #play logic

def menu():

    while True:
        draw_menu(BG)

run = True

while run:

    menu()



# def menu():

#     while True:

#         draw_menu()


#187





