from pyahp.methods import EigenvalueMethod
import numpy as np

class MatrixModel:
    def __init__(self, model, solver=EigenvalueMethod):
        self.solver = solver()
        self.preference_matrices = model['preferenceMatrices']

    def get_weights(self):

        matrix = np.array(self.preference_matrices['matrix'])
        print("输入矩阵如下:")
        print(matrix)
        weights = self.solver.estimate(matrix)

        return weights