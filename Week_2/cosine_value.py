import numpy as np 

N = 8
for i in range(8):
    print(f"\ni = {i}")
    for x in range(8):
        print(f"x = {x}, cosine: {np.cos(((2*x+1)*i*np.pi)/(2*N))}")