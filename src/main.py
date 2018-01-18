import time
import rocket
import pygame
import multiprocessing as ms

class Main:


   
    def start(self):
        #pygame.init()
        #screen = pygame.display.set_mode((1200, 600))
        done = False
        is_blue = True
        x = 30
        y = 30 
        
        v = ms.Value('d', 0.0)
        a = ms.Value('d', 0.0)
        h = ms.Value('d', 0.0)
        asked = ms.Value('i', 0)
        
        #parent_conn, rocket_conn = ms.Pipe()
        p = ms.Process(target=rocket.startRocket, args=(v,a,h, asked))
        p.start()
 
      #  oldH = 1000  
        for i in range(1, 10):
            print("V:", v.value)   
            print("a:", a.value)   
            print("h:", h.value)   
            
            if(a.value > 5):
                print("too fast")
                asked.value = 0
            else:                            
                if(a.value < 0):
                    if(v.value < -3):
                        asked.value = 100
                    else:
                        asked.value = 0
                                
                elif(a.value > 0):
                    if(v.value > -3):
                        asked.value = 0
                    else:
                        asked.value = 100
            
            time.sleep(1)

        p.join()
           
        '''
        r = rocket.Rocket();
        
        for x in range(0, 200):
            time.sleep(0.01) 
            print(x)
            r.tick()
                
                        
            color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, 100+-r.getH(), 1, 1))
            pygame.display.flip()
            
        oldH = 100     
        for x in range(200, 1800):
            time.sleep(0.01) 
            print(x)
            r.tick()
       
            if(r.getA() > 5):
                print("too fast")
                r.askThrottle(0)
            else:                            
                if(r.getA() < 0):
                    if(r.getV() < -3):
                        r.askThrottle(100)
                    else:
                        r.askThrottle(0)
                                
                elif(r.getA() > 0):
                    if(r.getV() > -3):
                        r.askThrottle(0)
                    else:
                        r.askThrottle(100)  
                    
                        
            color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, 100+-r.getH(), 1, 1))
            pygame.display.flip()

'''

'''
        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
            
            screen.fill((0, 0, 0))
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
            
            pygame.display.flip()
            clock.tick(60)
'''
        

if __name__ == '__main__': # pragma: no cover
    m = Main()
    m.start()