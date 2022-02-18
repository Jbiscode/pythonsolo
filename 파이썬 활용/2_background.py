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


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가
            running =False  #게임이 진행중이 아님
    
    screen.blit(background, (0,0))      # blit 백그라운드를 그려주는 역할
    ## background 안불러오고 screen.fill(R.G.B) 로 색깔로 채워도됌  0~255까지
    
    pygame.display.update()   # 화면을 프레임마다 업데이트해줘야함
     
pygame.quit()
