from pygame import *        # import * from pygame
import sys                  # import sys
import pygame               # import pygame


def menu_screen(Button, run_game):                          # function for screen menu
    """make the screen for menu"""
    display.set_caption("Jet Mission")                      # the title of the game
    screen = pygame.display.set_mode((800, 600))            # screen width and height
    #object button for quit and start
    start_button = Button("New Piskel.png")                 # insert the start button image
    quit_button = Button("quit button.png")                 # insert the quit button image
    #image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")       # insert background image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) # set the width and height
    pygame.init()           # intialize pygame

    while True:             # loop
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) # set rectangle when the game start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  # set rectangle when the game end
        screen.blit(bg_image, (0, 0))                                     # call background image 0,0

        screen.blit(start_button.button, (250, 200))          # set start button's size
        screen.blit(quit_button.button, (250, 300))           # set quit button's size

        ev = event.wait()                                     # set the amount of time for pause

        if ev.type == MOUSEBUTTONDOWN:          # if you right click the mouse, run the code
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:                     # if you press quit, run the code
            sys.exit()

        display.update()


def pause_menu(Button,run_game):        # function for pause menu
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission")                      # game title
    screen = pygame.display.set_mode((800, 600))            # game title's size

    # object button for quit and start
    start_button = Button("quit button.png")                # start button image
    return_button = Button("pause button.png")              # quit button image

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")       # background image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) # background size

    pygame.init()        # initialize pygame
    paused = True # pause flag
    while paused:   # puase loop
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))  # set rectangle when the game start
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  # set rectangle when the game end
        screen.blit(bg_image, (0, 0))  # call background image 0,0

        screen.blit(start_button.button, (250, 200))  # set start button's size
        screen.blit(return_button.button, (250, 300))  # set quit button's size

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                menu_screen(Button, run_game)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False # flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()


def lose_menu(Button,run_game,score):
    """make the screen for menu"""
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("times new roman", 100)
    text = font.render("Replay?", True, (255, 255, 255))
    score_text = font.render("score:"+str(score), True, (255, 255, 255))

    # object button for quit and start
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) # set rectangle when the game start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  # set rectangle when the game end
        screen.blit(bg_image, (0, 0))  # call background image 0,0
        screen.blit(text, (200, 10))                                    # set text's size
        screen.blit(start_button.button, (250, 200))                    # set start button's size
        screen.blit(quit_button.button, (250, 300))                     # set quit button's size
        screen.blit(score_text, (200, 400))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:          # if you right click the mouse, run the code
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:                     # if you press quit, run the code
            sys.exit()
            
        display.update()