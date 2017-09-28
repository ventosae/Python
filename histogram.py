from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

shots = [0,1,2,3,4]
bins =[0.006,0.06,0.244,0.418,0.27]
##[0.006,0.06,0.244,0.418,0.27]

plt.bar(shots, bins)
blue_patch = mpatches.Patch(color='blue', label='probability')

plt.xlabel('shots')
plt.ylabel('probability')
plt.title('task 1')
plt.legend(handles=[blue_patch])
plt.show()
