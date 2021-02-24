import timeit
import numpy as np

print(timeit.timeit(setup='myArray = range(1000)', stmt='[x ** 2 for x in myArray]', number=1000))



print(timeit.timeit(setup='import numpy as np',
                    stmt='otherArray = np.arange(1000); '
                         'otherArray ** 2 ', number=1000))
