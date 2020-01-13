import pygame

pygame.mixer.init()

def play(filename, wait=False):
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
	if wait:
		while pygame.mixer.music.get_busy() == True:
		    continue