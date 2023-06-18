

import math

def get(x):
    r=math.exp(math.log(x)/2)
    fr=math.floor(r)
    if fr*fr==x:
        return fr
    else:
        return fr


k=int(input())
print(get(k))
