import pygame
import sys
import random
import time

# Based off of this https://www.youtube.com/watch?v=Qf3-aDXG8q4

# Add pause

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Final 2')

background_color = pygame.Color('black')

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


class Image:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def load_image(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Entire game, variables mode and difficulty determine if the game will be single or multiplayer and difficulty will
# determine the ai difficulty (increases the ai movement speed)
def start_game(mode, difficulty):
    # Variables
    global ballSpeed_x, ballSpeed_y, player1_score, player2_score
    ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    player1 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
    player2 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

    player1_color = pygame.Color('blue')
    player2_color = pygame.Color('red')
    background_color = pygame.Color('black')
    light_grey = (200, 200, 200)

    ballSpeed_x = 7 * random.choice((-1, 1))
    ballSpeed_y = 7 * random.choice((-1, 1))

    player1_speed = 0
    player2_speed = 0

    player1_score = 0
    player2_score = 0
    game_font = pygame.font.Font("freesansbold.ttf", 48)

    # Handles the balls physics and collision
    def ball_animation():
        global ballSpeed_x, ballSpeed_y, player1_score, player2_score
        if player1_score < 5 or player2_score < 5:
            ball.x += ballSpeed_x
            ball.y += ballSpeed_y
            if ball.top <= 0 or ball.bottom >= screen_height:
                ballSpeed_y *= -1
            if ball.left <= 0:
                player2_score += 1
                ball_restart()
            if ball.right >= screen_width:
                player1_score += 1
                ball_restart()
            if ball.colliderect(player1) or ball.colliderect(player2):
                ballSpeed_x *= -1
        if player1_score >= 5 or player2_score >= 5:
            ball.x = screen_width / 2
            ball.y = screen_height / 2

    # Player 1 (blue) movement
    def player1_animation():
        player1.y += player1_speed
        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= screen_height:
            player1.bottom = screen_height

    # Player 2 (red) movement
    def player2_animation():
        player2.y += player2_speed
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_height:
            player2.bottom = screen_height

    # Player 2 (ai) movement and following the ball
    def player2_bot(aiSpeed):
        if player2.top < ball.y:
            player2.top += aiSpeed
        if player2.top > ball.y:
            player2.top -= aiSpeed
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_height:
            player2.bottom = screen_height

    # Respawns the ball back in the center and gives it a random x and y speed
    def ball_restart():
        global ballSpeed_x, ballSpeed_y
        ball.center = (screen_width / 2, screen_height / 2)
        ballSpeed_y *= random.choice((-1, 1))
        ballSpeed_x *= random.choice((-1, 1))


    # While loop continuously runs and refreshes game, draws objects, text, images/buttons, and handles input
    while True:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if mode == 1:
                # PLAYER 1 INPUT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player1_speed += 7
                    if event.key == pygame.K_w:
                        player1_speed -= 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        player1_speed -= 7
                    if event.key == pygame.K_w:
                        player1_speed += 7
            if mode == 2:
                # PLAYER 1 AND PLAYER 2 INPUT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player1_speed += 7
                    if event.key == pygame.K_w:
                        player1_speed -= 7
                    if event.key == pygame.K_DOWN:
                        player2_speed += 7
                    if event.key == pygame.K_UP:
                        player2_speed -= 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        player1_speed -= 7
                    if event.key == pygame.K_w:
                        player1_speed += 7
                    if event.key == pygame.K_DOWN:
                        player2_speed -= 7
                    if event.key == pygame.K_UP:
                        player2_speed += 7
        # Determine winner/loser and put up respective image
        if mode == 1:
            if player1_score >= 5:
                solo_win.load_image()
            if player2_score >= 5:
                solo_lose.load_image()
        if mode == 2:
            if player1_score >= 5:
                p1_win.load_image()
            if player2_score >= 5:
                p2_win.load_image()

        ball_animation()
        player1_animation()

        # Determine if single or multiplayer
        if mode == 1:
            if difficulty == 1:
                player2_bot(5)
            if difficulty == 2:
                player2_bot(10)
            if difficulty == 3:
                player2_bot(12)
        # Determine AI difficulty
        if mode == 2:
            player2_animation()

        # Create player 1 and player 2, ball, and the center line
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 40), (screen_width / 2, screen_height - 40))
        pygame.draw.rect(screen, player1_color, player1)
        pygame.draw.rect(screen, player2_color, player2)
        # Creates main menu button to return back home
        if mainMenu_button.draw():
            main_menu()
        pygame.draw.ellipse(screen, light_grey, ball)

        # Display player scores
        player1_text = game_font.render(f"{player1_score}", False, player1_color)
        screen.blit(player1_text, (600, 470))
        player2_text = game_font.render(f"{player2_score}", False, player2_color)
        screen.blit(player2_text, (660, 470))

        clock.tick(60)
        pygame.display.flip()


