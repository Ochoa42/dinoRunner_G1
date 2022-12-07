import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT,SCREEN_WIDTH, TITLE, FPS 
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacleManager import ObstacleManager




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #-----> agregamos el ancho y largo que qeremos la ventana
        self.clock = pygame.time.Clock() # ----> tiempo
        self.playing = False
        self.game_speed = 30
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()


    def run(self):
        self.playing = True # ----> ponemos en play el juego
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()    

    def events(self):
        for event in pygame.event.get():  #----> capturamos todos los tipos de eventos
            if event.type == pygame.QUIT:  #----> en caso el tipo de evento es quit o exit(), nos salimos del juego 
                self.playing = False
    
    def update(self):
        user_input =pygame.key.get_pressed()
        self.obstacle_manager.update(self)
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)    # cada cuanto milisegundo queremos q se dibuje nuestra imagen
        self.screen.fill((255,255,255) )  #---> agregamos color de fondo
        self.draw_background() 
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update() # 
        pygame.display.flip()  #---> actualizar pantalla
        

    def draw_background(self):
        image_with = BG.get_width()  # odtenemos el ancho de la imagen y lo guardamos en (image_with)
        self.screen.blit(BG,(self.x_pos_bg, self.y_pos_bg)) #le decimos que posicion queremos dibujar 
        self.screen.blit(BG,(image_with + self.x_pos_bg,self.y_pos_bg)) # sumamos el ancho de bg a la posicion x

        if (self.x_pos_bg <= - image_with):  
            self.screen.blit(BG,(image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg = self.x_pos_bg - self.game_speed     



