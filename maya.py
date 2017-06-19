#maya
NUM = input("#: ")
try:
	num = int(NUM)
	number = NUM
except ValueError:
	if NUM == "random":
		import random
		randomness = int(raw_input("Degree "))
		num = random.randint(1,10**randomness)
		number = num
base = 20
basePower = 0
count = 0
alive = True
done = False
ans = []

while True:
	if num-(base**basePower) <= 0:
		#print "bP", basePower
		break
	elif num-(base**basePower) > 0:
		basePower +=1
		
#print basePower, "places"
bp = basePower-1

while True:
	for i in range(base):
		#find digit
		#print "num", str(num)
		num -= base**bp
		if num >= 0:
			#print "next"
			count +=1
		else:
			#print "abort!"
			num += base**bp
			bp -= 1
			#print "take             XXX ", count
			ans.append(count)
			break
	#kill switch
	if bp == -1:
		#print "diediedie"
		break
	else:
		count = 0

#print str(ans)
#Done! now to show it...
import pygame
screen = pygame.display.set_mode((128,128*basePower))
screen.fill((255,255,255))
shell = pygame.image.load("shell.png")
stick = pygame.image.load("stick.png")
rock = pygame.image.load("rock.png")
ypos = (128*basePower)

for i in range(basePower):
	digit = ans[-1]
	
	
	if digit == 0:
		ypos -= 128
		screen.blit(shell, (0,ypos))
		
	else:
		sticks = int(digit/5)
			
		for i in range(sticks):
			ypos -=32
			screen.blit(stick, (0,ypos))
		ypos -=32
		
		rocks = digit%5
		if rocks == 0:
			rocky = 0
		else:
			rocky = 1
		xpos = 0
		for i in range(rocks):
			screen.blit(rock, (xpos,ypos))
			xpos+=32
		
		ypos -= (4-sticks-rocky)*32 

					
	ans = ans[0:-1]
	
	
name = str(number)+".png"		
pygame.display.flip()	
pygame.image.save(screen, name)
#input("die")