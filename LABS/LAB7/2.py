import pygame
import os

pygame.init()

WIDTH = 500
HEIGTH = 500
screen = pygame.display.set_mode((WIDTH, HEIGTH))

songs = ["HRCRX_-_Mineral.mp3", "AurbanniAudio_-_Air__Bach_.mp3", "nik_proteus_-_deep_2.mp3"] 

END_MUSIC = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(END_MUSIC)

#loading our song
order = 0
current_song = songs[order]
path = os.path.join("music",current_song)
pygame.mixer.music.load(path)
pygame.mixer.music.play(0)

def next_music():
    global order
    global current_song
    global songs
    global path

    if order == len(songs) - 1:
        order = 0
    else:    
        order += 1    

    current_song = songs[order]
    path = os.path.join("music",current_song)
    pygame.mixer.music.load(path)    
    pygame.mixer.music.play(0)

def previous_music():
    global order
    global current_song
    global songs
    global path

    order -= 1
    current_song = songs[order]
    path = os.path.join("music",current_song)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # stops music on key "Space"
                pygame.mixer.music.stop() # .pause()
            if event.key == pygame.K_x: # plays music on key "x"
                pygame.mixer.music.play() # .unpause()
            if event.key == pygame.K_LEFT: # turns on previous music by key "left"
                previous_music()
            if event.key == pygame.K_RIGHT: # turns on next music by key "right"
                next_music()    

    pygame.display.flip()