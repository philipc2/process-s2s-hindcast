from cfg import *


var = ['ts']

for v in covariates:
    for y in years:
        for m in months_n:
            print(vym_str.format(v,y,m))