# Creates the difficulty select screen
def difficulty_select():
    while True:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        difficultyTitle.load_image()
        if mainMenu_button.draw():
            main_menu()
        if easy.draw():
            start_game(1, 1)
        if normal.draw():
            start_game(1, 2)
        if hard.draw():
            start_game(1, 3)

        pygame.display.flip()
        clock.tick(60)

    # Creates main menu


def main_menu():
    while True:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pongTitle.load_image()
        if singleplayer_button.draw():
            difficulty_select()

        if multiplayer_button.draw():
            start_game(2, 0)

        if quit_button.draw():
            sys.exit()
        # Refreshes screen, refresh rate to 60, for consi stency in movement Higher fps causes everything to move faster
        pygame.display.flip()
        clock.tick(60)


# get image
Pong_Title = pygame.image.load("Images/PONG_Title.png").convert_alpha()
Pong_Quit = pygame.image.load("Images/PONG_Quit.png").convert_alpha()
Pong_Win = pygame.image.load("Images/PONG_Win.png").convert_alpha()
Pong_Lose = pygame.image.load("Images/PONG_Lose.png").convert_alpha()
Pong_P1Win = pygame.image.load("Images/PONG_P1Win.png").convert_alpha()
Pong_P2Win = pygame.image.load("Images/PONG_P2Win.png").convert_alpha()
Pong_Single = pygame.image.load('Images/PONG_Singleplayer.png').convert_alpha()
Pong_Multi = pygame.image.load("Images/PONG_Multiplayer.png").convert_alpha()
Pong_Difficulty = pygame.image.load("Images/PONG_Difficulty.png").convert_alpha()
Pong_Easy = pygame.image.load("Images/PONG_Easy.png").convert_alpha()
Pong_Normal = pygame.image.load("Images/PONG_Normal.png").convert_alpha()
Pong_Hard = pygame.image.load("Images/PONG_Hard.png").convert_alpha()
Pong_MainMenu = pygame.image.load("Images/PONG_MainMenu.png").convert_alpha()
Pong_Paused = pygame.image.load("Images/PONG_Paused.png").convert_alpha()

# Create the images and where they will appear on the screen
pongTitle = Image(screen_width / 2 - 150, 100, Pong_Title, 4)
solo_win = Image(screen_width / 4 - 75, 50, Pong_Win, 5)
solo_lose = Image(screen_width / 4 - 75, 50, Pong_Lose, 5)
p1_win = Image(screen_width / 4 - 200, 50, Pong_P1Win, 5)
p2_win = Image(3 * screen_width / 4 - 150, 50, Pong_P2Win, 5)
difficultyTitle = Image(screen_width / 2 - 150, 50, Pong_Difficulty, 5)
pong_paused = Image(screen_width / 2 - 40, 150, Pong_Paused, 5)

# Create the buttons and where they will appear on the screen
singleplayer_button = Button(screen_width / 4 - 50, 350, Pong_Single, 5)
multiplayer_button = Button(screen_width / 4 - 50, 450, Pong_Multi, 5)
quit_button = Button(screen_width / 4 - 50, 550, Pong_Quit, 5)
mainMenu_button = Button(screen_width / 2 - 45, screen_height - 100, Pong_MainMenu, 3)
easy = Button(1 * screen_width / 5, 250, Pong_Easy, 5)
normal = Button(2 * screen_width / 5, 250, Pong_Normal, 5)
hard = Button(screen_width / 2 + 200, 250, Pong_Hard, 5)

main_menu()
