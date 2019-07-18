import numpy as np
import matplotlib.pyplot as plt

def LinearRegression(x, y):
	"""
	This is my stupid simple script to run linear regression in (x,y) pair vectors.
	"""
	onez = np.ones(len(x))
	X = np.c_[x, onez]
	Y = np.matrix(y).T
	C = np.linalg.inv( X.T.dot(X) ).dot(X.T*Y)
	fit = (C[0]*x+C[1]).A1
	return C, fit

class plot:
	def __init__(self, *args, lineStyle='', legendLocation='upper left', xlabel='xlabel', ylabel='ylabel', xlim='', ylim=''):
		self.args = args
		self.lineStyle = lineStyle
		self.legendLocation = legendLocation
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.xlim = xlim
		self.ylim = ylim

	def show(self, *plotArgs):
		if not plotArgs:
			plt.plot(self.args)
		else:
			plt.plot(plotArgs)
	# if( not( np.mod(len(args),2) ) ):
	# 	for ind, n in enumerate(args[0::2]):
	# 		plt.plot(args[2*ind], args[2*ind+1], label="asdasd")
	# plt.xlim((-1e-6, dftemp2['PW'].unique()[0]+1e-6))
	# plt.xlabel(self.xlabel)
	# plt.ylabel(self.ylabel)
	# plt.minorticks_on()
	# plt.grid(b=True, which='major', color='50', linestyle='-')
	# plt.grid(b=True, which='minor', color='20', linestyle='--')
	# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	# plt.legend(loc=self.legendLocation)
	# fig = plt.gcf()
	# fig.set_size_inches(12, 5)
	# plt.show()