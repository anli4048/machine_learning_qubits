#import scqubits.testing as sctest
#sctest.run()

import numpy as np
dimension = 4
offdiag_elements = np.sqrt(range(1, dimension))
print(np.diagflat(offdiag_elements, 1))