import cv2
import numpy
from reader import UMatFileVideoStream
from random import seed, randint

from transfigurator import Transfigurator
from listgenerator import ListGenerator

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
        # for i in range(1, perms):
        #     ts[i*4] = randint(1, matrix.shape[0]-1)
        #     ts[i*4+1] = randint(1, matrix.shape[0]-1)
        #     matrix[[ts[i*4], ts[i*4+1]],:] = matrix[[ts[i*4+1], ts[i*4]],:]
        #     ts[i*4+2] = randint(1, matrix.shape[1]-1)
        #     ts[i*4+3] = randint(1, matrix.shape[1]-1)
        #     matrix[:,[ts[i*4+2], ts[i*4+3]]] = matrix[:,[ts[i*4+3], ts[i*4+2]]]
        lg = ListGenerator(seed, matrix)
        tf = Transfigurator(lg)
        tf.encode(matrix)
        cv2.imshow('encoded', matrix)
        # for i in range(perms-1, 0, -1):
        #     matrix[:,[ts[i*4+2], ts[i*4+3]]] = matrix[:,[ts[i*4+3], ts[i*4+2]]]
        #     matrix[[ts[i*4], ts[i*4+1]],:] = matrix[[ts[i*4+1], ts[i*4]],:]
        tf.decode(matrix)
        cv2.imshow('decoded', matrix)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    stream.stop()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()