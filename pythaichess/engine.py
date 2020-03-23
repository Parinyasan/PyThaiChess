import numpy as np

class Thaichess:
    def __init__(self):
        self.khun_white = 'Kw'
        self.khun_black = 'Kb'
        self.khon_white = 'kw'
        self.khon_black = 'kb'
        self.ma_white = 'Mw'
        self.ma_black = 'Mb'
        self.met_white = 'mw'
        self.met_black = 'mb'
        self.rua_white = 'rw'
        self.rua_black = 'rb'
        self.biagai_white = 'Bw'
        self.biagai_black = 'Bb'
        self.bia_white = 'bw'
        self.bia_black = 'bb'

        self.board = np.chararray((8, 8), itemsize=2)

    def reset(self):
        self.board[:] = '__'
        self.board[0] = [self.rua_black, 
                         self.ma_black, 
                         self.khon_black, 
                         self.met_black, 
                         self.khun_black, 
                         self.khun_black,
                         self.ma_black,
                         self.rua_black]
        self.board[-1] = [self.rua_white, 
                         self.ma_white, 
                         self.khon_white, 
                         self.met_white, 
                         self.khun_white, 
                         self.khun_white,
                         self.ma_white,
                         self.rua_white]
        self.board[2] = self.bia_black
        self.board[-3] = self.bia_white

    def print(self):
        print(self.board)


if __name__ == '__main__':
    chess = Thaichess()
    chess.reset()
    chess.print()
