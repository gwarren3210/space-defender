import matplotlib.pyplot as plt
import numpy as np
import sys

file = sys.argv[1]
#file = input('')       # tesing input
#file = "game1.txt"     # testing the rest of the code

lines = np.loadtxt(file)      # loading the file

# init list for each alien
rd = []
gn = []
bl = []
gy = []

# appending the lists from each given line
for line in lines:
    rd.append(int(line[0]))
    gn.append(int(line[1]))
    bl.append(int(line[2]))
    gy.append(int(line[3]))

# plotting each line
plt.plot(rd,"^-r")
plt.plot(gn,'^-g')
plt.plot(bl,"*-b")
plt.plot(gy,'s-k')

# labels
plt.title(str(file)+" Statistics on Aliens Shot")
plt.xlabel("time steps")
plt.ylabel("# Aliens shot")
plt.legend(["red", "green", "blue", "space ship"])

# showing plot
plt.show()