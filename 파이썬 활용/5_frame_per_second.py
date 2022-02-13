import pygame

pygame.init()  #초기화 반드시 필요
# 화면 크기 설정
screen_width = 480       # 가로
screen_height = 640      # 세로
screen = pygame.display.set_mode((screen_width,screen_height))
# 화면 타이틀 설정
pygame.display.set_caption("JB game")  #게임 이름



# FPS
clock = pygame.time.Clock()









# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\사재빈\\Desktop\pythonWorkspace\\파이썬 활용\\background.png")

# 캐릭터 (스프라이트)불러오기 sprite
character = pygame.image.load("C:\\Users\\사재빈\\Desktop\pythonWorkspace\\파이썬 활용\\character.png")
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]   #캐릭터의 가로 크기
character_height = character_size[1]  #캐릭터의 세로 크기
character_x_pos = screen_width / 2 -character_width/2  # 화면 가로의 절반 크기에 위치하게   (가로)
character_y_pos = screen_height - character_height     # 화면 세로크기 가장 아래에 위치   (세로)
                  # 좌표는 맨왼쪽 위 0,0 기준으로 움직이는거라 조정해줘야함
to_x = 0    # x좌표로 캐릭터이동
to_y = 0    # y좌표로 캐릭터이동

# 이동 속도
character_speed = 0.5

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)  #게임화면의 초당 프레임 수 설정
    #print("fps :" =str(clock.get_fps()))
    
## 캐릭터가 1초동안에 100만큼 이동해해야함
## 10FPS = 1초 동안에 10번 동작 -> 1번에 10만큼 이동
## 20FPS = 1초 동안에 20번 동작 -> 1번에 5만큼 이동
    
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가
            running =False  #게임이 진행중이 아님
    
        if event.type == pygame.KEYDOWN:   # 키 눌렸나 확인 
            if event.key == pygame.K_LEFT:   #왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  #오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP:   # 위로      #점프인데 좌표기준으로 위로가려면 마이너스해야함
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 아래로
                to_y += character_speed
        if event.type == pygame.KEYUP:     # 방향키를 떼면 멈춘다는
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  to_x = 0
             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x *dt       #위에서 움직이라는 만큼 캐릭터 위치를 정해줌
    character_y_pos += to_y *dt       # 프레임별로 이동속도에 차이가 나면 안되니까 dt값 곱해서 보정
    
    #가로 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0,0))      # blit 백그라운드를 그려주는 역할
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()   # 화면을 프레임마다 업데이트해줘야함
     
pygame.quit()
