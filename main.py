# pygame template
import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

#Initialize
pygame.init()
#Set screen dimensions
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
#Create screen
screen = pygame.display.set_mode(SIZE)
#Create clock
clock = pygame.time.Clock()
#Name the program
pygame.display.set_caption("ENTER TITLE")

# ---------------------------
# Fonts
menu_font = pygame.font.SysFont("Georgia", 25, True, False)
health_font = pygame.font.SysFont("Georgia", 14, True, False)

# Menu Buttoms
shop_button = pygame.Rect(800, 700, 200, 100)  # (RIGHT SIDE)
play_button = pygame.Rect(400, 700, 200, 100) # (MIDDLE)
instructions_button = pygame.Rect(0, 700, 200, 100) # (LEFT SIDE)

# ---------------------------
#Game runs while running is True
running = True
#Current screen being displayed
current_screen = "menu"

# ---------------------------

#Display menu function
def run_menu():
    menu = True
    while menu:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = False
            elif event.type == QUIT:
                menu = False

        # GAME STATE UPDATES
        # All game math and comparisons happen here

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        # BACKGROUND
        #Sky
        for i in range (0, 200, 1):
            pygame.draw.line(screen, (i,0,75), [0,2*i], [1000,2*i], 5)
        #Grass
        for i in range (0, 200, 1):
            pygame.draw.line(screen, (0,i,0), [0,400+2*i], [1000,400+2 *i], 5)

        # BUTTONS
        #Shop Button
        pygame.draw.ellipse(screen, (0, 0, 0), shop_button, 0)
        shop_text = menu_font.render("SHOP", True, (255, 255, 0))
        screen.blit(shop_text, [860, 735])
        #Play button
        pygame.draw.ellipse(screen, (0, 0, 0), play_button, 0)
        play_text = menu_font.render("PLAY", True, (255, 255, 0))
        screen.blit(play_text, [460, 735])
        #Instruction Button
        pygame.draw.ellipse(screen, (0, 0, 0), instructions_button, 0)
        rules_text = menu_font.render("RULES", True, (255, 255, 0))
        screen.blit(rules_text, [50, 735])

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(60)

#Display rules function
def run_rules():
    rules = True
    while rules:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rules = False
            elif event.type == QUIT:
                rules = False

        # GAME STATE UPDATES
        # All game math and comparisons happen here

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        # BACKGROUND
        for i in range(161):
            pygame.draw.line(screen, (80+i, 40+i, 60+i//2), [0,5*i], [1000,5*i], 5)



        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(60)
        # ---------------------------

#DIsplay game
def run_game():
    health = 1000
    play = True
    while play:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    play = False
            elif event.type == QUIT:
                play = False

        # GAME STATE UPDATES
        # All game math and comparisons happen here

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        # LEFT BOARD
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 200, 800], 0)
        # Health Bar
        pygame.draw.rect(screen, (255, 0, 0), [5, 5, 190, 20], 0)
        pygame.draw.rect(screen, (0, 255, 0), [5, 5, 190*(health/1000), 20], 0)
        health_text = health_font.render(f"{health}/1000", True, (0, 0, 0))
        screen.blit(health_text, [60, 5])
        # Character
        pygame.draw.rect(screen, (155, 136, 187), [5, 30, 190, 190], 0)
        # Passive
        pygame.draw.rect(screen, (255, 255, 255), [5, 225, 50, 50], 0)
        # Ability 1
        pygame.draw.rect(screen, (255, 255, 255), [5, 280, 50, 50], 0)
        # Ability 2
        pygame.draw.rect(screen, (255, 255, 255), [5, 335, 50, 50], 0)
        # Ability 3
        pygame.draw.rect(screen, (255, 255, 255), [5, 390, 50, 50], 0)
        # Ultimate Ability
        pygame.draw.rect(screen, (255, 255, 255), [5, 445, 50, 50], 0)


        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(60)
        # ---------------------------


# ---------------------------
run_game()

while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
