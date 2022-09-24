from listgenerator import ListGenerator

class Transfigurator:
    def __init__(self, list_generator):
        self.list_gen = list_generator
    
    def encode(self, frame_matrix):
        perms = self.list_gen #TODO swap to true frame array
        for i in range(0, perms.length+1, 4):
            #TODO color encoding
            frame_matrix[[perms[i], perms[i+1]],:] = frame_matrix[[perms[i+1], perms[i]],:]
            frame_matrix[:,[perms[i+2], perms[i+3]]] = frame_matrix[:,[perms[i+3], perms[i+2]]]
        return frame_matrix

    def decode(self, frame_matrix):
        perms = self.list_gen
        for i in range(perms.length, -1, -4):
            #TODO color encoding
