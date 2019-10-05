import pygame
import random
import sys

pygame.init()

width = 800
height = 500
score = 0

screen = pygame.display.set_mode((width,height))

game_over = False
clock = pygame.time.Clock()
SPEED = 10

player_pos =  [width/2,  height-100]
BACKGROUND_COLOR = (0,0,0)
enemy_pos = [random.randint(0,width-50), 0]
enemy_list = [enemy_pos]

def add_enemy(enemy_list):
	delay = random.random()
	if len(enemy_list)<10 and delay < 0.1:
		a = random.randint(0,width-50)
		b = 0
		enemy_list.append([a,b])


def enemy_position(enemy_list,score,SPEED):
	for enemy_pos in enemy_list:
		if enemy_pos[1]>=0 and enemy_pos[1]<height:
			enemy_pos[1]+=SPEED
		else:
			enemy_pos[1]=0
			enemy_pos[0] = random.randint(0,width-50)
			score+=1
			SPEED+=0.1
	return score,SPEED


def draw_enemy(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, (0,0,255), (enemy_pos[0], enemy_pos[1], 50,50))



def enemy_collision(player_pos,enemy_list):
	for enemy_pos in enemy_list:
		if collision_check(player_pos,enemy_pos):
			return True
	return False




def collision_check(player_pos,enemy_pos):

	x= player_pos[0]
	y=player_pos[1]
	a= enemy_pos[0]
	b=enemy_pos[1]
	if(x>=a and x<(a+50)) or (x<=a and a<(x+50)):
		if(y>=b and y<(b+50)) or (y<=b and b<(y+50)):
			return True
	return False


while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_pos[0]-=50
			elif event.key == pygame.K_RIGHT:
				player_pos[0]+=50
			elif event.key == pygame.K_UP:
				player_pos[1]-=50
			elif event.key == pygame.K_DOWN:
				player_pos[1]+=50
	screen.fill(BACKGROUND_COLOR)
	add_enemy(enemy_list)
	score,SPEED = enemy_position(enemy_list,score,SPEED)
	draw_enemy(enemy_list)
	if enemy_collision(player_pos,enemy_list):
		game_over = True
		print("score: " + str(score))
		break

	clock.tick(30)
	pygame.draw.rect(screen, (255,0,0), (player_pos[0], player_pos[1], 50,50))
	pygame.display.update()
