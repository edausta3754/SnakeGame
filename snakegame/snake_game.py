import pygame
import time
import random

pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (0, 200, 50)
OBSTACLE_COLOR = (0, 0, 0)  # Engellerin rengi
BLUE = (0,0,200)
# Yılan, yem ve engel başlangıç pozisyonları
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 4

food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]

obstacle_list = []  # Engel listesi
num_obstacles = 20  # Ekran üzerine yerleştirilecek engel sayısı

for _ in range(num_obstacles):
    obstacle_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
    obstacle_list.append(obstacle_pos)

food_spawn = True

paused = False  # Oyunun duraklatılıp duraklatılmadığını kontrol etmek için
game_over = False  # Oyunun bitip bitmediğini kontrol etmek için

font = pygame.font.SysFont(None, 55)

# Skor
score = 0

# Yılan başı görselini yükle
head_img = pygame.image.load("head.jpg")
head_img = pygame.transform.scale(head_img, (10, 10))  # Yılanın başını 10x10 piksele ölçeklendir

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and not direction == 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and not direction == 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and not direction == 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and not direction == 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.key == pygame.K_RETURN:
                # Game Over durumunda Enter tuşuna basıldığında oyunu tekrar başlat
                game_over = False
                snake_pos = [100, 50]
                snake_body = [[100, 50], [90, 50], [80, 50]]
                direction = 'RIGHT'
                change_to = direction
                speed = 15
                food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                            random.randrange(1, (HEIGHT // 10)) * 10]
                obstacle_list = []
                for _ in range(num_obstacles):
                    obstacle_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                                    random.randrange(1, (HEIGHT // 10)) * 10]
                    obstacle_list.append(obstacle_pos)
                food_spawn = True
                score = 0  # Yeni oyun başladığında skoru sıfırla

    # Oyun duraklatılmadıysa ve oyun bitmediyse devam et
    if not paused and not game_over:
        # Yılanın hareketi
        if change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'

        # Yılanın pozisyonunu güncelle
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Duvarlara, engellere veya kuyruğa çarpma kontrolü
        if (
            snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body[1:] or
            snake_pos in obstacle_list
        ):     
            game_over = True

        # Yılanın vücudunu güncelle
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            food_spawn = False
            score += 1  # Yem yendiğinde skoru artır
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                        random.randrange(1, (HEIGHT // 10)) * 10]
            food_spawn = True

        # Ekranı temizle
        WIN.fill(WHITE)

        # Engelleri çiz
        for obstacle_pos in obstacle_list:
            pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(obstacle_pos[0], obstacle_pos[1], 10, 20))

        # Yılan başını çiz
        WIN.blit(head_img, (snake_pos[0], snake_pos[1]))

        # Yılanın geri kalanını ve yemi çiz
        for pos in snake_body[1:]:
            pygame.draw.rect(WIN, PURPLE, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Skoru ekrana yazdır
        score_text = font.render("Score: {}".format(score), True, BLUE)
        WIN.blit(score_text, (10, 10))

        # Ekranı güncelle
        pygame.display.flip()

        # FPS ayarı
        pygame.time.Clock().tick(speed)
        # Her 15 yemde bir hızı artır
    if score % 5 == 0 and score > 0:
        speed += 0.03
    else:
        # Oyun duraklatıldı veya bitti, ekrana mesaj yazısı ekle
        if game_over:
            game_over_text = font.render("GAME OVER", True, RED)
            score_text = font.render("Score: {}".format(score), True, BLUE)
            retry_text = font.render("PLAY AGAIN? (Enter)", True, RED)
            WIN.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
            WIN.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2))
            WIN.blit(retry_text, (WIDTH // 2 - 200, HEIGHT // 2 + 50))
        else:
            text = font.render("PAUSE", True, RED)
            WIN.blit(text, (WIDTH // 100 - 200, HEIGHT // 15 - 30))
        pygame.display.flip()
