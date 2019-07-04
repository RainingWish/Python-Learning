#Creat a tetris game

#must import:
import pygame,sys,random,time

#create blocks
all_block=[[[0,0],[0,-1],[0,1],[0,2]], #shape I
			[[0,0],[0,1],[1,1],[1,0]], #shape 0
			[[0,0],[0,-1],[-1,0],[-1,1]], #shape Z
			[[0,0],[0,1],[-1,-1],[-1,0]], #shape S
			[[0,0],[0,1],[1,0],[0,-1]], #shape T
			[[0,0],[1,0],[-1,0],[1,-1]], #shape L
			[[0,0],[1,0],[-1,0],[1,1]], #shape J

#Create Background
background=[[0 for column in range(0,10)]for row in range(0,22)]
background[0]=[1 for column in range(0,10)]

#Game Random system

select_block = list(random.choice(all_block))
block_initial_position=[21,5]
times=0
score=[0]
gameover=[]
press=False

#game setting
pygame.init()
screen=pygame.display.set_mode((250,500))

#game function
def block_move_down():
	y_drop=block_initial_position[0]
	x_move=block_initial_position[1]
	y_drop-=1
	for row,column in select_block:
		row+=y_drop
		column+=xmove
		if background[row][column]==1:
			break
	else:
		block_initial_position.clear()
		block_initial_position.extend([y_drop,x_move])

	y_drop,x_move=block_initial_position
	for row,column in select_block:
		background[y_drop+row][x_move+column]=1

	complete row=[]
	for row in range(1,21):
		if 0 not in background[row]:
			complete_row.append(row)
	complete_row.sort(reverse=True)

	for row in complete_row:
		background.pop(row)
		background.append([0 for column in range(0,10)])
	score[0]+=len(complete_row)
	pygame.display.set_caption('Tetris,Score:'+str(score[0]+'Tonymot'))

	select_block.clear()
	select_block.extend(list(random.choice(all_block)))
	block_initial_position.clear()
	block_initial_position.extend([20,5])
	y_drop,x_move=block_initial_position
	for row,column in select_block:
		row+=y_drop
		column+=xmove
		if background[row][column]==1:
			gameover.append(1)
	else:
		return

def new_draw():
	y_drop,x_move=block_initial_position
	for row,column in select_block:
		row+=y_drop
		column+=xmove
		pygame.draw.rect(screen,(255,165,0),(column*25,500-row*25,23,23))
	
	for rowin range(0,20):
		for column in range(0,10):
			bottom_block=background[row][column]
			if bottom_block:
				pygame.draw,rect(screen,(0,0,255),(column*25,500-row*25,23,23))

def move_left_right(n):
	y_drop,x_move=block_initial_position
	x_move+=n
	for row,column in select_block:
		row+=y_drop
		column+=xmove
		if column<0 or column>9 or background[row][column]:
			break
		else:
			block_initial_position.clear()
			block_initial_position.extend([y_drop,x_move])

def rotate():
	y_drop,x_move=block_initial_position
	rotating_position=[(-column,row) for row,column in select_block]
	for row,column in rotating_position:
		row+=y_drop
		column+=x_move
		if column<0 or column>9 or background[row][column]:
			break
		else:
			block_initial_position.clear()
			block_initial_position.extend(rotating_position)

while True:
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
			move_left_right(-1)
		elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
			move_left_right(1)
		elif event.type==pygame.KEYDOWN and event.key==pygame.K_UP
			rotate()
		elif event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
			press=True
		elif event.type==pygame.KEYUP and event.key==pygame.K_DOWN:
			press=Flase
	if press:
		time+=10
	if time>=50:
		block_move down()
		time=0
	else:
		time+=1

	if gameover:
		sys.exit()
	new_draw()
	pygame.time.Clock().tick(200)
	pygame.display,flip()















