import random
import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (100, 22, 44)

screen_width = 900
screen_height = 600

def plot_snake(gameWindow, color, snake_list, snake_size):
    for snake_part in snake_list:
        pygame.draw.rect(gameWindow, color, [snake_part[0], snake_part[1], snake_size, snake_size])

def text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def gameloop():
    # Your game loop logic goes here
    pass

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
init_velocity = 10
fps = 15

score = 0
snake_size = 20

food_x = random.uniform(20, screen_width / 1.5)
food_y = random.uniform(20, screen_height / 1.5)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

snake_list = []
snake_length = 1

def show_score(score):
    score_text = font.render("Score: " + str(score), True, red)
    gameWindow.blit(score_text, [5, 5])

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = 10
                    velocity_y = 0
                elif event.key == pygame.K_LEFT:
                    velocity_x = -10
                    velocity_y = 0
                elif event.key == pygame.K_UP:
                    velocity_y = -10
                    velocity_x = 0
                elif event.key == pygame.K_DOWN:
                    velocity_y = 10
                    velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
        score += 1
        print("Score:", score)
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)
        snake_length += 5

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    head = [snake_x, snake_y]
    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    if snake_y < 0 or snake_x < 0 or snake_x > screen_width or snake_y > screen_height:
        game_over = True
        print("Game Over")

    if game_over:
        gameWindow.fill(white)
        text_screen("Game Over", red, screen_width / 4, screen_height / 4)
        text_screen("Press ENTER to play again", black, screen_width / 4, screen_height / 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    snake_x = 45
                    snake_y = 55
                    velocity_x = 0
                    velocity_y = 0
                    game_over = False
                    score = 0
                    snake_list.clear()

    plot_snake(gameWindow, black, snake_list, snake_size)

    show_score(score)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
