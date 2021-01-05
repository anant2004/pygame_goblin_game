import pygame #import the module
pygame.init()

win = pygame.display.set_mode((500, 500)) # create a window
pygame.display.set_caption('Hello') # give window a caption

#set the coordinates of the sprite and height, width and velocity
x = 50
y = 50
width = 20
height = 20
vel = 10
run = True

# this is the main loop of the program
while run:
    pygame.time.delay(10) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # this line says whem the user presses the cross button the program should exit
            run = False

    keys = pygame.key.get_pressed() 

    # these if statements see what should be done when the user does an event(click a button)
    if keys[pygame.K_LEFT]:
        x-=vel

    if keys[pygame.K_RIGHT]:
        x+=vel

    if keys[pygame.K_UP]:
        y-=vel

    if keys[pygame.K_DOWN]:
        y+= vel

    win.fill((0,0,0))

    pygame.draw.rect(win, (255,0,0), (x,y,width,height))# this line draws our main sprite
    pygame.display.update()# this line keeps updating the window constantly

pygame.quit()