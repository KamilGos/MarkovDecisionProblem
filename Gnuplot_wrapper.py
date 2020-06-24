import PyGnuplot as gp
from copy import deepcopy

class Gnuplot:

    def __init__(self, World):
        self.world = World
        self.data = []
        for i in range(self.world.nStates):
            self.data.append([i + 1])

    def showData(self):
        print(self.data)

    def addValue(self, column, value):
        self.data[column].append(value)

    def saveDataToDat(self, filename):
        const_values = self.world.stateForbiddenIndexes + self.world.stateTerminalsIndexes
        filename = filename + ".dat"
        tmp_data = []
        for i in range(self.world.nStates):
            if i + 1 not in const_values:
                tmp_data.append(self.data[i])
        self.data = deepcopy(tmp_data)
        gp.s(self.data, filename)

    def plotDataDat(self, filename, iter):
        filename = filename + ".dat"
        cols = self.world.nStates - (len(self.world.stateTerminalsIndexes) + len(self.world.stateForbiddenIndexes))
        command = "plot for [col=1:" + str(
            cols) + "] \"" + filename + "\" using 0:col with lines title columnheader lw 2"
        title_command = 'set title \'Iterations = ' + str(iter) + '\' font\'{,20}\''
        gp.c(title_command)
        gp.c('set xlabel \'Iterations\' font\'{,20}\'')
        gp.c('set ylabel \'Value\' font\'{,20}\'')
        gp.c('set tics font \',10\'')
        gp.c('set key font \',20\'')
        gp.c('set grid')
        gp.c('set key right bottom')
        gp.c(command)

    def plotDataPlot(self, filename='tmp'):
        filename = filename + '.plot'
        gp.c('load \'' + filename + '\'')

    def generateGnuplotPlotFile(self, filename, iter):
        file = open(filename + ".plot", 'w')
        file.write('set title \'Iterations = ' + str(iter) + '\' font\'{,20}\'' + '\n')
        file.write('set xlabel \'Iterations\' font\'{,20}\'' + '\n')
        file.write('set ylabel \'Value\' font\'{,20}\'' + '\n')
        file.write('set tics font \',10\'' + '\n')
        file.write('set key font \',20\'' + '\n')
        file.write('set grid' + '\n')
        file.write('set key right bottom' + '\n')
        cols = self.world.nStates - (len(self.world.stateTerminalsIndexes) + len(self.world.stateForbiddenIndexes))
        file.write("plot for [col=1:" + str(
            cols) + "] \"" + filename + ".dat\" using 0:col with lines title columnheader lw 2" + '\n')
