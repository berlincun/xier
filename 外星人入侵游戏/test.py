import pygame
import sys
import random

a=0
b=1

# 初始化游戏
pygame.init()

# 设置游戏窗口尺寸
screen = pygame.display.set_mode((1446, 777))

# 创建时钟对象
clock = pygame.time.Clock()

# 加载飞船图像
ship_image = pygame.image.load('D:/vscode/Microsoft VS Code/实验/ship.png')
ship_rect = ship_image.get_rect()
ship_rect.left = 50  # 将飞船放在屏幕左侧
ship_rect.centery = screen.get_rect().centery  # 居中垂直位置

# 设置飞船移动速度
ship_speed = 5

# 设置子弹属性
bullet_image = pygame.image.load('D:/vscode/Microsoft VS Code/实验/bullet.png')
bullet_rect = bullet_image.get_rect()
bullet_speed = 7
bullets = []
last_bullet_time = 0  # 上次射击子弹的时间

# 设置外星人属性
alien_image = pygame.image.load('D:/vscode/Microsoft VS Code/实验/alien.png')
alien_speed = 1
aliens = []
alien_direction = -1  # 外星人移动方向，-1表示向左移动

# 设置游戏结束标志
game_over = False

# 创建外星人
alien_gap = 800  # 外星人前后左右的间隔
alien_width = alien_image.get_width()
alien_height = alien_image.get_height()
aliens_top = random.randint(0, 777 - alien_height)  # 外星人初始位置随机
alien_creation_count = 0  # 计数器，记录已经创建的外星人数量

# 加载开始界面背景和按钮图像
start_bg = pygame.image.load('D:/vscode/Microsoft VS Code/实验/start_bg.jpg')
play_button = pygame.image.load('D:/vscode/Microsoft VS Code/实验/play_button.png')

# 加载结束界面背景和按钮图像
end_bg = pygame.image.load('D:/vscode/Microsoft VS Code/实验/end_bg.jpg')
try_again_button = pygame.image.load('D:/vscode/Microsoft VS Code/实验/try_again_button.png')
exit_button = pygame.image.load('D:/vscode/Microsoft VS Code/实验/exit_button.png')

# 加载星星图片
star_image = pygame.image.load('D:/vscode/Microsoft VS Code/实验/star.png')
stars = []

# 读取最高分
def read_high_score():
    try:
        with open('high_score.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

# 保存最高分
def save_high_score(score):
    with open('high_score.txt', 'w') as file:
        file.write(str(score))

# 添加开始界面
start_screen = True
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 620 <= x <= 870 and 650 <= y <= 700:  # 按钮范围
                start_screen = False  # 点击按钮后开始游戏

    screen.blit(start_bg, (0, 0))  # 绘制开始界面背景
    screen.blit(play_button, (620, 650))  # 绘制play按钮
    pygame.display.flip()

score = 0
level = 1
high_score = read_high_score()  # 读取最高分

# 游戏循环
while not game_over or b==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship_rect.x += ship_speed
    if keys[pygame.K_UP]:  # 上移
        ship_rect.y -= ship_speed
    if keys[pygame.K_DOWN]:  # 下移
        ship_rect.y += ship_speed

    # 控制飞船不能飞出屏幕
    if ship_rect.top < 0:
        ship_rect.top = 0
    if ship_rect.bottom > 777:
        ship_rect.bottom = 777

    # 射击子弹
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - last_bullet_time > 300:
        new_bullet = bullet_rect.copy()
        new_bullet.center = ship_rect.center
        bullets.append(new_bullet)
        last_bullet_time = current_time

    # 移动子弹
    for bullet in bullets:
        bullet.x += bullet_speed
        if bullet.right > 1446:
            bullets.remove(bullet)

    # 创建外星人
    if len(aliens) < 5 and alien_creation_count < 3:
        new_alien = {'image': alien_image, 'rect': alien_image.get_rect()}
        new_alien['rect'].right = 1446  # 外星人从屏幕右侧出现
        new_alien['rect'].y = random.randint(0, 777 - alien_height)  # 外星人初始位置随机
        aliens.append(new_alien)
        alien_creation_count += 1

    # 移动外星人
    for alien in aliens:
        alien['rect'].x += alien_speed * alien_direction
        if alien['rect'].right < 0:
            aliens.remove(alien)
            alien_creation_count -= 1

    # 检测飞船是否碰到外星人
    for alien in aliens:
        if ship_rect.colliderect(alien['rect']):
            game_over = True

    # 检测子弹是否击中外星人
    for bullet in bullets:
        for alien in aliens:
            if bullet.colliderect(alien['rect']):
                bullets.remove(bullet)
                aliens.remove(alien)
                alien_creation_count -= 1
                score += 10
                a += 1# 击中外星人得10分

    # 每获得50分，外星人移动速度加一，飞船速度加一，等级加一
    if score % 50 == 0 and score > 0 and a==5:
        alien_speed += 1
        ship_speed += 1
        level += 1
        a=0
    # 生成星星
    if len(stars) < 30:
        x, y = random.randint(0, 1446), random.randint(0, 777)
        stars.append((x, y))

    # 检查是否刷新最高分
    if score > high_score:
        high_score = score
        save_high_score(high_score)

    # 绘制游戏界面
    screen.fill((0, 0, 0))  # 设置背景色为黑色
    screen.blit(ship_image, ship_rect)  # 绘制飞船
    for bullet in bullets:
        screen.blit(bullet_image, bullet)  # 绘制子弹
    for alien in aliens:
        screen.blit(alien['image'], alien['rect'])  # 绘制外星人
    for star in stars:
        screen.blit(star_image, star)  # 绘制星星
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # 显示分数
    level_text = font.render("level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (10, 50))  # 显示等级
    high_score_text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(high_score_text, (10, 100))  # 显示最高分
    pygame.display.flip()
    clock.tick(60)

    # 游戏结束画面
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 150 <= x <= 270 and 250 <= y <= 360:  # try again按钮范围
                    game_over = False  # 点击try again按钮重新开始游戏
                    # 重置游戏
                    ship_rect.left = 50
                    ship_rect.centery = screen.get_rect().centery
                    bullets = []
                    aliens = []
                    alien_creation_count = 0
                    score = 0
                    level = 1
                    alien_speed = 1
                    ship_speed = 5
                    
                elif 125 <= x <= 325 and 550 <= y <= 630:  # exit按钮范围
                    b=0
                    pygame.quit()
                    sys.exit()

        screen.blit(end_bg, (0, 0))  # 绘制结束界面背景
        screen.blit(try_again_button, (150, 250))  # 绘制try again按钮
        screen.blit(exit_button, (125, 550))  # 绘制exit按钮
        high_score_text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
        screen.blit(high_score_text, (10, 50))  # 显示最高分
        pygame.display.flip()
