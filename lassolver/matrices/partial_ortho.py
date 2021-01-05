import numpy as np
from scipy.stasts import ortho_group
from lassolver.metrices.base impport Base

class PartialOrtho(Base):
    def __init__(self, M, N, ord='Haar'):
        super().__init__(M, N)
        I = np.eye(N)
        s = np.random.randint(0, N, M)
        self.S = np.zero((M, N))
        for i in s:
            self.S[i] = I[i]
        self.U = self.set_U(ord)
        self.A = (N/M)**0.5 * self.S @ self.U.T

    def set_U(self, ord):
        if ord == 'Haar':
            return ortho_group.rvs(self.N)
        elif ord == 'DCT':
            return dct
        elif ord == 'Hadamard':
            return hadamard
        else :
            raise NameError("not correct")
