import pygame

pygame.init()  #초기화 반드시 필요

# 화면 크기 설정
screen_width = 480       # 가로
screen_height = 640      # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JB game")  #게임 이름

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

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가
            running =False  #게임이 진행중이 아님
    
    screen.blit(background, (0,0))      # blit 백그라운드를 그려주는 역할
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()   # 화면을 프레임마다 업데이트해줘야함
     
pygame.quit()
