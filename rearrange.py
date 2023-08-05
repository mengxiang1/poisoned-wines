import numpy as np

file = "9_17.txt"
BINLENGTH = 9

def np_to_hex():
    pass

def rearrange(arr):
    
    def count_ones(value):
        return value.count('1')
    def sum_values(value):
        return np.sum(value)
    arr = [format(i, f'0{BINLENGTH}b') for i in arr]
    arr = sorted(arr, key=lambda x: (count_ones(x), arr.index(x)))
    arr = np.array([list(map(int, j)) for j in [list(i) for i in arr]])
    arr = np.rot90(arr)
    sorted_indices = np.argsort(np.apply_along_axis(sum_values, 1, arr))
    arr = arr[sorted_indices]


    indexRef = []
    for i in arr:
        i = [str(j) for j in i]
        indexRef.append(int("".join(i), 2))
    indexRef = np.array(indexRef)
    indices = indexRef.argsort()
    arr = arr[indices]
    arr = np.rot90(arr, -1)
    return(np.ndarray.tolist(arr))

def verify(arrs):
    arr_list = []
    for arr in arrs:
        arr_list.append(rearrange(arr))
    for i in range(len(arr_list)):
        print(f"Array {i}'s base form: \n{np.array(arr_list[i])}\nHex form: {' '.join([hex(int(''.join([str(k) for k in j]), 2))[2:] for j in np.array(arr_list[i])])}\n")

    unique_list = []

    for x in arr_list:
        if x not in unique_list:
            unique_list.append(x)

    return len(unique_list) == 1

def main():
    combs = [list(map(lambda a: int(a, 16), j)) for j in [i.split(" ") for i in open(file).read().splitlines()]]
    print(verify(combs))

if __name__ == "__main__":
    main()