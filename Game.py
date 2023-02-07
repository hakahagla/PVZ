#Plant VS Zombies

import pygame
import random

#Initalise Modules

pygame.init()
font = pygame.font.Font("SERIO___.TTF",18)
clock =  pygame.time.Clock()
width,height = (1100,680)#Size of window

#Import assests

slot = pygame.image.load('Screen/ChooserBackground.png')
shovel = pygame.image.load('Screen/Shovel.jpg')
bg = pygame.image.load("Background/mainmenu.png")
bg = pygame.transform.scale(bg, (width, height))
bg2 = pygame.image.load("Background/Background_0.jpg")
bg2 = pygame.transform.scale(bg2, (1430, height))


#Classes
#=================================================================================================       
class window():
    global bg
    global bg2
    global width,height
    global s_cd
    

    def __init__(self):
        self.width,self.height = (1100,680)
        self.background = bg
        self.background2 = bg2
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.background,(0,0))

    def clicked(self):
        global ingame
        global currgame
        global s_count
        global s_cd
        x,y=pygame.mouse.get_pos()
        if x >= 515 and x <= 890 and  y >= 90 and y <= 235: #Ingame button is clicked
            s_count = sunlightcounter()
            s_cd = sunlightgeneration()
            self.screen.blit(self.background2,(0,0))
            ingame = True
            currgame = game()
#=================================================================================================         
class card_peashooter():
        
    def __init__(self):
        self.pcard = pygame.image.load('cards/card_peashooter.png')
        self.card = self.pcard
        menu.screen.blit(self.card,(100,10))

    def clicked(self):  
        pass
#=================================================================================================            
class game():
    global lawnmower
    global slot
    global shovel
    global bg2
    global s_count
    global s_cd
    global created_lawnmower
    global lawnmower

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
        self.l_coord = [[190, 120],[190, 220],[190, 320],[180, 420],[170, 550]]
        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        for i in created_lawnmower:
            globals()['objl'+str(i)] = lawnmower(self.l_coord[i-1][0],self.l_coord[i-1][1],i)
        
    def refresh(self):
        
        menu.screen.blit(self.background,(0,0))
        menu.screen.blit(self.slot,(0,0))
        menu.screen.blit(self.shovel,(660,0))
        

        test_card = card_peashooter()
        s_count.display()
        s_cd.generate()
    
    def clicked(self):
        global drag
        global created_sun
        self.targetxz = 0
        self.targetxy = 0
        peashooter = pygame.image.load("plants/Peashooter/Peashooter_0.png").convert_alpha()
        x,y=pygame.mouse.get_pos()
        if x >= 100 and x <= 160 and y >= 10 and y <= 95:
            drag = True
        if drag == True:
            game.drag(self,peashooter)
        else:
            if len(created_sun) != 0:
                for i in created_sun:
                    if globals()['objs'+ str(i)].clicked() == False:
                        self.distancez = 999
                        for i in range (0,len(self.c_coord)):
                            self.diffxz = self.c_coord[i][0]-x
                            self.diffyz = self.c_coord[i][1]-y
                            self.temp = (self.diffxz**2+self.diffyz**2)**1/2
                            if self.temp <= self.distancez:
                                self.targetxz,self.targetyz = self.c_coord[i][0],self.c_coord[i][1]
                                self.distance = self.temp
                                for j in range(0,999):
                                    if j+1 not in created_zombie:
                                        created_zombie.append(j+1)
                                        globals()['objz'+str(j+1)] = normalzombie(self.targetxz-30,self.targetyz-50,j+1)
                                        break
            else:
                self.distancez = 999
                for i in range (0,len(self.c_coord)):
                    self.diffxz = self.c_coord[i][0]-x
                    self.diffyz = self.c_coord[i][1]-y
                    self.temp = (self.diffxz**2+self.diffyz**2)**1/2
                    if self.temp <= self.distancez:
                        self.targetxz,self.targetyz = self.c_coord[i][0],self.c_coord[i][1]
                        self.distance = self.temp
                        for j in range(0,999):
                            if j+1 not in created_zombie:
                                created_zombie.append(j+1)
                                globals()['objz'+str(j+1)] = normalzombie(self.targetxz-30,self.targetyz-50,j+1)
                                break

    def drag(self,obj):
        global drag
        x,y=pygame.mouse.get_pos()
        menu.screen.blit(obj,(x-30,y-25))

    def place(self):
        global created_plant
        if s_count.counter - 100 >= 0: #Replace 100 with an variable which the function takes in first and stores it to that
            s_count.update(-100)
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
            for j in range(0,999):
                if j+1 not in created_plant:
                    created_plant.append(j+1)
                    globals()['objp'+str(j+1)] = peashooter(self.targetx-30,self.targety-25,j+1)
                    break
            
        #Validate there are only one plant on that tile
