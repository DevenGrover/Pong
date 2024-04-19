#sounds , menu option , score display , reset-start mechanism 
import pygame
import time
pygame.init()
s=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Collision")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
color=(0,0,0)
coord_a=60
coord_b=80
coord_x=940
coord_y=80
ball_obj = pygame.draw.circle(surface=s,color=(255,0,0), center=[100, 100], radius=40)
speed = [1,1]
running=True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        print("S")
        if coord_b<=490:
            coord_b+=1
    if keys[pygame.K_w]:
        print("W")
        if coord_b>=10:
            coord_b-=1
    if keys[pygame.K_DOWN]: 
        print("DOWN")
        if coord_y<=490:
            coord_y+=1
    if keys[pygame.K_UP]: 
        print("UP")
        if coord_y>=10:
            coord_y-=1

    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         print("Key W has been pressed")
        #         coord_y-=12
        #     if event.key == pygame.K_s:
        #         print("Key S has been pressed")
        #         coord_y+=12
        # if event.key == pygame.K_a:
        #     print("Key A has been pressed")
        #     coord_x-=12
        # if event.key == pygame.K_d:
        #     print("Key D has been pressed")
        #     coord_x+=12
        if event.type == pygame.QUIT:
            running=False
    s.fill(color)
    ball_obj = ball_obj.move(speed)
    if ball_obj.centerx>=950:
        break
    if ball_obj.centerx<=50:
        break
    if ball_obj.left <= 0 or ball_obj.right >= 1000:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= 600:
        speed[1] = -speed[1]
    #Collision starts here
    if ball_obj.centerx==90:
        if ball_obj.centery>=coord_b and ball_obj.centery<=coord_b+100:
            speed[0] = -speed[0]
    if ball_obj.centerx==930:
        if ball_obj.centery>=coord_y and ball_obj.centery<=coord_y+100:
            speed[0] = -speed[0]
    pygame.draw.circle(surface=s, color=(255,0,0),center=ball_obj.center, radius=15)
    pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_x,coord_y, 20, 100))
    pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_a,coord_b, 20, 100))
    pygame.display.flip()
    time.sleep(0.001)
    print(ball_obj.centery)
print("GAME OVER")