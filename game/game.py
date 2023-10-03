import pygame
# Инициализация pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Определение размеров окна
WIDTH = 1024
HEIGHT = 600

#Создание заднего фона
background_image = pygame.image.load("Background.jpg")

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker")

# Определение шрифта
font = pygame.font.Font(None, 36)

# Инициализация баланса и количества денег за нажатие
balance = 0
a = 1
n = 1
priceU0 = 50

def draw_upgrade():
    #Рисование кнопки улучшения клика
    pygame.draw.rect(screen, WHITE, (0,30,220,50))

    #Рисование текста
    text = font.render("Upgrade cost = " + str(priceU), True, BLACK)
    screen.blit(text, (0, 30))

def draw_button():
    # Рисование кнопки
    pygame.draw.rect(screen, WHITE, (512, 300, 100, 50))
    
    # Рисование текста на кнопке
    text = font.render("Click", True, BLACK)
    screen.blit(text, (512, 300))

def update_balance():
    # Увеличение баланса
    global balance
    balance += a

def draw_balance():
    # Рисование текущего баланса
    text = font.render("Balance: " + str(balance), True, BLACK)
    screen.blit(text, (0, 0))

def draw_coinsPerClick():
    #Количество монет за нажатие
    text = font.render("Coins per click: " +str(a),True,BLACK)
    screen.blit(text, (250,0))

# Основной цикл программы
running = True
while running:
    # Обработка событий

    npriceU = priceU0 * (1.07 ** n)
    priceU = round (npriceU)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия на кнопку
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if 512 <= mouse_pos[0] <= 612 and 300 <= mouse_pos[1] <= 350:
                    update_balance()
                elif 0 <= mouse_pos[0] <= 220 and 30 <= mouse_pos[1] <= 80:
                    if balance >= priceU:
                        a = a + 1
                        n = n + 1
                        balance = balance - priceU

                
    
    # Очистка экрана
    screen.blit(background_image, (0,0))
    
    # Рисование кнопки и баланса
    draw_button()
    draw_balance()
    draw_upgrade()
    draw_coinsPerClick()
    
    # Обновление экрана
    pygame.display.flip()

# Завершение программы
pygame.quit()
