# pygame template
import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_BACKSPACE

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
game_font = pygame.font.SysFont("Georgia", 14, False, False)
faction_name_font = pygame.font.SysFont("Georgia", 32, True, False)

# Colours
DEFAULT = (49, 51, 53)

# Buttons
shop_button = pygame.Rect(800, 700, 200, 100)  # (RIGHT SIDE)
play_button = pygame.Rect(400, 700, 200, 100) # (MIDDLE)
instructions_button = pygame.Rect(0, 700, 200, 100) # (LEFT SIDE)
view_back_button = pygame.Rect(300, 645, 100, 50) # (ON THE FACTION SELECT SCREEN)

#Select Buttons
select_button_1 = pygame.Rect(300, 200, 190, 85)
select_button_2 = pygame.Rect(700, 200, 190, 85)
select_button_3 = pygame.Rect(300, 600, 190, 85)
select_button_4 = pygame.Rect(700, 600, 190, 85)

#Info/View Buttons
view_button_1 = pygame.Rect(300, 290, 190, 85)
view_button_2 = pygame.Rect(700, 290, 190, 85)
view_button_3 = pygame.Rect(300, 690, 190, 85)
view_button_4 = pygame.Rect(700, 690, 190, 85)

# ---------------------------
#Game runs while running is True
running = True
# #Current screen being displayed
# current_screen = "menu"

# ---------------------------
#Drawing Faction Icons
def faction_1_icon(x, y):
    pygame.draw.rect(screen, (255, 0, 0), [x, y, 190, 190], 0)
def faction_2_icon(x, y):
    pygame.draw.rect(screen, (0, 255, 0), [x, y, 190, 190], 0)
def faction_3_icon(x, y):
    pygame.draw.rect(screen, (0, 0, 255), [x, y, 190, 190], 0)
def faction_4_icon(x, y):
    pygame.draw.rect(screen, (255, 255, 0), [x, y, 190, 190], 0)

#Display Faction select
def faction_select():
    # Faction Select Grid 2x2
    pygame.draw.line(screen, (0, 0, 0), [600, 0], [600, 800], 1)
    pygame.draw.line(screen, (0, 0, 0), [200, 400], [1000, 400], 1)
    # Faction 1 Display
    faction_1_icon(300, 5)
    pygame.draw.rect(screen, (0, 0, 0), select_button_1, 0)
    select_text_1 = menu_font.render("Select", True, (255, 255, 255))
    screen.blit(select_text_1, [355, 225])
    pygame.draw.rect(screen, (0, 0, 0), view_button_1, 0)
    view_text_1 = menu_font.render("View", True, (255, 255, 255))
    screen.blit(view_text_1, [360, 315])
    # Faction 2 Display
    faction_2_icon(700, 5)
    pygame.draw.rect(screen, (0, 0, 0), select_button_2, 0)
    select_text_2 = menu_font.render("Select", True, (255, 255, 255))
    screen.blit(select_text_2, [755, 225])
    pygame.draw.rect(screen, (0, 0, 0), view_button_2, 0)
    view_text_2 = menu_font.render("View", True, (255, 255, 255))
    screen.blit(view_text_2, [760, 315])
    # Faction 3 Display
    faction_3_icon(300, 405)
    pygame.draw.rect(screen, (0, 0, 0), select_button_3, 0)
    select_text_3 = menu_font.render("Select", True, (255, 255, 255))
    screen.blit(select_text_3, [355, 625])
    pygame.draw.rect(screen, (0, 0, 0), view_button_3, 0)
    view_text_3 = menu_font.render("View", True, (255, 255, 255))
    screen.blit(view_text_3, [360, 715])
    # Faction 4 Display
    faction_4_icon(700, 405)
    pygame.draw.rect(screen, (0, 0, 0), select_button_4, 0)
    select_text_4 = menu_font.render("Select", True, (255, 255, 255))
    screen.blit(select_text_4, [755, 625])
    pygame.draw.rect(screen, (0, 0, 0), view_button_4, 0)
    view_text_4 = menu_font.render("View", True, (255, 255, 255))
    screen.blit(view_text_4, [760, 715])

