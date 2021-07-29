"""
this simple game consists of 1 player object, three enemy objects, and 1 prize object
if the player object collides with an enemy object, the game is lost
if the player object collides with the prize object, the game is won
"""

#import game library
import pygame
#import random library
import random

#initialize pygame modules to start the game
pygame.init()

#create a screen by setting width and height variables and assigning
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))

#create objects with images in folder
player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

#get width and height of images for boundary detection
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

#store object positons as variables
player_x_position = 100
player_y_position = 50

#enemy and prize objects start at random off-screen positions
enemy1_x_position =  screen_width
enemy1_y_position =  random.randint(0, screen_height - enemy1_height)

enemy2_x_position =  screen_width
enemy2_y_position =  random.randint(0, screen_height - enemy2_height)

enemy3_x_position =  screen_width
enemy3_y_position =  random.randint(0, screen_height - enemy3_height)

prize_x_position =  screen_width
prize_y_position =  random.randint(0, screen_height - prize_height)

#set arrow keys to false
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#begin the game loop to run the game logic until the game is won/lost
#screen is refreshed to apply changes continually
while 1:

    #clear screen
    screen.fill(0)
    #draw objects to specified point on screen
    screen.blit(player, (player_x_position, player_y_position))
    screen.blit(enemy1, (enemy1_x_position, enemy1_y_position))
    screen.blit(enemy2, (enemy2_x_position, enemy2_y_position))
    screen.blit(enemy3, (enemy3_x_position, enemy3_y_position))
    screen.blit(prize, (prize_x_position, prize_y_position))

    #update screen
    pygame.display.flip()

    #loop through game with for loop
    for event in pygame.event.get():

        #check if user quits the program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #check if user presses key down
        if event.type == pygame.KEYDOWN:

            #check which key is pressed and sets that value to true
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT: 
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight= True

        #check if key is up /not pressed
        if event.type == pygame.KEYUP:

            #check which key is released and sets the value to false
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT: 
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight= False

    #moving player up and down on the y axis(0,0)
    if keyUp == True:
        #player can't move above the window
        if player_y_position > 0 : 
            player_y_position -= 1
            
    if keyDown == True:
        #player can't move below the window
        if player_y_position < screen_height - player_height:
            player_y_position += 1

    #moving player left and right on the x axis(0,0)
    if keyLeft == True:
        #player can't move left of the window
        if player_x_position > 0 : 
            player_x_position -= 1    

    if keyRight == True:
        #player can't move right of the window
        if player_x_position < screen_width - player_width:
            player_x_position += 1

    #check collison with enemy and prize
    #by creating bounding boxes to test collision
    playerBox = pygame.Rect(player.get_rect())
    #update the playerBox position to the player's positon
    playerBox.top = player_y_position
    playerBox.left = player_x_position

    #bounding box for enemy
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1_y_position
    enemy1Box.left = enemy1_x_position

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2_y_position
    enemy2Box.left = enemy2_x_position

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3_y_position
    enemy3Box.left = enemy3_x_position

    #bounding box for prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_y_position
    prizeBox.left = prize_x_position

    #test collison of boxes with if statement
    if playerBox.colliderect(enemy1Box):

        #display losing status
        print("You lose!")

        #quit game and exit window
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy2Box):

        #display losing status
        print("You lose!")

        #quit game and exit window
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy3Box):

        #display losing status
        print("You lose!")

        #quit game and exit window
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(prizeBox):

        #display losing status
        print("You win!")

        #quit game and exit window
        pygame.quit()
        exit(0)

    #make enemy approach the player at speed
    enemy1_x_position -= 0.20
    enemy2_x_position -= 0.05
    enemy3_x_position -= 0.15
    
    #make prize approach the player at speed
    prize_x_position -= 0.10
