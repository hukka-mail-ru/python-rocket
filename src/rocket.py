import time
import sys
import multiprocessing as ms
import pygame

MIN_THROTTLE = 0   # percent
MAX_THROTTLE = 100 # percent
GRAVITY = -9.8 # G, m/s^2


class Rocket():
    

    def __init__(self):

        self.mass = 10000 # kg
        self.fuelMass = 5000 # kg
        self.fuelBurnSpeed = 1000 # kg/sec at 100% throttle
        self.throttle = 0 # percent
        self.maxF = 200000 # Jouls at 100% throttle
        self.askedThrottle = 0 # percent
        self.a = 0 # actual acceleration, m/s^2
        self.v = 0 # vertical velocity, m/s
        self.h = 500 # height, m
        self.startTimestamp = time.time()
        self.previousTimestamp = time.time()
        
    def getFuelMass(self):        
        return self.mass - self.fuelMass
    
    def askThrottle(self, throttle: int):
        self.askedThrottle = throttle
    
    def getThrottle(self):
        return  self.throttle   
     
    def getH(self):
        return  self.h   
    
    def getA(self):
        return  self.a   
    
    def getV(self):
        return  self.v  

    def tick(self):
        
        timestamp = time.time()
        dt = timestamp - self.previousTimestamp
        
        # burnt fuel
        bf = 0
        if self.getFuelMass() > 0:
            bf = self.fuelBurnSpeed / 100 * self.throttle * dt
        
        # mass
        self.mass -= bf

        # engine force   
        f = 0 
        if self.getFuelMass() > 0:
            f = self.maxF / 100 * self.throttle
          
        # acceleration 
        self.a = GRAVITY + f / self.mass  
        
        # distance
        dh = self.v * dt + self.a * dt * dt / 2
        
        # velocity
        self.v = self.v + self.a * dt        
        
        # height
        self.h += dh
        
        # update throttle
        if(self.throttle < self.askedThrottle):
            self.throttle += 1
        elif(self.throttle > self.askedThrottle):
            self.throttle -= 1
            
        if(self.throttle < MIN_THROTTLE):
            self.throttle = MIN_THROTTLE
        elif(self.throttle > MAX_THROTTLE):
            self.throttle = MAX_THROTTLE
        
        
        print ("t: ", timestamp - self.startTimestamp)
        print ("self.throttle: ", self.throttle)
        print ("dh: ", dh)
        print ("a: ", self.a)
        print ("v: ", self.v)
        print ("h: ", self.h)
        print ("m: ", self.mass)
        print ("================================= ")
        
        
        self.previousTimestamp = timestamp
   

  
     
def startRocket(v: ms.Value, 
                a: ms.Value, 
                h: ms.Value,
                asked: ms.Value):
    r = Rocket()
    
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
        
    for x in range(0, 1000):
        r.tick()
        v.value = r.getV()
        a.value = r.getA()
        h.value = r.getH()
        r.askThrottle(asked.value)
        
        color = (0, 0, 0)
        pygame.draw.rect(screen, color, pygame.Rect(100,100,50,50))
        
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(r.getFuelMass()), 1, (255,255,0))
        screen.blit(label, (100, 100))
        
        color = (255, 255, 255)
        pygame.draw.rect(screen, color, pygame.Rect(0, 500, 1000, 1))
        
        color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, 500-r.getH(), 1, 1))
        pygame.display.flip()
        
        if(r.getH() <= 0):
            break
            
        time.sleep(0.01) 
    
    done = False    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                done = True
      
    print("Done") 
     