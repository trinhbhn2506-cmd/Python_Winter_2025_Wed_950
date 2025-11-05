l1 = [1, 2, 3, 0] # - list
l2 = [4, 5, 6, 9]
l3 = (7, 8, 9, 0)

l2D = [l1, l2, l3]
print(l2D)
print(l2D[1][2])

print('----------')
for row in l2D:
    #print(row)
    for el in row:
        print(el, end='\t')
    print()
#TODO - create functions to
# sum_rows of a 2D list,
# sum_cols of a 2D list,
# sum all values

def sum_rows(l2D):
    return [sum(row) for row in l2D]
def sum_cols(l2D):
    return [sum(col) for col in zip(*l2D)]
def sum_all(l2D):
    return sum(sum(row) for row in l2D, sum(col) for col in zip(*l2D) )

print(sum_rows(l2D))
print(sum_cols(l2D))
print(sum_all(l2D))