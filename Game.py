#Plant VS Zombies

import pygame

#Initalise Modules
pygame.init()
clock =  pygame.time.Clock()
width,height = (1100,680)#Size of window

#Import assests
lawnmower = pygame.image.load('Screen/car.png')
slot = pygame.image.load('Screen/ChooserBackground.png')
shovel = pygame.image.load('Screen/Shovel.jpg')
bg = pygame.image.load("Background/mainmenu.png")
bg = pygame.transform.scale(bg, (width, height))
bg2 = pygame.image.load("Background/Background_0.jpg")
bg2 = pygame.transform.scale(bg2, (1430, height))

#=================================================================================================
#Classes

class window():
    global bg
    global bg2
    global width,height
    

    def __init__(self):
        self.clicked == False
        self.width,self.height = (1100,680)
        self.background = bg
        self.background2 = bg2
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.background,(0,0))

    def clicked(self):
        global ingame
        x,y=pygame.mouse.get_pos()
        if x >= 515 and x <= 890 and  y >= 90 and y <= 235: #Ingame button is clicked
            self.screen.blit(self.background2,(0,0))
            ingame = True
            global currgame
            currgame = game()

#=================================================================================================
            
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
    global created_plant
    
    def __init__(self):
        self.lawnmower = lawnmower
        self.slot = slot
        self.shovel = shovel
        self.background = bg2
        self.c_coord = [[300,150],[380,150],[460,150],[540,150],[620,150],[700,150],[780,150],[870,150],[960,150],
                                [300,260],[380,260],[460,260],[540,260],[620,260],[700,260],[780,260],[870,260],[960,260],
                                [300,370],[380,370],[460,370],[540,370],[620,370],[700,370],[780,370],[870,370],[960,370],
                                [300,480],[380,480],[460,480],[540,480],[620,480],[700,480],[780,480],[870,480],[960,480],
                                [300,590],[380,590],[460,590],[540,590],[620,590],[700,590],[780,590],[870,590],[960,590]]

        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        menu.screen.blit(self.lawnmower,(190, 120))
        menu.screen.blit(self.lawnmower,(190, 220))
        menu.screen.blit(self.lawnmower,(190, 320))
        menu.screen.blit(self.lawnmower,(180, 420))
        menu.screen.blit(self.lawnmower,(170, 550))

        test_card = card_peashooter()


    def refresh(self):
        
        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        menu.screen.blit(self.lawnmower,(190, 120))
        menu.screen.blit(self.lawnmower,(190, 220))
        menu.screen.blit(self.lawnmower,(190, 320))
        menu.screen.blit(self.lawnmower,(180, 420))
        menu.screen.blit(self.lawnmower,(170, 550))

        test_card = card_peashooter()
        
    
    def clicked(self):
        
        global drag
        self.targetxz = 0
        self.targetxy = 0
        peashooter = pygame.image.load("plants/Peashooter/Peashooter_0.png").convert_alpha()
        x,y=pygame.mouse.get_pos()
        if x >= 100 and x <= 160 and y >= 10 and y <= 95:
            drag = True
        if drag == True:
            game.drag(self,peashooter)
        else:
            print(x,y)
            self.distancez = 999
            created_zombie.append(len(created_zombie)+1)
            for i in range (0,len(self.c_coord)):
                self.diffxz = self.c_coord[i][0]-x
                self.diffyz = self.c_coord[i][1]-y
                self.temp = (self.diffxz**2+self.diffyz**2)**1/2
                if self.temp <= self.distancez:
                    self.targetxz,self.targetyz = self.c_coord[i][0],self.c_coord[i][1]
                    self.distance = self.temp
            globals()['objz'+str(created_zombie[len(created_zombie)-1])] = normalzombie(self.targetxz-30,self.targetyz-50,len(created_zombie)-1)
            
        #Need to check sunlight count and deduct      

    def drag(self,obj):
        global drag
        x,y=pygame.mouse.get_pos()
        menu.screen.blit(obj,(x-30,y-25))

    def place(self):
        global created_plant
        created_plant.append(str(len(created_plant)+1))
        self.x,self.y=pygame.mouse.get_pos()
        self.distance = 9999
        self.targetx,self.targety = 0.0,0.0
        for i in range (0,len(self.c_coord)):
            self.diffx = self.c_coord[i][0]-self.x
            self.diffy = self.c_coord[i][1]-self.y
            self.temp = (self.diffx**2+self.diffy**2)**1/2
            if self.temp <= self.distance:
                self.targetx,self.targety = self.c_coord[i][0],self.c_coord[i][1]
                self.distance = self.temp
        globals()['objp'+created_plant[len(created_plant)-1]] = peashooter(self.targetx-30,self.targety-25)

        #Validate there are only one plant on that tile

#=================================================================================================

class plant():
    
    def __init__(self,x,y):
        self.health = 0
        self.a_dmg = 0
        self.a_speed = 0
        self.framevalue = 0
        self.cd = 0
        self.cd_constant = 0
        self.x,self.y = x,y
        self.count = 0

    def animation(self,obj):
        global bullet_normal
        
        if self.framevalue >= len(obj):
            self.framevalue = 0
        self.currframe = obj[self.framevalue]
        if self.count == 16:
            self.framevalue += 1
            self.count = 0
        self.count += 1
        menu.screen.blit(self.currframe,(self.x,self.y))
        self.shoot(bullet_normal)

    def shoot(self,obj):
        global created_zombie
        global created_bullet

        self.cd -= 1
        if len(created_zombie) != 0 and self.cd == 0:
            for i in range(0,len(created_zombie)):
                x,y = globals()['objz'+str(created_zombie[i])].coord()
                if y + 50 == self.y + 25: #If there is a zombie in front
                    for j in range(0,999):
                        if j+1 not in created_bullet:
                            created_bullet.append(j+1)
                            globals()['objb'+str(j+1)] = normal_b(20,obj,self.x-10,self.y,j+1)
                            break
                    self.cd = self.cd_constant
        if self.cd < 0:
            self.cd = 50
         
                    
    def attack(self):
        pass

    def takedmg(self): 
        pass


