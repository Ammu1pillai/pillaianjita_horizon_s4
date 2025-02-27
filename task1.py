import pygame
import random
import math
pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("First game")
font = pygame.font.Font(None, 36)

circles = []
run = True
holding = False
start = 0
rand = (0,0,0)
curr = 0

class Circle:
    def __init__(self, x, y, rand):
        self.x = x
        self.y = y
        self.rand = rand
        self.radius = 10

    def inflate(self,duration):
        self.radius = 10 + duration/50

    def draw(self, surface):
        pygame.draw.circle(surface, self.rand, (self.x, self.y), int(self.radius))

def path_len(circles):
    length = 0
    if len(circles) > 1:
        for i in range(len(circles)-1):
            x1,y1 = circles[i].x,circles[i].y
            x2,y2 = circles[i+1].x,circles[i+1].y
            dist = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
            length+=dist
    return length


while run:
    pygame.time.delay(10)
    win.fill((255, 255, 255))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            holding = True
            start = pygame.time.get_ticks()
            x,y = pygame.mouse.get_pos()
            rand = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            curr = Circle(x,y,rand)
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                holding = False
                if curr:
                    duration = (pygame.time.get_ticks() - start)
                    curr.inflate(duration)
                    circles.append(curr)
                    curr = 0
                start = 0

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circles.clear()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                circles.remove(circles[len(circles)-1])
                
                
                    
    for circle in circles:
        circle.draw(win)

    if len(circles) > 1:
        for i in range(len(circles)-1):
            pygame.draw.line(win,(0,0,0), (circles[i].x, circles[i].y), (circles[i+1].x,circles[i+1].y),2)

    leng = path_len(circles)
    text = font.render(f"Path Length: {int(leng)} pixels", True, (0,0,0))
    win.blit(text,(20,20))
    
    if holding and curr:
        duration = (pygame.time.get_ticks()-start)
        curr.inflate(duration)
        curr.draw(win)
        
            
    pygame.display.update()
    
pygame.quit() 
