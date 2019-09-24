"""
    ZDK
    获得成对比较矩阵的权重
"""
import json

from matrixmodel import MatrixModel

with open('matrix.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

matrix_model = MatrixModel(model)
print(matrix_model.get_weights())
