import numpy as np

def sort_2d_array(arr_2d):
    sorted_2d = []
    for sub_arr in arr_2d:
        int_arr = np.array([int(s, 2) for s in sub_arr])
        sorted_indices = np.lexsort((int_arr, np.char.count(sub_arr, '1')))
        sorted_sub_arr = sub_arr[sorted_indices]
        sorted_2d.append(sorted_sub_arr)
    return np.array(sorted_2d)


arr = np.array([['100000000', '011000000', '000110000', '000001100', '100000011', '000101010',
     '010000110', '001000101', '000011001', '001010010', '010100001', '110100100',
     '101001010', '001101100', '110001001', '010011100', '101010100']])

print(sort_2d_array(arr))