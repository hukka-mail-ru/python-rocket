import time
import rocket
import pygame

class Main:


   
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        done = False
        is_blue = True
        x = 30
        y = 30
        
        r = rocket.Rocket();
        r.askThrottle(70);
        
        for x in range(0, 370):
            time.sleep(0.1) 
            print(x)
            r.tick()
            
            color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, 100+-r.getH(), 1, 1))
            pygame.display.flip()

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