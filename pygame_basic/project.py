# Project) 오락실 Pang 게임 만들기

# [게임 조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료 (실패)
# 8. FPS 는 30 으로 고정 (필요 시 speed 값을 조정)

# [게임 이미지]
# 1. 배경: 640 * 480(가로 세로) - background.png
# 2. 무대: 640 * 50 - stage.png
# 3. 캐릭터 : 60 * 33 - charater.png
# 4. 무기 : 20 * 430 - weapon.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png
import random
import pygame 
##################################################
# 기본 초기화 (반드시 해야하는 것)
pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clock = pygame.time.Clock()
##################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\차윤범\\Desktop\\Advanced_Python\\pygame_basic\\background.png")

#캐릭터 만들기
character= pygame.image.load("C:\\Users\\차윤범\\Desktop\\Advanced_Python\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기
ddong = pygame.image.load("C:\\Users\\차윤범\\Desktop\\Advanced_Python\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10


running = True 
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

#캐릭터가 100만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼 10*10 = 100
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5 * 20 = 100
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos =random.randint(0, screen_width - ddong_width)

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()


