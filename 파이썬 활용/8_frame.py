import pygame
##################################################################
#####기본 초기화 (반드시 해야하는 것들)############                
pygame.init()  #초기화 반드시 필요                                 
# 화면 크기 설정                                                  
screen_width = 480       # 가로                                   
screen_height = 640      # 세로                                  
screen = pygame.display.set_mode((screen_width,screen_height))    
# 화면 타이틀 설정                                                  
pygame.display.set_caption("JB game")  #게임 이름                   
                                                                    
# FPS                                                                
clock = pygame.time.Clock()                                          
##################################################################

######## 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 이동속도, 폰트 등)

running = True
while running:
    dt = clock.tick(60)  
    
    
####### 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   
            running =False  
    
        
        
###### 3. 게임 캐릭터 위치 정의    (기본 캐릭 위치, 경계값처리 등)
    
    
###### 4. 충돌처리    


###### 5. 화면에 그리기 blit  (캐릭터,글자 등)  
    
    pygame.display.update()   # 화면을 프레임마다 업데이트해줘야함
     
pygame.quit()