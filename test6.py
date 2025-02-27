#program is used to count mississipis in hide-and-seek
import time
mississippi = 1
for mississippi in range(6):
    print(mississippi, " Mississippi")
    time.sleep(1)
    mississippi += 1
    if mississippi == 6:
        print("Ready or not, here I come")