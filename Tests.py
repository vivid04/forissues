import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dirs = ['../Out/sage', '../Out/KLEE', '../Out/PP-CASE']
solvers = ['z3', 'stp', 'boolector', 'ppbv']
colors = ['g', 'c', 'b', 'r', 'y']
markers = ['x', '^', 's', 'o', '+']


def original_cumsum():
	df = pd.DataFrame(pd.read_csv('dircolors.csv'))
	df.cumsum().plot()
	plt.savefig('expected.png')


# cumsum with step
def time_sovled(data):
	df = pd.DataFrame(data)
	rows, columns = df.shape
	X = np.linspace(0, rows, 51)
	X = [int(x) for x in X]
	cumsum = []
	for x in X:
		cumsum.append(df.loc[:x].sum())

	d = pd.DataFrame(cumsum)
	for solver in solvers:
		index = solvers.index(solver)
		ax = d[solver].plot(color=colors[index], marker=markers[index], markersize=3)
		ax.set_xticklabels(X)
	plt.savefig('output.png')

original_cumsum()
# time_sovled(pd.read_csv('dircolors.csv'))
plt.show()