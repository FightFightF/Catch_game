import pygame
import sys
import random

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def game_loop():
    pygame.init()

    screen_width = 1000
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Kapibara")

    background = pygame.image.load("background_game_1.png").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    pygame.mixer.music.load("8_bit_menu_game.mp3")
    pygame.mixer.music.play(-1)

    pygame.font.init()
    font = pygame.font.Font(None, 65)

    item_images = {
    "orange": [pygame.transform.scale(pygame.image.load("orange_1.png").convert_alpha(), (55, 55)),
               pygame.transform.scale(pygame.image.load("orange_2.png").convert_alpha(), (55, 55)),
               pygame.transform.scale(pygame.image.load("orange_3.png").convert_alpha(), (55, 55)),
               pygame.transform.scale(pygame.image.load("orange_4.png").convert_alpha(), (55, 55))],
    "watermelon": [pygame.transform.scale(pygame.image.load("watermelon_1.png").convert_alpha(), (55, 55)),
                   pygame.transform.scale(pygame.image.load("watermelon_2.png").convert_alpha(), (55, 55)),
                   pygame.transform.scale(pygame.image.load("watermelon_3.png").convert_alpha(), (55, 55)),
                   pygame.transform.scale(pygame.image.load("watermelon_4.png").convert_alpha(), (55, 55))],
    "pear": [pygame.transform.scale(pygame.image.load("pear_1.png").convert_alpha(), (75, 75)),
             pygame.transform.scale(pygame.image.load("pear_2.png").convert_alpha(), (75, 75)),
             pygame.transform.scale(pygame.image.load("pear_3.png").convert_alpha(), (75, 75)),
             pygame.transform.scale(pygame.image.load("pear_4.png").convert_alpha(), (75, 75))],
    "Lats": [pygame.transform.scale(pygame.image.load("2Ls_1.png").convert_alpha(), (40, 40)),
             pygame.transform.scale(pygame.image.load("2Ls_2.png").convert_alpha(), (40, 40)),
             pygame.transform.scale(pygame.image.load("2Ls_3.png").convert_alpha(), (40, 40)),
             pygame.transform.scale(pygame.image.load("2Ls_4.png").convert_alpha(), (40, 40)),],
    "Motorbike": [pygame.transform.scale(pygame.image.load("motorbike_1.png").convert_alpha(), (70, 70)),
                  pygame.transform.scale(pygame.image.load("motorbike_2.png").convert_alpha(), (70, 70)),
                  pygame.transform.scale(pygame.image.load("motorbike_3.png").convert_alpha(), (70, 70)),
                  pygame.transform.scale(pygame.image.load("motorbike_4.png").convert_alpha(), (70, 70))],
    "Cigarette_Pack": [pygame.transform.scale(pygame.image.load("pack_1.png").convert_alpha(), (60, 60)),
                       pygame.transform.scale(pygame.image.load("pack_2.png").convert_alpha(), (60, 60)),
                       pygame.transform.scale(pygame.image.load("pack_3.png").convert_alpha(), (60, 60)),
                       pygame.transform.scale(pygame.image.load("pack_4.png").convert_alpha(), (60, 60))]
    }

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            #Character
            self.image_left = pygame.image.load("capybara_left_1.png").convert_alpha()
            self.image_right = pygame.image.load("capybara_right_1.png").convert_alpha()

            # Start Character form
            self.original_width = self.image_left.get_width()
            self.original_height = self.image_left.get_height()

            # New sprite form
            self.width = 100
            self.height = int(self.original_height * (self.width / self.original_width))
            self.image_left = pygame.transform.scale(self.image_left, (self.width, self.height))
            self.image_right = pygame.transform.scale(self.image_right, (self.width, self.height))


            self.image = self.image_right
            self.rect = self.image.get_rect()
            self.rect.centerx = screen_width // 2
            self.rect.bottom = screen_height - 10
            self.speed = 7
            self.direction = "right"

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if self.rect.left > 0:  
                    self.rect.x -= self.speed
                    self.image = self.image_left
                    self.direction = "left"
            if keys[pygame.K_RIGHT]:
                if self.rect.right < screen_width:  
                    self.rect.x += self.speed
                    self.image = self.image_right
                    self.direction = "right"

    class Item(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.type = item_type
            self.image_index = 0  
            self.image_list = item_images[self.type]
            self.image = self.image_list[self.image_index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 3
            self.update_counter = 0

        def update(self):
            self.rect.y += self.speed
            if self.rect.top > screen_height:
                self.kill()  
            else:
                if self.update_counter % 5 == 0:
                    self.image_index = (self.image_index + 1) % len(self.image_list)
                    self.image = self.image_list[self.image_index]
                self.update_counter += 1

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    items = pygame.sprite.Group()

    running = True
    clock = pygame.time.Clock()
    score = 0
    forbidden_items_count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.randint(1, 100) == 1:
            item_type = random.choice(list(item_images.keys()))
            new_item = Item(random.randint(0, screen_width - 30), 0)
            all_sprites.add(new_item)
            items.add(new_item)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, items, True)
        for hit in hits:
            if hit.type == "Motorbike" or hit.type == "Cigarette_Pack":
                forbidden_items_count += 1
                print("Bad Items:", forbidden_items_count)
                if forbidden_items_count >= 5:
                    print("Spēle beigusies!")
                    running = False
            else:
                score += 1
                print("Score:", score)

        screen.blit(background, (0, 0))

        score_text = font.render(f"{score}", True, WHITE)
        score_rect = score_text.get_rect(center=(screen_width // 2, 20))
        screen.blit(score_text, score_rect)

        forbidden_items_text = font.render(f"Slikti: {forbidden_items_count}/5", True, WHITE)
        forbidden_items_rect = forbidden_items_text.get_rect(left=20, centery=20)
        screen.blit(forbidden_items_text, forbidden_items_rect)

        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
