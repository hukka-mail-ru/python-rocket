import time
import math

MIN_THROTTLE = 0   # percent
MAX_THROTTLE = 100 # percent
GRAVITY = -9.8 # G, m/s^2

class Rocket():
    

    def __init__(self):

        self.mass = 1500 # kg
        self.fuelMass = 100 # kg
        self.maxAcceleration = 100 # m/s^2 at 100% throttle
        self.throttle = 0 # percent
        self.askedThrottle = 0 # percent
        self.a = 0 # actual acceleration, m/s^2
        self.v = 0 # vertical velocity, m/s
        self.h = 100 # height, m
        
        self.previousTimestamp = time.time()
        
    def getFuelMass(self):        
        return self.fuelMass
    
    def askThrottle(self, throttle: int):
        self.askedThrottle = throttle
     
    def getH(self):
        return  self.h   
    
    def getA(self):
        return  self.a   
    
    def getV(self):
        return  self.v  

    def tick(self):
        
        timestamp = time.time()
        dt = timestamp - self.previousTimestamp
        
        print ("dt: ", dt)

        # acceleration     
        self.a = GRAVITY + self.maxAcceleration / 100 * self.throttle  
        
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
        
        print ("self.throttle: ", self.throttle)
        print ("dh: ", dh)
        print ("self.a: ", self.a)
        print ("self.v: ", self.v)
        print ("self.h: ", self.h)
        print ("================================= ")
        
        self.previousTimestamp = timestamp
        