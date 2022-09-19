import tsplib95
import pandas
import sys

path = './ch130.tsp'
in_problem = tsplib95.load(path)

sys.stdout = open('Output_content.txt', 'w')
print(in_problem)
sys.stdout.close()

