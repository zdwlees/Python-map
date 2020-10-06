import ast, os, sys

os.chdir(os.path.dirname(sys.argv[0]))

print("If you want to create a new map type n, if you want to load one type the filename.")
answer = input()
if answer == "n":
    map = {}
    for x in range(0,50):
        for y in range(0,50):
                map[x,y] = 0
else:
    f = open(str(answer) + ".txt", "r")
    map = ast.literal_eval(f.read())
    f.close()





import pygame
import math
pygame.init()
dis = pygame.display.set_mode((500,500))
pygame.display.set_caption('Map Creator')

white = (255,255,255)

clock = pygame.time.Clock()

wall = pygame.image.load('swall.png')
room = pygame.image.load('sroom.png')
spawn = pygame.image.load('sspawn.png')

def game_loop():
    global finish
    tileType = 1
    finish = False
    running = True
    while running:
        mocl = pygame.mouse.get_pressed()
        mopo = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finish = True
                    running = False
                for i in range(0,10):
                    if event.key == getattr(pygame, "K_"+str(i)):
                        tileType = i
                
                

            if mocl[0] == 1:
                map[math.floor(mopo[0]/10),math.floor(mopo[1]/10)] = tileType
            

        



        dis.fill(white)




        for x in range(0,50):
            for y in range(0,50):
                if (x,y) in map and map[x,y] == 1:
                    dis.blit(wall, (x*10, y*10))
                if (x,y) in map and map[x,y] == 0:
                    dis.blit(room, (x*10, y*10))
                if (x,y) in map and map[x,y] == 2:
                    dis.blit(spawn, (x*10, y*10))

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
if finish:
    print("What name to save?")
    f = open(input() + ".txt", "w")
    f.write(str(map))
    f.close()



