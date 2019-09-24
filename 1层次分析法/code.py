import json
import numpy as np
from pyahp import parse

# 一致性检验的范围 在method 第41行进行修改
from pyahp.methods import method


with open('matrix.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
print("B:"+str(priorities))



