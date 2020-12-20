import numpy as np
from scipy.stats import ortho_group
from lassolver.matrices.base import *

class UnitaryInvar(Base):
    def __init__(self, M, N, connum):
        super().__init__(M, N)
        self.kappa = connum
        self.r = kappa**(1/M)
        self.sv = self.singular_value()
        self.S = np.hstack((np.diag(self.sv), np.zeros((M, N-M)))
        self.V = ortho_group(M)
        self.U = ortho_group(N)
        self.A = self.V @ self.S @ self.U.T

    def singular_value(self):
        sv = np.array(self.N * (1 - 1/self.r) / (1 - 1/self.kappa) if self.kappa != 1 else self.N/self.M])
        for i in range(self.M-1):
            sv = np.append(self.sv, self.sv[-1] / self.r)
        return sv

    def change_condition(self, connum):
        self.kappa = connum
        self.r = kappa**(1/self.M)
        self.sv = self.singular_value()
        self.S = np.hstack(np.diag(self.sv, np.zeros((self.M, self.N - self.M)))
        self.A = self.V @ self.S @ self.U.T