#=================================================================================================
class plant():
    
    def __init__(self,x,y,index):
        self.health = 0
        self.a_dmg = 0
        self.a_speed = 0
        self.framevalue = 0
        self.cd = 0
        self.cd_constant = 0
        self.x,self.y = x,y
        self.count = 0
        self.created = False
        self.index = index

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
        self.death()
        self.shoot(bullet_normal)

    def shoot(self,obj):
        global created_zombie
        global created_bullet
        self.cd -= 1 
        if self.cd <= 0 and len(created_zombie) != 0: #Fixed the issue where the plant does shoot immediately when zombie spawns
            self.cd = self.cd_constant
            self.created = False
            for i in created_zombie:
                x,y = globals()['objz'+str(i)].coord()                 
                if y + 50 == self.y + 25 and x >= self.x and self.created == False: #If there is a zombie in front
                    self.created = True
                    for j in range(1,999):
                        if j not in created_bullet:
                            created_bullet.append(j)
                            globals()['objb'+str(j)] = normal_b(10,obj,self.x-10,self.y,j)
                            break

    def coord(self):
        return self.x,self.y

    def death(self):
        global created_plant
        if self.health <= 0 :
            created_plant.remove(self.index)
            del globals()['objp' + str(self.index)]
            
class peashooter(plant):
    global bullet_normal
    
    def __init__(self,x,y,index):
        self.health = 100
        self.a_dmg = 20
        self.a_speed = 1
        self.cd_constant = 240 * 3
        self.cd = 0
        self.framevalue = 0
        self.x,self.y = x,y
        self.count = 0
        self.created = False
        self.index = index
#=================================================================================================
class zombie():

    def __init__(self,x,y,index):
        self.health = 100
        self.dmg = 25
        self.speed = 0.05
        self.framevalue = 0
        self.x,self.y = x,y
        self.count = 0
        self.index = index
        self.nocollision = False
        self.nocollisionplant = False

    def coord(self):
        return self.x,self.y

    def animation(self,obj,anim_type):
        self.atype = anim_type
        if self.framevalue >= len(obj):
            self.framevalue = 0
            if self.collision() == True:
                self.attack()
        self.currframe = obj[self.framevalue]
        if self.count == 16:
            self.framevalue += 1
            self.count = 0
            
        self.count += 1
        if self.atype == 1:
            self.x -= self.speed
            menu.screen.blit(self.currframe,(self.x,self.y))
        elif self.atype == 2:
            menu.screen.blit(self.currframe,(self.x-50,self.y-10))
        elif self.atype == 3:
            menu.screen.blit(self.currframe,(self.x,self.y))
            
    def death(self):
        global created_zombie
        if self.health <= 0:
            self.nocollision = True
            self.animation(zombie_anim_death,2)
        if self.framevalue == len(zombie_anim_death):
            created_zombie.remove(self.index)
            del globals()['objz'+str(self.index)]

    def collision(self):
        global created_plant
        for i in created_plant:
            x,y = globals()['objp'+str(i)].coord()
            if int(self.x - 45) <= int(x) and int(self.x - 33) >= int(x) and int(self.y ) == int(y - 25):
                self.target = i
                return True
                break

    def attack(self):
        global zombie_anim_attack
        globals()['objp' + str(self.target)].health -= self.dmg
          
class normalzombie(zombie):
    def __init__(self,x,y,index):
        self.health = 100
        self.dmg = 25
        self.speed = 0.05
        self.framevalue = 0
        self.x,self.y = x,y
        self.count = 0
        self.index = index
        self.nocollision = False
#=================================================================================================
class bullet():
    def __init__(self,dmg,anim,x,y,index):
        self.dmg = dmg
        self.speed = 0.1
        self.x = x + 30
        self.y = y
        self.anim = anim
        self.index = index  #Which object name in the created_bullet array it is
        
        
    def move(self):
        self.collision()
        self.x += 1
        menu.screen.blit(self.anim,(self.x,self.y))
        if self.x >= 1100:
            created_bullet.remove(self.index)
            del globals()['objb'+str((self.index))]


    def collision(self):
        global created_zombie
        global created_bullet
        for i in created_zombie:
            x,y = globals()['objz'+str(i)].coord()
            if int(self.x + 5) >= int(x - 20) and int(self.x + 5) <= int(x - 18) \
            and int(self.y+20) >= int(y) and int(self.y - 100) <= int(y)\
            and globals()['objz'+str(i)].nocollision == False:
                created_bullet.remove(self.index)
                globals()['objz'+str(i)].health -= self.dmg
                del globals()['objb'+str((self.index))]
                break
                
