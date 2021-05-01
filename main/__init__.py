import pygame
import random
import math
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((1400, 700))
#screen = pygame.display.toggle_fullscreen


pygame.display.set_caption("Bat Unleashed")
icon = pygame.image.load('baticon.png')
pygame.display.set_icon(icon)


bg3 = pygame.image.load("bg7.jpg")
pygame.mixer.music.load('background.wav')
#pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

playerImg = pygame.image.load('bat3.png')
playerX = 345
playerY = 550
playerX_change = 0

scorevalue=0
font=pygame.font.Font('freesansbold.ttf', 40)
textX=600
textY=10

font1=pygame.font.Font('freesansbold.ttf', 80)
def show(x,y):
    score=font.render("Score :" +str(scorevalue),True,(255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    game = font1.render("GAME OVER!!", True, (255,0,0))
    screen.blit(game, (400, 300))


enemyImg =[]
enemyX=[]
enemyY =[]
enemyX_change=[]
enemyY_change=[]
noofenemies=9
for i in range(noofenemies):
    enemyImg.append(pygame.image.load('mine22.png'))
    enemyImg.append(pygame.image.load('mine222.png'))
    enemyImg.append(pygame.image.load('mine2222.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(10)
    enemyY_change.append(60)

def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))
def iscollision(enemyX, enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 40:
        return True
    else:
        return False


bulletImg = pygame.image.load('bullet2.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 60
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 80, y + 80))


running = True
while running:
   # bg3 = pygame.image.load("bg7.jpg")
    screen.blit(bg3,(0,0))
    #screen.fill((255, 0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -30
            if event.key == pygame.K_RIGHT:
                playerX_change = 30
            if event.key == pygame.K_SPACE:
                if bullet_state =="ready":
                    sound=mixer.Sound('laser.wav')
                    sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 5:
        playerX = 5
    elif playerX >= 1150:
        playerX = 1150
    #playerY = 480

    for i in range(noofenemies):
        if enemyY[i]>435:
            for j in range(noofenemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 5:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 15
        elif enemyX[i] >= 1150:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -15
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            sound1 = mixer.Sound('explosion.wav')
            sound1.play()
            bulletY = 480
            bullet_state = 'ready'
            scorevalue += 1

            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #playerY = 480
    # Bullet Movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state =="fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    # enemy()
    player(playerX, playerY)
    show(textX,textY)
    pygame.display.update()
