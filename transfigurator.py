from listgenerator import ListGenerator

class Transfigurator:
    def __init__(self, list_generator):
        self.list_gen = list_generator
    
    def encode(self, frame_matrix):
        perms = self.list_gen.generate()
        for c in range(0,3): # RGB
            for i in range(0, perms.length+1, 4):
                #TODO color encoding
                frame_matrix[perms[c][i][0], perms[c][i][1],:] = frame_matrix[perms[c][i][1], perms[c][i][0],:]
                frame_matrix[:,perms[c][i][2], perms[c][i][3]] = frame_matrix[:,perms[c][i][3], perms[c][i][2]]
        return frame_matrix

    def decode(self, frame_matrix):
        perms = self.list_gen.generate()
        for c in range(0,3): # RGB
            for i in range(perms.length, -1, -1):
                #TODO color encoding
                frame_matrix[:,perms[c][i][2], perms[c][i][3]] = frame_matrix[:,perms[c][i][3], perms[c][i][2]]
                frame_matrix[perms[c][i][0], perms[c][i][1],:] = frame_matrix[perms[c][i][1], perms[c][i][0],:]
        return frame_matrix
