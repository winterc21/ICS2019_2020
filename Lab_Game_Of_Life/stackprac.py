import cv2
import numpy as np

L = 3


r = np.random.randint(10, size=(L,L))


# ~ print(r)

a = np.random.randint(10, size=(L,L))
b = np.random.randint(10, size=(L,L))

print(a)
print('\n\n')
print(b)

c = np.stack((a,b),axis=0)

print('\n\n')

print(c)

print(np.sum(c, axis=0))


# ~ d = c==r

# ~ print(c!=0)

# ~ print(c[0,:,:])

# ~ print(np.sum(d.astype(int), axis=0))
