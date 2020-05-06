import pygame
import sys

pygame.init()
pygame.display.set_caption("Arcanoid")

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# paddle related variables
paddleWidth = 119
paddleHeight = 20
paddleX = width / 2 - paddleWidth / 2
paddle = pygame.image.load('paddle_wide_pulsate_3.png')

# ball related variables
ballWidth = 10
ballHeight = 10
ballX = width / 2 - ballWidth / 2
ballY = height / 2 - ballHeight / 2
coordinates = pygame.math.Vector2((ballX, ballY))
d = pygame.math.Vector2((2, 2))
ball = pygame.image.load('ball.png')

# bricks related variables
brickWidth = 43
brickHeight = 21
rows = 12
columns = 15
offSet = 0
brick = pygame.image.load('brick_green.png')

bricks = [[] for i in range(rows)]
print(bricks)
for i in range(rows):
    for j in range(columns):
        bricks[i].append([j * (brickWidth + offSet) + 60, 30 + i * (brickHeight + offSet), False])

# background
background = pygame.image.load('background.jpg')
counter = 1
crashed = False
while not crashed:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
            sys.exit(0)

    def drawPaddle():
        paddleX = pygame.mouse.get_pos()[0] - paddleWidth/2
        if paddleX > width - paddleWidth:
            paddleX = width - paddleWidth
        if paddleX < 0:
            paddleX = 0
        screen.blit(paddle, (paddleX, height - 70))
        if coordinates.x >= paddleX and coordinates.x <= paddleX + paddleWidth and coordinates.y >= height - ballHeight - 70 and coordinates.y <= height - 70 + paddleHeight:
            d.y *= -1


    def drawBall():
        screen.blit(ball, coordinates)
        coordinates.x += d.x
        coordinates.y += d.y
    if coordinates.x > width - ballWidth or coordinates.x < 0:
        d.x *= -1
    if coordinates.y > height - ballHeight or coordinates.y < 0:
        d.y *= -1

    def drawBricks():
        for i in range(rows):
            for j in range(columns):
                if not bricks[i][j][2]:
                    screen.blit(brick, (bricks[i][j][0], bricks[i][j][1]))
        for i in range(rows):
            for j in range(columns):
                bx = bricks[i][j][0]
                by = bricks[i][j][1]
                destroyed = bricks[i][j][2]
                if not destroyed:
                    if coordinates.x >= bx and coordinates.x <= bx + brickWidth and coordinates.y <= by + brickHeight:
                        bricks[i][j][2] = True
                        d.x *= -1
                        d.y *= -1
    if coordinates.y >= height - 10:
        crashed = True

    drawBall()
    drawBricks()
    drawPaddle()
    counter += 1
    pygame.display.flip()
