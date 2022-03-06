import pygame
import time
import random

# Init Pygame
pygame.init()

# Define Colors
white = (255, 255, 255)
black = (0, 160, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
green = (0, 0, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python")

clock = pygame.time.Clock()



snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)



def print_score(score):

    text_2 = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text_2, [0,0])



def draw_snake(snake_size, snake_pixels):

    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_display.fill(green)

    game_over = False
    game_close = False

    x = width /  2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0


    while not game_over:

        while game_close:

            game_display.fill(green)
            game_over_message_1 = message_font.render("GAME OVER", True, red)
            game_over_message_2 = message_font.render("press q to quit", True, red)
            game_over_message_3 = message_font.render("press e to continue", True, red)
            game_display.blit(game_over_message_1, [width / 3, height / 3])
            game_display.blit(game_over_message_2, [width / 2, height / 2])
            game_display.blit(game_over_message_3, [width / 8, height / 2])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                 if event.key == pygame.K_a:
                     x_speed = -snake_size
                     y_speed = 0
                 if event.key == pygame.K_d:
                      x_speed = snake_size
                      y_speed = 0
                 if event.key == pygame.K_w:
                     x_speed = 0
                     y_speed = -snake_size
                 if event.key == pygame.K_s:
                     x_speed = 0
                     y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
             game_close = True
        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
             if pixel == [x, y]:
                 game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()