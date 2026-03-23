#Подключаем модуль
import pygame

# Инициализация pygame
pygame.init()

#Установка стартовых значений и настройки
FPS = 60

#Ширина и высота экрана
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

#Инициализируем объект окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Загружаем изображение из относительного пути (только внутри директории проекта)
#background_img = pygame.image.load("")
#Отрисовываем изображение в буфер (пока не выводим на экран)
#Каждый следующий blit нарисует что-то поверх предыдущего с наслоением
#screen.blit(background_img, (0,0))

#Создаем объект для отслеживания времени
clock = pygame.time.Clock()

#Для проверки игрового цикла
running = True

#Дельта-тайм - разница во времени в милисекундах между предыдущим и текущим кадром.
dt = 0

#Позиция игрока в формате Vector2. Теперь player.pos хранит Vector2 объект, который запоминает координаты player
#screen.get_width() screen.get_height() получают размеры экрана
#Чтобы игрок со старта был в центре экрана любого размера, делим эти показатели на 2
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Игровой цикл. Каждая итерация по циклу - один кадр
while running:
    #Заполнение экрана фоновым изображением для очистки от предыдущих изображений.
    #Если при движении игрока за ним тянется "полоса" из его "тела" - значит, этой инструкции нет
    screen.fill('black')
    
    #Обработка событий pygame
    for event in pygame.event.get():
        #Условие выхода на крестик окна
        if event.type == pygame.QUIT:
            #Если условие игрового цикла True, а не переменная, то можем просто инструкцию pygame.quit() сюда вставить
            running = False
        
        #Если событие - это нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:  # Кнопка мыши нажата
            print(f"Нажата кнопка: {event.button}")
            # 1-левая, 2-средняя, 3-правая, 4-колесо вверх, 5-колесо вниз
            print(f"Позиция: {event.pos}")

        '''if event.type == pygame.MOUSEBUTTONUP:  # Кнопка мыши отпущена
            print(f"Отпущена кнопка: {event.button}")
            print(f"Позиция: {event.pos}")'''
    
    #Рисуем кружок игрока
    pygame.draw.circle(screen, "red", player_pos, 40)

    #Передвигаем на клавиши мыши, пока не упираемся в края экрана
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if player_pos.y >= 300 * dt: player_pos.y -= 300 * dt
    if key[pygame.K_s]:
        if player_pos.y <= screen.get_height() - 300 * dt: player_pos.y += 300 * dt
    if key[pygame.K_a]:
        if player_pos.x >= 300 * dt: player_pos.x -= 300 * dt
    if key[pygame.K_d]:
        if player_pos.x <= screen.get_width() - 300 * dt: player_pos.x += 300 * dt


    #Отображаем изображение из буфера (все то, что расовали до этого через blit по слоям)
    pygame.display.flip()

    #tick() : Этот метод следует вызывать один раз за кадр.
    #Он вычисляет, сколько миллисекунд прошло с момента предыдущего вызова.
    #Если вы передадите необязательный аргумент framerate (здесь FPS передаем),
    #функция будет задерживать выполнение игры, чтобы она работала медленнее,
    #чем заданное количество тактов в секунду.
    #Например, если мы передадим 10 в качестве аргумента, программа никогда
    #не будет работать со скоростью более 10 кадров в секунду.
    dt = clock.tick(FPS) / 1000

pygame.quit()