#Display Ability List
def abilities(x, y, r, g, b):
    # Basic Attack (Click)
    pygame.draw.rect(screen, (r, g, b), [x, y, 50, 50], 0)
    passive_text = game_font.render("B", True, (255-r, 255-g, 255-b))
    screen.blit(passive_text, [x+2, y])
    # Ability 1
    pygame.draw.rect(screen, (r, g, b), [x, y+55, 50, 50], 0)
    a1_text = game_font.render("1", True, (255 - r, 255 - g, 255 - b))
    screen.blit(a1_text, [x+2, y+55])
    # Ability 2
    pygame.draw.rect(screen, (r, g, b), [x, y+110, 50, 50], 0)
    a2_text = game_font.render("2", True, (255 - r, 255 - g, 255 - b))
    screen.blit(a2_text, [x+2, y+110])
    # Ultimate Ability
    pygame.draw.rect(screen, (r, g, b), [x, y+165, 50, 50], 0)
    ult_text = game_font.render("3", True, (255 - r, 255 - g, 255 - b))
    screen.blit(ult_text, [x+2, y+165])

#Display game
def run_game():
    #Health
    total_health = 10000
    current_health = 1000
    #Selected Faction - 0 means none
    faction = 0
    #Which character - 0 means none
    view = 0

    play = True
    while play:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    play = False
                elif faction == 0 and view != 0 and event.key == K_BACKSPACE:
                    view = 0
            elif event.type == QUIT:
                play = False
            elif event.type == MOUSEBUTTONDOWN:
                if faction == 0:
                    #If a faction has not been selected yet (i.e. On Faction Selection Screen)
                    select_1_hit = select_button_1.collidepoint(event.pos)
                    select_2_hit = select_button_2.collidepoint(event.pos)
                    select_3_hit = select_button_3.collidepoint(event.pos)
                    select_4_hit = select_button_4.collidepoint(event.pos)
                    view_1_hit = view_button_1.collidepoint(event.pos)
                    view_2_hit = view_button_2.collidepoint(event.pos)
                    view_3_hit = view_button_3.collidepoint(event.pos)
                    view_4_hit = view_button_4.collidepoint(event.pos)
                    if view == 0:
                        if select_1_hit == 1:
                            faction = 1
                        elif select_2_hit == 1:
                            faction = 2
                        elif select_3_hit == 1:
                            faction = 3
                        elif select_4_hit == 1:
                            faction = 4
                        elif view_1_hit == 1:
                            view = 1
                        elif view_2_hit == 1:
                            view = 2
                        elif view_3_hit == 1:
                            view = 3
                        elif view_4_hit == 1:
                            view = 4
                    else:
                        back_button_hit = view_back_button.collidepoint(event.pos)
                        if back_button_hit == 1:
                            view = 0

        # GAME STATE UPDATES
        # All game math and comparisons happen here

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        # LEFT BOARD
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 200, 800], 0)
        # Health Bar
        pygame.draw.rect(screen, (175, 0, 0), [5, 5, 190, 20], 0)
        pygame.draw.rect(screen, (34, 139, 34), [5, 5, 190*(current_health/total_health), 20], 0)
        health_text = health_font.render(f"{current_health}/{total_health}", True, (0, 0, 0))
        screen.blit(health_text, [60, 5])
        current_health+=2

        # Faction Icon + Border
        pygame.draw.rect(screen, DEFAULT, [5, 30, 190, 190], 0)
        pygame.draw.rect(screen, (175, 0, 175), [5, 30, 190, 190], 2)
        # Display Abilities
        abilities(5, 225, 255, 255, 255)

        # RIGHT SCREEN
        if faction == 0:
            if view == 0:
                faction_select()
            elif view == 1:
                view_faction1()
                #Back Button
                pygame.draw.rect(screen, (0,0,0), view_back_button, 0)
                back_text = menu_font.render("BACK", True, (175, 0, 175))
                screen.blit(back_text, [310, 653])
            elif view == 2:
                view_faction2()
                #Back Button
                pygame.draw.rect(screen, (0,0,0), view_back_button, 0)
                back_text = menu_font.render("BACK", True, (175, 0, 175))
                screen.blit(back_text, [310, 653])
            elif view == 3:
                view_faction3()
                #Back Button
                pygame.draw.rect(screen, (0,0,0), view_back_button, 0)
                back_text = menu_font.render("BACK", True, (175, 0, 175))
                screen.blit(back_text, [310, 653])
            elif view == 4:
                view_faction4()
                #Back Button
                pygame.draw.rect(screen, (0,0,0), view_back_button, 0)
                back_text = menu_font.render("BACK", True, (175, 0, 175))
                screen.blit(back_text, [310, 653])

        elif faction == 1:
            faction_1_icon(5, 30)
            pygame.draw.rect(screen, (175, 0, 175), [5, 30, 190, 190], 2)
        elif faction == 2:
            faction_2_icon(5, 30)
            pygame.draw.rect(screen, (175, 0, 175), [5, 30, 190, 190], 2)
        elif faction == 3:
            faction_3_icon(5, 30)
            pygame.draw.rect(screen, (175, 0, 175), [5, 30, 190, 190], 2)
        elif faction == 4:
            faction_4_icon(5, 30)
            pygame.draw.rect(screen, (175, 0, 175), [5, 30, 190, 190], 2)

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(60)

