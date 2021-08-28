import math
import math as m
from math import sqrt
from math import sqrt as mysqrt

import time



if __name__ == '__main__':
    t0 = time.time()
    print(math.sqrt(3.7))
    print(m.sqrt(3.7))
    print(sqrt(3.7))
    print(mysqrt(3.7))
    t1 = time.time()

    print(f"Elapsed duration in many sqrt(s) is {t1 - t0} sec")
