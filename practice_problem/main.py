

with open('a_example.in', 'r') as f:
    first_line = f.readline().strip().split()
    M = int(first_line[0])
    N = int(first_line[1])
    slice_nums = [int(a) for a in f.readline().strip().split()]