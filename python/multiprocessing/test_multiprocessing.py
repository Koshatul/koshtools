#################################################
# test_multiprocessing.py
# Test multiprocessing library in python
#
# Copied From: http://stackoverflow.com/questions/18640334/testing-python-multiprocessing-pool-code-with-nose
# Author: aaron
#
# Execute: python test_multiprocessing.py
# Expected: no output
# Error: Displayed trace and 
#   "ImportError: This platform lacks a functioning sem_open implementation, therefore, the required synchronization primitives needed will not function, see issue 3770."
#

import multiprocessing as mp


def f(i):
    return i ** 2


pool = mp.Pool()
out = pool.map(f, range(10))


def test_pool():
    """Really simple test that relies on the output of pool.map.
    The actual tests are much more complicated, but this is all
    that is needed to produce the problem."""
    ref_out = map(f, range(10))
    assert out == ref_out

if __name__ == '__main__':
    test_pool()
