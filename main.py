# pygame template
import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

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
#Display game
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
        pygame.draw.rect(screen, (175, 0, 0), [5, 5, 190, 20], 0)
        pygame.draw.rect(screen, (34, 139, 34), [5, 5, 190*(health/10000), 20], 0)
        health_text = health_font.render(f"{health}/10000", True, (0, 0, 0))
        screen.blit(health_text, [60, 5])
        # health+=50

        # Character Icon
        pygame.draw.rect(screen, (214, 138, 89), [5, 30, 190, 190], 0)
        # Passive
        pygame.draw.rect(screen, (255, 255, 255), [5, 225, 50, 50], 0)
        # Ability 1
        pygame.draw.rect(screen, (255, 255, 255), [5, 280, 50, 50], 0)
        # Ability 2
        pygame.draw.rect(screen, (255, 255, 255), [5, 335, 50, 50], 0)
        # Ultimate Ability
        pygame.draw.rect(screen, (255, 255, 255), [5, 390, 50, 50], 0)


        # MAIN SCREEN
        # Character Select
        pygame.draw.line(screen, (0,0,0), [600,0], [600,800], 1)
        pygame.draw.line(screen, (0,0,0), [200, 400], [1000, 400], 1)

        # Character 1
        pygame.draw.rect(screen, (255, 0, 0), [300, 5, 190, 190], 0)
        pygame.draw.rect(screen, (0, 0, 0), [300, 200, 190, 85], 0)
        select_text_1 = menu_font.render("Select", True, (255, 255, 255))
        screen.blit(select_text_1, [355, 225])
        pygame.draw.rect(screen, (0, 0, 0), [300, 290, 190, 85], 0)
        view_text_1 = menu_font.render("View", True, (255, 255, 255))
        screen.blit(view_text_1, [360, 315])

        # Character 2
        pygame.draw.rect(screen, (0, 255, 0), [700, 5, 190, 190], 0)
        pygame.draw.rect(screen, (0, 0, 0), [700, 200, 190, 85], 0)
        select_text_2 = menu_font.render("Select", True, (255, 255, 255))
        screen.blit(select_text_2, [755, 225])
        pygame.draw.rect(screen, (0, 0, 0), [700, 290, 190, 85], 0)
        view_text_2 = menu_font.render("View", True, (255, 255, 255))
        screen.blit(view_text_2, [760, 315])

        # Character 3
        pygame.draw.rect(screen, (0, 0, 255), [300, 405, 190, 190], 0)
        pygame.draw.rect(screen, (0, 0, 0), [300, 600, 190, 85], 0)
        select_text_3 = menu_font.render("Select", True, (255, 255, 255))
        screen.blit(select_text_3, [355, 625])
        pygame.draw.rect(screen, (0, 0, 0), [300, 690, 190, 85], 0)
        view_text_3 = menu_font.render("View", True, (255, 255, 255))
        screen.blit(view_text_3, [360, 715])

        # Character 4
        pygame.draw.rect(screen, (255, 255, 0), [700, 405, 190, 190], 0)
        pygame.draw.rect(screen, (0, 0, 0), [700, 600, 190, 85], 0)
        select_text_4 = menu_font.render("Select", True, (255, 255, 255))
        screen.blit(select_text_4, [755, 625])
        pygame.draw.rect(screen, (0, 0, 0), [700, 690, 190, 85], 0)
        view_text_4 = menu_font.render("View", True, (255, 255, 255))
        screen.blit(view_text_4, [760, 715])

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(60)
        # ---------------------------

# Character 1 Info

# Character 2 Info

# Character 3 Info

# Character 4 Info


#Display menu function
def run_menu():
    global running
    menu = True
    while menu:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = False
                    running = False
            elif event.type == QUIT:
                menu = False
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                play_hit = play_button.collidepoint(event.pos)
                instructions_hit = instructions_button.collidepoint(event.pos)
                if play_hit == 1:
                    print("HIT PLAY")
                    run_game()
                elif instructions_hit == 1:
                    print("HIT RULES")
                    run_rules()
                else:
                    print("HIT NOTHING")

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



# ---------------------------


while running:
    run_menu()
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        # elif event.type == MOUSEBUTTONDOWN:
        #     play_hit = play_button.collidepoint(event.pos)
        #     instructions_hit = instructions_button.collidepoint(event.pos)
        #     if play_hit == 1:
        #         print("HIT PLAY")
        #         run_game()
        #     elif instructions_hit == 1:
        #         print("HIT RULES")
        #         run_rules()
        #     else:
        #         print("HIT NOTHING")

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
