import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

plt.ion()
plt.plot([1.4, 2.5])
plt.title(" Sample interactive plot")

axes = plt.gca()
axes.plot([3.1, 2.2])