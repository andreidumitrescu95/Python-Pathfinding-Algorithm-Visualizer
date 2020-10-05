import pygame
from Helper.text_helper import drawText, drawTextcenter 

class Button(object):
    global screen_width,screen_height,screen
    def __init__(self,x,y,width,height,text_color,background_color,text):
        self.rect=pygame.Rect(x,y,width,height)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.text_color=text_color
        self.background_color=background_color
        self.angle=0

    def check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.background_color,(self.rect),0)
        drawTextcenter(self.text,pygame.font.SysFont('calibri', 18),WIN,self.x+self.width/2,self.y+self.height/2,self.text_color)  
        pygame.draw.rect(WIN,self.text_color,self.rect,3)