# ---------------------------


# Faction 1 Info
def view_faction1():
    #Icon
    faction_1_icon(300,30)
    pygame.draw.rect(screen, (175, 0, 175), [300, 30, 190, 190], 2)
    #Faction Name
    faction_name_text = faction_name_font.render("Faction: PYRO", True, (255,0,0))
    screen.blit(faction_name_text, [300, 225])
    #Faction Description
    line_1 = game_font.render("The Pyro wield the elementary power of heat and fire.", True, (0,0,0))
    line_2 = game_font.render("WIP", True, (0,0,0))
    screen.blit(line_1, [300, 275])
    screen.blit(line_2, [300, 300])
    #Abilities
    abilities(300, 425, 0, 0, 0)

# Faction 2 Info
def view_faction2():
    #Icon
    faction_2_icon(300,30)
    pygame.draw.rect(screen, (175, 0, 175), [300, 30, 190, 190], 2)
    #Faction Name
    faction_name_text = faction_name_font.render("Faction: NATURO", True, (0,255,0))
    screen.blit(faction_name_text, [300, 225])
    #Faction Description
    line_1 = game_font.render("The Naturo wield the ancient ability to harness nature and heal.", True, (0,0,0))
    line_2 = game_font.render("WIP", True, (0,0,0))
    screen.blit(line_1, [300, 275])
    screen.blit(line_2, [300, 300])
    #Abilities
    abilities(300, 425, 0, 0, 0)


# Faction 3 Info
def view_faction3():
    #Icon
    faction_3_icon(300,30)
    pygame.draw.rect(screen, (175, 0, 175), [300, 30, 190, 190], 2)
    #Faction Name
    faction_name_text = faction_name_font.render("Faction: CRYO", True, (0,0,255))
    screen.blit(faction_name_text, [300, 225])
    #Faction Description
    line_1 = game_font.render("The Cryo wield the freezing weapons of water and ice.", True, (0,0,0))
    line_2 = game_font.render("WIP", True, (0,0,0))
    screen.blit(line_1, [300, 275])
    screen.blit(line_2, [300, 300])
    #Abilities
    abilities(300, 425, 0, 0, 0)

# Faction 4 Info
def view_faction4():
    #Icon
    faction_4_icon(300,30)
    pygame.draw.rect(screen, (175, 0, 175), [300, 30, 190, 190], 2)
    #Faction Name
    faction_name_text = faction_name_font.render("Faction: ELECTRO", True, (255,255,0))
    screen.blit(faction_name_text, [300, 225])
    #Faction Description
    line_1 = game_font.render("The Electro wield the innovative tools of light and electricity.", True, (0,0,0))
    line_2 = game_font.render("WIP", True, (0,0,0))
    screen.blit(line_1, [300, 275])
    screen.blit(line_2, [300, 300])
    #Abilities
    abilities(300, 425, 0, 0, 0)


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

#ACTUAL CODE TO RUN
while running:
    run_menu()
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
