import conway_module
import time

w = int(input("Enter width of the board"))
h = int(input("ENter height of the board"))
cycle = int(input("Enter how many time cycles you need"))
state = [...]

for j in range (0,cycle):
	state = conway_module.conway_game(j, (w,h), state)
	j += 1
	time.sleep(1)

	


