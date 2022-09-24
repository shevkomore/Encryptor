import cv2
import numpy
from reader import UMatFileVideoStream
from random import seed, randint

stream = UMatFileVideoStream(0).start()

def main():
    with open("seed","r") as f:
        seed(f.readline())
   #set up variables for encryption/decryption
    perms = 300
    ts = numpy.ndarray([perms, 4], int)
    #print(ts)
    while not stream.stopped:
        frame = stream.read()
        matrix = frame.get()
        #Example encode-decode
        for i in range(0, perms):
            ts[i][0] = randint(1, matrix.shape[0]-1)
            ts[i][1] = randint(1, matrix.shape[0]-1)
            ts[i][2] = randint(1, matrix.shape[1]-1)
            ts[i][3] = randint(1, matrix.shape[1]-1)
            matrix[[ts[i][0], ts[i][1]],:] = matrix[[ts[i][1], ts[i][0]],:]
            matrix[:,[ts[i][2], ts[i][3]]] = matrix[:,[ts[i][3], ts[i][2]]]
        cv2.imshow('encoded', matrix)
    
        for i in range(perms-1, -1, -1):
            matrix[:,[ts[i][2], ts[i][3]]] = matrix[:,[ts[i][3], ts[i][2]]]
            matrix[[ts[i][0], ts[i][1]],:] = matrix[[ts[i][1], ts[i][0]],:]
        cv2.imshow('decoded', matrix)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    stream.stop()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()