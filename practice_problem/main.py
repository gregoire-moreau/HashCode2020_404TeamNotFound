def find_greedy(M, slice_n, indices):
    sum_ind = 0
    ind = []
    for i in range(len(indices)-1, -1, -1):
        if slice_n[indices[i]] <= M - sum_ind:
            ind.append(indices[i])
            sum_ind += slice_n[indices[i]]
    return sum_ind, ind

def find_best(M, slice_nums, improvements = 10000):
    cur_max, cur_inds = find_greedy(M, slice_nums, [i for i in range(len(slice_nums))])
    cur_inds.sort()
    for i in range(improvements):
        if (cur_max == M):
            break
        print(i)
        found = False
        for ind in reversed(cur_inds):
            v, inds = find_greedy(M + slice_nums[ind] - cur_max, slice_nums, [i for i in range(len(slice_nums)) if i not in cur_inds])
            if v > slice_nums[ind]:
                found = True
                break
        if not found:
            print("No improvements")
            break
        else:
            cur_max += v - slice_nums[ind]
            cur_inds.remove(ind)
            cur_inds += inds
            cur_inds.sort()
    return sorted(cur_inds)

def check(slice_num, indices, M):
    sum_slices = 0
    for ind in indices:
        sum_slices += slice_num[ind]
    if sum_slices <= M and len(set(indices)) == len(indices):
        print("Correct submission")
    else:
        print("Error somewhere")

if __name__ == '__main__':
    FILE = 'e_also_big'
    with open('input/'+FILE+'.in', 'r') as f:
        first_line = f.readline().strip().split()
        M = int(first_line[0])
        N = int(first_line[1])
        slice_nums = [int(a) for a in f.readline().strip().split()]
    indices = find_best(M, slice_nums)
    check(slice_nums, indices, M)
    with open('out/'+FILE+'.out', 'w') as f:
        f.write('%d\n'% len(indices))
        for ind in indices:
            f.write('%d '%ind)
        f.write('\n')
