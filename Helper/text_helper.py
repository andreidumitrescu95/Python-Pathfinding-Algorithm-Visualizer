import pygame

def drawTextcenter(text,font,screen,x,y,color):
    textobj=font.render(text,True,color)
    textrect=textobj.get_rect(center=((int)(x),(int)(y)))
    screen.blit(textobj,textrect)

def drawText(text, font, surface, x, y,color):
    textobj=font.render(text, 1, color)
    textrect=textobj.get_rect()
    textrect.topleft=(x, y)
    surface.blit(textobj, textrect)