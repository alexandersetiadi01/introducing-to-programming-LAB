from pygame import *        # we import * from pygame
import menu                 # import menu file to this
import random               # import random
from classes import *       # import * from classes file


def run_game():             # function to run the game
    """game play interface"""
    screen = pygame.display.set_mode((800, 600))    # set the height and width of the screen
    display.set_caption("Jet mission")              # set the title of the game

    scores = 0                          # set the score start from 0
    theClock = pygame.time.Clock()      # object to track time
    bg_image = Star_bg("star.gif")      # insert the star.gif image for the background

    #coordinate of moving background
    x = 0                   # set the coordinate x start from 0
    y = 0                   # set the coordinate y start from 0
    x1 = bg_image.width     # x1 is equal to background width
    y1 = 0                  # y1 is equal to 0

    pygame.init()           # initialize pygame

    #creating a jet :
    jet1 = Jet(screen)          # make an object called jet1 from Jet class
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()

    Fps = 40                                    # set fps to 40
    asteroid_timer = pygame.time.get_ticks()    # get time for the asteroid_timer
    while True:                                 # if the condition is True loop it
        theClock.tick(Fps)
        Fps += 0.01                             # game phase goes faster after every frame

        """background move"""
        x -= 5                          # for moving the background backward
        x1 -= 5                         # for moving the background backward
        bg_image.draw(screen, x, y)     # show the background image according to  x,y coordinate
        bg_image.draw(screen, x1, y1)   # show the background image according to  x1,y1 coordinate
        if x < -bg_image.width:         # if x is less than minus background width, run the code
            x = 0
        if x1 < 0:                      # if x1 is less than 0, run the code
            x1 = bg_image.width

        # create score board
        font = pygame.font.SysFont("Times New Romans", 36)                  # set the font and the font size
        score_board = font.render("score:"+str(scores), True, (255, 255, 255)) # update the score , set color to white
        # update refered to the word's method
        screen.blit(score_board,(10,550))       # draw the socre board in game
        Jet_sprites.draw(screen)                # draw the jet in game
        bullets.draw(screen)                    # draw the bullet
        asteroid_group.draw(screen)             # draw the asteroid
        display.update()                        # update jet and screen view
        event.get()                             # get the event
        """moving the jet according to key pressed"""

        key = pygame.key.get_pressed()          # make a variable for pygame.key.get_pressed
        if key[K_LEFT] and jet1.rect.x > 0:     # if key left and jet1.rect x is greater than 0, run the code
            jet1.moveleft()                     # move the jet to left

        if key[K_RIGHT] and jet1.rect.x <= 700: # if key right and jet1.rect.x is less than 700, run the code
            jet1.moveright()                    # move the jet to right

        if key[K_DOWN] and jet1.rect.y <= 500:  # if key down and jet1.rect.y is less than 500, run the code
            jet1.movedown()                     # move it down

        if key[K_UP] and jet1.rect.y > 0:       # if key up and jet1.rect.y is greater than 0, run the code
            jet1.moveup()                       # move it up

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42) # to set the bullet position based on jet position
            bullets.add(bullet)                                     # add bullets
            pygame.mixer.music.load("LaserBlast.wav")               # set the sound when you shoot the bullet
            pygame.mixer.music.play()                               # play the sound when you shoot the bullet

        if key[K_ESCAPE]:                       # if space is pressed, run the code
            menu.menu_screen(Button, run_game)  # end the game

        if key[K_p]:                            # if p is pressedn, run the code
            menu.pause_menu(Button,run_game)    # paused the game

        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            # spawn the asteroid randomly
            asteroid_group.add(asteroid)            # add asteroid
            asteroid_timer = pygame.time.get_ticks()# set time to spawn the asteroid

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:         # if asteroid.rect.right is equal or less than 0, run the code
                asteroid_group.remove(asteroid)  # remove after screen
            if groupcollide(Jet_sprites, asteroid_group,dokilla=True,dokillb=True): # condition check
                menu.lose_menu(Button, run_game, scores)

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left > 800:           # if bullet.rect.left is greater than 800
                bullets.remove(bullet)           # remove the bullet from the screen
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True): # if the bullet hit the asteroid
                scores += 100                                                  # add score 100


menu.menu_screen(Button,run_game)   # call the function

#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------

"""Acknowledgement:
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""