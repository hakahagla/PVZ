import pygame
import animation

pygame.init()
width,height = (1030,680)

lawnmower = pygame.image.load('Screen/car.png')
slot = pygame.image.load('Screen/ChooserBackground.png')
shovel = pygame.image.load('Screen/Shovel.jpg')
bg = pygame.image.load("Background/mainmenu.png")
bg = pygame.transform.scale(bg, (width, height))
bg2 = pygame.image.load("Background/Background_0.jpg")
bg2 = pygame.transform.scale(bg2, (1430, height))

font = pygame.font.Font("SERIO___.TTF",18)

clock =  pygame.time.Clock()

class window():
    global bg
    global bg2
    global width,height
    

    def __init__(self):
        self.clicked == False
        self.width,self.height = (1030,680)
        self.background = bg
        self.background2 = bg2
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.background,(0,0))

    def clicked(self):
        global ingame
        #print(pygame.mouse.get_pos())
        x,y=pygame.mouse.get_pos()
        if x >= 515 and x <= 890 and  y >= 90 and y <= 235: #Ingame button is clicked
            self.screen.blit(self.background2,(0,0))
            ingame = True
            global currgame
            currgame = game()
            
class card_peashooter():
        
    def __init__(self):
        self.pcard = pygame.image.load('cards/card_peashooter.png')
        self.card = self.pcard
        menu.screen.blit(self.card,(100,10))

    def clicked(self):  
        pass
            
class game():
    global lawnmower
    global slot
    global shovel
    global bg2
    global created
    
    def __init__(self):
        self.lawnmower = lawnmower
        self.slot = slot
        self.shovel = shovel
        self.background = bg2

        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        menu.screen.blit(self.lawnmower,(190, 120))
        menu.screen.blit(self.lawnmower,(190, 220))
        menu.screen.blit(self.lawnmower,(190, 320))
        menu.screen.blit(self.lawnmower,(180, 420))
        menu.screen.blit(self.lawnmower,(170, 550))

        test_card = card_peashooter()

        
        created.append('obj1')
        created.append('450,450')
        print(created)

    def refresh(self):
        global created
        
        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        menu.screen.blit(self.lawnmower,(190, 120))
        menu.screen.blit(self.lawnmower,(190, 220))
        menu.screen.blit(self.lawnmower,(190, 320))
        menu.screen.blit(self.lawnmower,(180, 420))
        menu.screen.blit(self.lawnmower,(170, 550))

        test_card = card_peashooter()
        obj1 = animation.peashooter(peashooter_anim)
        menu.screen.blit(obj1,(450,450))
        if len(created) == 4:
            obj2 = animation.peashooter2(peashooter_anim)
            menu.screen.blit(obj2,(self.x,self.y))

    def clicked(self):
        global drag
        peashooter = (pygame.image.load("plants/Peashooter/Peashooter_0.png").convert_alpha())
        x,y=pygame.mouse.get_pos()
        if x >= 100 and x <= 160 and y >= 10 and y <= 95:
            drag = True
        if drag == True:
            game.drag(self,peashooter)
            
        #Need to check sunlight count and deduct      

    def drag(self,obj):
        global drag
        if drag == True:
            x,y=pygame.mouse.get_pos()
            menu.screen.blit(obj,(x-30,y-25))
            pygame.display.flip()

    def place(self):
        global drag
        
        self.x,self.y=pygame.mouse.get_pos()
        self.x-=30
        self.y-=25
        obj2 = animation.peashooter(peashooter_anim)
        menu.screen.blit(obj2,(self.x,self.y))
        created.append('obj2')
        created.append(str(self.x)+','+str(self.y))
        print(created)



menu = window()

peashooter_anim = [(pygame.image.load("plants/Peashooter/Peashooter_0.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_1.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_2.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_3.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_4.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_5.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_6.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_7.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_8.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_9.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_10.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_11.png").convert_alpha()),
(pygame.image.load("plants/Peashooter/Peashooter_12.png").convert_alpha())]



running = True
ingame = False
drag = False
created = []

while running:
  if ingame == True:
      clock.tick(10)
      currgame.refresh()
  if drag == True:
      currgame.clicked()
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if ingame == False:
                menu.clicked()
            else:
                ingame = True
                if drag == False:
                    currgame.clicked()
                elif drag == True:
                    currgame.place()
                    drag = False
                    
        
        
            
            


            
            




