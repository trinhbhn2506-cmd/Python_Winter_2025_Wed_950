from time import time
from bowling_game import sum_bowls_seq, sum_bowls_loop, sum_bowls_recurs

def time_func(func, n):
    t0 = time()
    print(f'Running {func.__name__} with n={n}')
    res = func(n)
    print(f'Result={res}')
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Done in {elapsed} sec')

n = 998
#time_func(sum_bowls_seq(n), n)
time_func(sum_bowls_seq,n)
time_func(sum_bowls_loop,n)
#time_func(sum_bowls_recurs, n)