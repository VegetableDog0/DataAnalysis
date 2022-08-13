import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

x = [113, 135, 134, 100, 128, 91, 118, 125, 113, 96, 106, 103, 150, 136, 103, 90, 91, 142, 100, 115, 104, 133, 90, 149,
     126, 138, 142, 99, 144, 116, 112, 110, 96, 100, 101, 144, 96, 124, 132, 106, 95, 113, 144, 143, 113, 104, 118, 113,
     103, 111, 101, 146, 119, 147, 137, 148, 145, 110, 100, 149, 144, 113, 144, 119, 113, 91, 148, 135, 134, 103, 132,
     138, 118, 140, 121, 92, 120, 98, 101, 151, 92, 91, 116, 142, 90, 151, 101, 138, 110, 101, 111, 114, 121, 148, 130,
     95, 97, 136, 127, 104, 139, 119, 115, 99, 150, 137, 149, 124, 143, 122, 95, 110, 109, 139, 146, 144, 146, 113, 138,
     135, 137, 146, 100, 124, 117, 113, 139, 114, 120, 97, 118, 112, 148, 93, 140, 114, 96, 138, 112, 149, 106, 100,
     101, 147, 94, 91, 133, 147, 144, 101, 119, 104, 146, 145, 122, 120, 134, 148, 141, 119, 90, 96, 138, 127, 131, 145,
     97, 137, 131, 108, 149, 109, 104, 102, 107, 129, 139, 98, 96, 142, 141, 149, 117, 104, 140, 121, 145, 113, 107,
     101, 138, 109, 146, 151, 133, 134, 94, 122, 92, 119, 143, 134, 109, 129, 91, 101, 147, 147, 150, 134, 93, 105, 129,
     103, 133, 148, 103, 132, 117, 136, 96, 113, 121, 106, 119, 119, 116, 133, 96, 132, 117, 93, 131, 140, 133, 112, 91,
     105, 127, 125, 97, 140, 124, 136, 145, 98, 148, 91, 128, 111]

plt.figure(figsize=(20, 8), dpi=100)

plt.hist(x, 30)

plt.show()
