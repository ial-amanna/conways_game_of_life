import numpy as np
import time
import argparse

class Board(object):
   def __init__(self, size, seed = 'Random'):
      if seed == 'Random':
         self.state = np.random.randint(2, size = size)
      self.work = Work(self)
      self.iteration = 0
   def display_at_prompt(self):
      i = self.iteration
      while i<10: #runs for 10 life cycles, if more are needed, change this or remove this check
         i += 1
         self.work.applyRules()
         print('Life Cycle: {} Birth: {} Survive: {}'.format(i, self.work.born, self.work.survived))
         yield self #if output is needed one at a time this statement is needed, else if all at once is required, remove this


class Work(object):
   def __init__(self, board):
      self.state = board.state
   def countNeighbors(self):
      state = self.state
      n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
          state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
          state[2:,1:-1] + state[2:,2:])
      return n
   def applyRules(self):
      n = self.countNeighbors()
      state = self.state
      birth = (n == 3) & (state[1:-1,1:-1] == 0)
      survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)
      state[...] = 0
      state[1:-1,1:-1][birth | survive] = 1
      born = np.sum(birth)
      self.born = born
      survived = np.sum(survive)
      self.survived = survived
      return state


#main program - in command line - specify the arguments
def main():
   ap = argparse.ArgumentParser(add_help = False)
   ap.add_argument('-h','--height', help = 'Board Height', default = 100)
   ap.add_argument('-w','--width', help = 'Board Width', default = 100)
   args = vars(ap.parse_args()) 
   bHeight = int(args['height'])
   bWidth = int(args['width'])
   board = Board((bHeight,bWidth))
   for _ in board.display_at_prompt():
      time.sleep(1)
      pass


if __name__ == '__main__':
	try:
		main()
	except:
		KeyboardInterrupt()
