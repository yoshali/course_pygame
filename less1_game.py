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

#target_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dragging = False

#Позиция игрока в формате Vector2. Теперь player.pos хранит Vector2 объект, который запоминает координаты player
#screen.get_width() screen.get_height() получают размеры экрана
#Чтобы игрок со старта был в центре экрана любого размера, делим эти показатели на 2
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

mouse_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Кнопка мыши нажата
            mouse_pos = pygame.Vector2(event.pos)
            # Проверяем, попали ли по игроку
            if mouse_pos.distance_to(player_pos) < 40:
                    dragging = True
                    drag_offset = player_pos - mouse_pos
                    print("Начали перетаскивать игрока")

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if dragging:
                dragging = False
                print("Отпустили игрока")

        if event.type == pygame.MOUSEMOTION and dragging:
            mouse_pos = pygame.Vector2(event.pos)
            player_pos = mouse_pos + drag_offset
            # Опционально: ограничиваем, чтобы игрок не выходил за экран
            player_pos.x = max(40, min(SCREEN_WIDTH - 40, player_pos.x))
            player_pos.y = max(40, min(SCREEN_HEIGHT - 40, player_pos.y))            
    
    #Рисуем кружок игрока
    pygame.draw.circle(screen, "red", player_pos, 40)

    ''' if event.type == pygame.MOUSEBUTTONUP:  # Кнопка мыши отпущена
            print(f"Отпущена кнопка: {event.button}")
            print(f"Позиция: {event.pos}")
    if target_pos:
        direction = (target_pos - player_pos)
    if direction.length() < 5:
        target_pos = None
    else:
        player_pos += direction.normalize() * 300 * dt'''
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