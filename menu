import pygame
import sys
from game import game_loop

pygame.init()

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kapibara")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Galvenā Izvēlne", pygame.font.Font(None, 60), BLACK, screen, screen_width // 2, 100)

        play_button = pygame.Rect(300, 250, 200, 50)
        levels_button = pygame.Rect(300, 350, 200, 50)  
        city_button = pygame.Rect(300, 450, 200, 50)    
        exit_button = pygame.Rect(300, 550, 200, 50)

        pygame.draw.rect(screen, BLACK, play_button)
        pygame.draw.rect(screen, BLACK, levels_button)  
        pygame.draw.rect(screen, BLACK, city_button)    
        pygame.draw.rect(screen, BLACK, exit_button)

        draw_text("Spēlēt", pygame.font.Font(None, 36), WHITE, screen, 400, 275)
        draw_text("Līmeņi", pygame.font.Font(None, 36), WHITE, screen, 400, 375)  
        draw_text("Pilsēta", pygame.font.Font(None, 36), WHITE, screen, 400, 475) 
        draw_text("Izeja", pygame.font.Font(None, 36), WHITE, screen, 400, 575)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_loop()
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if levels_button.collidepoint(event.pos):  
                    print("Вы открыли экран с уровнями игры")
                if city_button.collidepoint(event.pos):    
                    print("Вы открыли экран выбора города")
        pygame.display.update()

main_menu()
