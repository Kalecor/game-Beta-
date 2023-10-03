import pygame
import time
# Инициализация pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Определение размеров окна и ФПС
WIDTH = 1024
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()

#Загрузка заднего фона
background_image = pygame.image.load("Background.jpg")

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Clicker")

# Определение шрифта
font = pygame.font.Font(None, 36)

# Инициализация баланса, количество монет за клик и количество улучшений, а так же начальная цена улучшения
auto = 0
balance = 0
a = 1
n = 0
b = 0
priceU0 = 100
priceA0 = 150

def draw_autoclick():
    #Рисование кнопки автоматических кликов
    pygame.draw.rect(screen, WHITE, (0,85,230,50))

    #Рисование текста
    text = font.render("Buy autoclick = " + str(priceA), True, BLACK)
    screen.blit(text, (0,85))



def draw_upgrade():
    #Рисование кнопки улучшения клика
    pygame.draw.rect(screen, WHITE, (0,30,230,50))

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
    # Обработка и округление цены улучшения
    npriceU = priceU0 * (1.07 ** n)
    priceU = round (npriceU)

    #Обработка и округление цены автоклика
    npriceA = priceA0 * (1.07 ** b)
    priceA = round (npriceA)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия на кнопку
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if 512 <= mouse_pos[0] <= 612 and 300 <= mouse_pos[1] <= 350:
                    update_balance()
                # Проверка нажатия на кнопку и количества монет на улучшение
                elif 0 <= mouse_pos[0] <= 230 and 30 <= mouse_pos[1] <= 80:
                    if balance >= priceU:
                        a = a + 1
                        n = n + 1
                        balance = balance - priceU
                # Проверка нажатия на кнопку покупки автокликов, не работает
                elif 0 <= mouse_pos[0] <= 230 and 85 <= mouse_pos[1] <= 135:
                    if balance >= priceA:
                        b = b + 1
                        auto = auto + 1
                        balance = balance - priceA

    # Выставление FPS
    clock.tick(FPS)           
    
    # Рисование заднего фона
    screen.blit(background_image, (0,0))
    
    # Рисование кнопки и баланса
    draw_button()
    draw_balance()
    draw_upgrade()
    draw_coinsPerClick()
    draw_autoclick()
    
    # Обновление экрана
    pygame.display.flip()

# Завершение программы
pygame.quit()