class peashooter(plant):
    global bullet_normal
    
    def __init__(self,x,y):
        self.health = 100
        self.a_dmg = 20
        self.a_speed = 3
        self.cd = 50
        self.cd_constant = 240 * 1
        self.framevalue = 0
        self.x,self.y = x,y
        self.count = 0
    

#=================================================================================================

class zombie():

    def __init__(self,x,y,index):
        self.health = 100
        self.a_dmg = 20
        self.a_speed = 3
        self.m_speed = 0.05
        self.framevalue = 0
        self.x,self.y = x,y
        self.count = 0
        self.index = index
        self.dcount = 0

    def move(self):
        pass

    def coord(self):
        return self.x,self.y

    def animation(self,obj,anim_type):
        self.atype = anim_type
        if self.framevalue >= len(obj):
            self.framevalue = 0
        self.currframe = obj[self.framevalue]
        if self.count == 16:
            self.framevalue += 1
            self.count = 0
        self.count += 1
        if anim_type == 1:
            self.x -= self.m_speed
            menu.screen.blit(self.currframe,(self.x,self.y))
        elif anim_type == 2:
            menu.screen.blit(self.currframe,(self.x-40,self.y-10))


    def death(self,obj):
        global created_zombie
        if self.health <= 0:
            self.animation(zombie_anim_death,2)
            self.dcount += 1
        if self.dcount == 400 :
            print(created_zombie)
            print(self.index)
            created_zombie.remove(self.index+1)
            del globals()['objz'+str(self.index+1)]

class normalzombie(zombie):
    pass

#=================================================================================================

class bullet():
    def __init__(self,dmg,anim,x,y,index):
        self.dmg = dmg
        self.speed = 0.1
        self.x = x + 30
        self.y = y
        self.anim = anim
        self.index = index
        self.collided = False
        
    def move(self):
        self.collision()
        self.x += 1
        menu.screen.blit(self.anim,(self.x,self.y))
        

    def collision(self):
        global created_zombie
        global created_bullet
        
        for i in range(0,len(created_zombie)):
            x,y = globals()['objz'+str(created_zombie[i])].coord()
            if int(self.x + 10) >= int(x - 20) and int(self.x + 10) <= int(x - 18):
                created_bullet.remove(self.index)
                globals()['objz'+str(created_zombie[i])].health -= self.dmg
                del globals()['objb'+str((self.index))]
                


class normal_b(bullet):
    pass
#=================================================================================================

class sunlight():
    def __init__(self):
        self.speed = 0.05

    def animation(self,obj):
        if self.framevalue >= len(obj):
            self.framevalue = 0
        self.currframe = obj[self.framevalue]
        if self.count == 16:
            self.framevalue += 1
            self.count = 0
        self.count += 1
        self.x -= self.m_speed
        menu.screen.blit(self.currframe,(self.x,self.y))

    def clicked(self):
        del self

class sunlightcounter():
    def __init__(self):
        pass
    
#=================================================================================================


#Main Program
        
menu = window()

bullet_normal = pygame.image.load("Bullets/PeaNormal/PeaNormal_0.png").convert_alpha()

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

zombie_anim = [pygame.image.load("zombies/NormalZombie/Zombie/Zombie_0.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_1.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_2.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_3.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_4.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_5.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_6.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_7.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_8.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_11.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_12.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_13.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_14.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_15.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_17.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_18.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_19.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/Zombie/Zombie_20.png").convert_alpha()]

sun_anim = [pygame.image.load("plants/Sun/Sun_0.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_1.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_2.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_3.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_4.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_5.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_6.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_7.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_8.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_9.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_10.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_11.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_12.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_13.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_14.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_15.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_16.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_17.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_18.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_19.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_20.png").convert_alpha(),
pygame.image.load("plants/Sun/Sun_21.png").convert_alpha()]

zombie_anim_death = [pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_0.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_1.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_2.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_3.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_4.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_5.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_6.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_7.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_8.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_10.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_11.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_12.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_13.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_14.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_15.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_16.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieLostHead_17.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_0.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_1.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_2.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_3.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_4.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_5.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_6.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_7.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_8.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieDie/ZombieDie_9.png").convert_alpha()]



running = True
ingame = False
drag = False
created_plant = []
created_zombie = []
created_sun = []
created_bullet = []



while running:
  if ingame == True:
      clock.tick(240)
      currgame.refresh()
      for i in range(0,len(created_plant)):
          globals()['objp'+str((i+1))].animation(peashooter_anim)
      for i in range(0,len(created_zombie)):

          if globals()['objz'+str((i+1))].health > 0:
            globals()['objz'+str((i+1))].animation(zombie_anim,1)
          else:
            globals()['objz'+str((i+1))].death(zombie_anim_death)
      for i in range(0,len(created_bullet)):
          globals()['objb'+str(created_bullet[i-1])].move()
            
                
            
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
                    drag = False
                    currgame.place()
                    
                    
        
        
            
            


            
            