class normal_b(bullet):
    pass
#=================================================================================================
class sunlightgeneration():
    global created_sun
    global sun_anim

    def __init__(self):
        self.cd = 500 #Set an initial value so sunlight does not spawn straight away
        self.cd_constant = 240 * 4
        
    def generate(self):
        self.cd -= 1
        if self.cd <= 0:
            self.x = random.randint(260,990)
            if self.x <= 760:
                self.y = 110
            else: 
                self.y = 0
            self.cd = self.cd_constant
            for i in range(1,999):
                if i not in created_sun:
                    created_sun.append(i)
                    globals()['objs'+str(i)] = sunlight(self.x,self.y,25,i)
                    break
#================================================================================================
class sunlight():
    global s_count
    global created_sun

    def __init__(self,x,y,amount,index):
        self.speed = 0.1
        self.x = x
        self.y = y
        self.amount = amount
        self.index = index
        self.framevalue = 0
        self.count = 0

    def animation(self,obj):
        if self.framevalue >= len(obj):
            self.framevalue = 0
        self.currframe = obj[self.framevalue]
        if self.count == 16:
            self.framevalue += 1
            self.count = 0
        self.count += 1
        self.move()
        
    def move(self):
        self.y += self.speed
        menu.screen.blit(self.currframe,(self.x,self.y))

    def clicked(self):
        x,y = pygame.mouse.get_pos()
        if x >= self.x - 75 and x <= self.x + 75 and y >= self.y - 75 and y <= self.y + 75:
            s_count.update(self.amount)
            created_sun.remove(self.index)
            del globals()['objs' + str(self.index)]
            return True
        else:
            return False
#=================================================================================================       
class sunlightcounter():
    def __init__(self):
        self.counter = 1000
        self.display()
    
    def update(self,amount):
        self.counter += amount
        self.display()

    def display(self):
        output = font.render(str(self.counter),False,(0,0,0))
        output_rect = output.get_rect(center=(50, 95))
        menu.screen.blit(output,(output_rect))
#=================================================================================================
class lawnmower():
    global lawnmower_anim
    global created_zombie
    def __init__(self,x,y,index):
        
        self.dmg = 10000
        self.speed = 1.25 
        self.x = x
        self.y = y
        self.index = index
        self.nomove = True
        self.nocollision = True
        menu.screen.blit(lawnmower_anim,(self.x,self.y))
        

    def collision(self):
        for i in created_zombie:
            x,y = globals()['objz'+str(i)].coord()
            if self.y - 20 <= y and self.y + 20 >=y and int(self.x+55) <= int(x) and int(self.x+60) >= int(x):
                self.nomove = False
                globals()['objz'+str(i)].health -= self.dmg


    def move(self):
        if self.x >= 1110:
            created_lawnmower.remove(self.index)
            del globals()['objl'+str(self.index)]
        if self.nomove == False:
            self.x += self.speed
        menu.screen.blit(lawnmower_anim,(self.x,self.y))
        self.collision()


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
zombie_anim_attack = [pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_0.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_1.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_2.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_3.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_4.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_5.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_6.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_7.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_8.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_9.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_10.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_11.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_12.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_13.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_14.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_15.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_16.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_17.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_18.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_19.png").convert_alpha(),
pygame.image.load("zombies/NormalZombie/ZombieAttack/ZombieAttack_20.png").convert_alpha()]
lawnmower_anim =  pygame.image.load('Screen/car.png')

running = True
ingame = False
drag = False
created_plant = []
created_zombie = []
created_sun = []
created_bullet = []
created_sun = []
created_lawnmower = [1,2,3,4,5]

while running:
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
                    
  if ingame == True:
    clock.tick(240)
    currgame.refresh()

    for i in created_plant:
        globals()['objp'+str(i)].animation(peashooter_anim)
    for i in created_sun:
        globals()['objs'+str(i)].animation(sun_anim)
    for i in created_zombie:
        if globals()['objz'+str(i)].health > 0:
            if globals()['objz'+str(i)].collision() == True: #Collided with a plant
                globals()['objz'+str(i)].animation(zombie_anim_attack,3)
            else: #Walk
                globals()['objz'+str(i)].animation(zombie_anim,1)
        else:
            globals()['objz'+str(i)].death()
    for i in created_bullet:
        globals()['objb'+str(i)].move()
    for i in created_lawnmower:
        globals()['objl'+str(i)].move()
    
    
  if drag == True:
      currgame.clicked()

  pygame.display.flip()

  
