import pygame

# Инициализация pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение размеров окна
WIDTH = 800
HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Увеличение баланса")

# Определение шрифта
font = pygame.font.Font(None, 36)

# Инициализация баланса
balance = 0

def draw_button():
    # Рисование кнопки
    pygame.draw.rect(screen, WHITE, (350, 250, 100, 50))
    
    # Рисование текста на кнопке
    text = font.render("Увеличить", True, BLACK)
    screen.blit(text, (355, 260))

def update_balance():
    # Увеличение баланса на 1
    global balance
    balance += 1

def draw_balance():
    # Рисование текущего баланса
    text = font.render("Баланс: " + str(balance), True, BLACK)
    screen.blit(text, (350, 350))

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия на кнопку
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if 350 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 300:
                    update_balance()
    
    # Очистка экрана
    screen.fill(BLACK)
    
    # Рисование кнопки и баланса
    draw_button()
    draw_balance()
    
    # Обновление экрана
    pygame.display.flip()

# Завершение программы
pygame.quit()