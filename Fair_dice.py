from itertools import product
import numpy as np
from Fair_coin import cond_prob

omega = set(product([1, 2, 3, 4, 5, 6], repeat=5))

A = {om for om in omega if np.sum(om) % 3 == 0}
B = {om for om in omega if np.prod(om) > 500}

print(cond_prob(B, A))
