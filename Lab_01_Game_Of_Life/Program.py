import cv2
import numpy as np

live=1
liveColor=(255,0,0)
dead=1
deadColor=(0,0,0)


neighborsList = ((-1,-1), (-1,0) ,(-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))


def show(img, title="image", wait=30):
    d = np.max(img.shape)
    h,w = img.shape[:2]
    unitSize = 600//d
    resized = cv2.resize(np.uint8(img), (unitSize*w,unitSize*h), interpolation = cv2.INTER_AREA)
    cv2.imshow(title, resized)
    cv2.waitKey(wait)


def showCA(ca, wait=0):
    h,w = ca.shape[:2]
    out = np.zeros((h,w,3))

    out[ca==1]=(255,0,0)
    out[ca==0]=(0,0,0)
    show(out, wait=wait)

# ~ caInitPic = cv2.imread('CA_1.png', 0) # the 0 says to import the image in grayscale

# ~ L0 = caInitPic.shape[0] # get the height and width of the image if it's not a square
# ~ L1 = caInitPic.shape[1]

# ~ ca = np.zeros((L0,L1))


# ~ # anything closer to black than to white in the image becomes a 1. Otherwise it stays 0.
# ~ ca[caInitPic<128]=1	
# ~ ca[caInitPic>128]=0


def load(filename):
    img=cv2.imread(filename)
    h,w = img.shape[:2]
    out = np.zeros((h,w))
    out[img[:,:,1]>150]=0
    out[img[:,:,1]<100]=1
    return out


# ~ def iterate(ca):
    # ~ newCa=ca*1
    # ~ kernel=np.int16([[1,1,1],
                     # ~ [1,0,1],
                     # ~ [1,1,1]])
    # ~ whereTheLiveAre=np.int16(ca==live)
    # ~ neighborCount=cv2.filter2D(whereTheLiveAre,-1,kernel,borderType=cv2.BORDER_CONSTANT)
    # ~ newCa[ca==1]=1
    # ~ newCa[ca==0]=0
    # ~ newCa[np.logical_and(np.logical_and(ca==1,2<=neighborCount),neighborCount<=3)]=1
    # ~ return newCa    


def iterate(ca):
    newCa = ca*1
    h,w = ca.shape
    for i in range(w):
        for j in range(h):
            n = 0
            v = ca[i][j]
            for dx,dy in neighborsList:
                ti=(i+dx)%w
                tj=(j+dy)%w
                if ca[ti][tj]==1:
                    n+=1
                #look around ca[i][j] and count neighbors

            if v==1 and n<2:
                newCa[i][j]=0
            elif v==1 and n>=2 and n<=3:
                newCa[i][j]=1
            elif v==0 and n==3:
                newCa [i][j]=1
            elif v==1 and n>3:
                newCa[i][j]=0
            elif v==0 and n<3 or n>3:
                newCa [i][j]=0
    return newCa
    
# ~ ca = np.array([[0,0,0,0,0,0,0,0,0,0],
                # ~ [0,0,0,0,0,0,0,0,0,0],
                # ~ [0,0,0,0,0,0,0,0,0,0],
                # ~ [0,0,0,0,0,0,0,0,0,0],
                # ~ [0,0,0,0,0,0,0,0,0,0],
                # ~ [0,0,1,1,1,0,0,0,0,0],
                # ~ [0,1,0,0,1,0,0,0,0,0],
                # ~ [0,0,0,0,1,0,0,0,0,0],
                # ~ [0,1,0,0,1,0,0,0,0,0],
                # ~ [0,0,0,1,0,0,0,0,0,0]])


ca=load("CA_1.png")
fps=10
while True:
    showCA(ca,1000//fps)
    ca=iterate(ca)
