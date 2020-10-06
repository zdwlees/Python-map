import pygame, ast, math, os, sys

os.chdir(os.path.dirname(sys.argv[0]))
pygame.init()
pygame.key.set_repeat(0)

f = open("map.txt", "r")
map = ast.literal_eval(f.readline())
f.close()

disp_width = 850
disp_height = 650
pix = 50
size = 50
maxX = size - disp_width / pix
maxY = size - disp_height / pix
centreX = math.floor(disp_width / pix / 2)
centreY = math.floor(disp_height / pix / 2)



disp = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Moveable Map')

white = (255,255,255)

clock = pygame.time.Clock()

wall = pygame.image.load('wall.png')
room = pygame.image.load('room.png')
playImg = pygame.image.load('player.png')
spawn = pygame.image.load('spawn.png')
tiles = [room,wall,spawn]

def player(x,y):
    disp.blit(playImg, (x,y))

def game_loop():
    x = list(map.keys())[list(map.values()).index(2)][0]
    y = list(map.keys())[list(map.values()).index(2)][1]
    
    if x < centreX:
        mapX = 0
        plaX = x
    elif x > maxX - centreX:
        mapX = maxX
        plaX = x - maxX
    else:
        mapX = x - centreX
        plaX = centreX

    if y < centreY:
        mapY = 0
        plaY = y
    elif y > maxY - centreY:
        mapY = maxY
        plaY = y - maxY
    else:
        mapY = y - centreY
        plaY = centreY

    
    running = True
    while running:
        totX = mapX + plaX
        totY = mapY + plaY
        move1 = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and move1:
                    if (mapY == 0 or plaY != centreY) and map.get((totX,totY-1)) != 1:
                        plaY -= 1
                    elif mapY>0 and map.get((totX,totY-1)) != 1 and plaY == centreY:
                        mapY -= 1
                    move1 = False
                    
                    
                if event.key == pygame.K_s and move1:
                    if (mapY == maxY or plaY != centreY) and map.get((totX,totY+1)) != 1:
                        plaY += 1
                    elif mapY<maxY and map.get((totX,totY+1)) != 1 and plaY == centreY:
                        mapY += 1
                    move1 = False
                    
                    
                if event.key == pygame.K_a and move1:
                    if (mapX == 0 or plaX != centreX) and map.get((totX-1,totY)) != 1:
                        plaX -= 1
                    elif mapX>0 and map.get((totX-1,totY)) != 1 and plaX == centreX:
                        mapX -= 1
                    move1 = False
                    
                if event.key == pygame.K_d and move1:
                    if (mapX == maxX or plaX != centreX) and map.get((totX+1,totY)) !=1:
                        plaX += 1
                    elif mapX<maxX and map.get((totX+1,totY)) != 1 and plaX == centreX:
                        mapX += 1
                    move1 = False
                    



        disp.fill(white)
        
        for x in range (0,size):
            for y in range (0,size):
                if (x,y) in map:
                    disp.blit(tiles[map[x,y]], ((x-mapX)*pix,(y-mapY)*pix))
                    
        player(plaX*pix,plaY*pix)
        #print(str(mapX) + ' ' + str(mapY) + ' ' + str(plaX) + ' ' + str(plaY))
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
     
