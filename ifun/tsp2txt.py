import tsplib95
import pandas
import sys

in_problem = tsplib95.load('./ch130.tsp')

sys.stdout = open('Output_content.txt', 'w')
print(in_problem)
sys.stdout.close()

