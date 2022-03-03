import matplotlib.pyplot as plt
import numpy as np
import math

# === Settings ===
sigfigs = 4

# === Constants ===

# === Conversion Factors ===
micronToAngstrom = (10**4)

# # === He-Ne Wavelength Calculation ===
backgroundCounts = [50,63,60,70,52,53,71,68,69,76,63,60,64,63,57,51,57,58,74,64,55,61,64,64,54,68,59,64,51,60]

averageBackgroundCount = round(sum(backgroundCounts)/len(backgroundCounts),2)

totalCounts = [
                [1064,945,866,717,682,632,511,533,429,405,373,343,298,274,230,218,187,201,178,147,130,143,133,121,97,108,89,84,104,99,107,80,79,81,80,66,77,83,65,84,82,70,66],
                [1165,995,908,821,737,615,580,529,409,407,397,288,274,276,278,217,214,221,168,144,183,164,165,133,127,117,111,94,109,96,80,87,82,87,80,76,75,63],
                [1087,1057,966,831,741,650,581,510,489,440,384,352,310,259,246,250,210,189,202,200,181,137,106,126,120,123,102,98,109,90,103,85,132,83,86,68,86,77,98,74,60,66]]

subtractedCounts = [[],[],[]]

for t in range(len(totalCounts)):
    for c in range(len(totalCounts[t])):
        subtractedCounts[t].append(totalCounts[t][c]-averageBackgroundCount)

print("avg background count",averageBackgroundCount)
for trial in subtractedCounts:
    print("Trial:",trial)