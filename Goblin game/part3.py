import pygame #import the module
pygame.init()

win = pygame.display.set_mode((500, 480)) # create a window
pygame.display.set_caption('Sample Game') # give window a caption

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('R1.png')

clock = pygame.time.Clock()

#set the coordinates of the sprite and height, width and velocity
x = 50
y = 400
width = 64
height = 64
vel = 10
run = True
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():

    global walkCount
    win.blit(bg, (0,0))
    if walkCount+1 >= 27:# this line draws our main sprite
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount+=1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount+=1

    else:
        win.blit(char, (x,y))

    pygame.display.update()# this line keeps updating the window constantly

# this is the main loop of the program
while run:
    clock.tick(27) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # this line says whem the user presses the cross button the program should exit
            run = False

    keys = pygame.key.get_pressed() 

    # these if statements see what should be done when the user does an event(click a button)
    if keys[pygame.K_LEFT] and x>=vel:
        x-=vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x<500-width:
        x+=vel
        left = False
        right = True

    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:

        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0

    else :

        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1 

        else :
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()