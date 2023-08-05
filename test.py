import numpy as np
import csv

open("output.csv", "w").write("")

with open("9_17.txt") as f:
    content = f.read()
    # Max value and length of binary 
    maxNum = max([int(i, base=16) for i in content.replace("\n", " ").split(" ")])
    binLength = len(bin(maxNum)[2:])

    # Split content into numpy binary array
    arr = []
    for i ,line in enumerate(content.split("\n")):
        arr.append([])
        for value in line.split(" "):
            arr[i].append(format(int(value, base=16), f'0{binLength}b'))
    arr = np.array(arr)

def sort_binary_array(arr_2d):
    sorted_2d = []
    for sub_arr in arr_2d:
        int_arr = np.array([int(s, 2) for s in sub_arr])
        sorted_indices = np.lexsort((int_arr, np.char.count(sub_arr, '1')))
        sorted_sub_arr = sub_arr[sorted_indices]
        sorted_2d.append(sorted_sub_arr)
    return np.array(sorted_2d)

def sort_binary_array_vertical(binary_array):
    sorted_subarrays = []
    for subarray in binary_array:
        # Convert the binary subarray into a vertical grid
        vertical_grid = np.array([list(binary_string) for binary_string in subarray])
        # Merge the individual digits vertically
        merged_vertical = [''.join(vertical_grid[:, i]) for i in range(vertical_grid.shape[1])]
        # Sort the merged subarray in descending order
        sorted_array = np.array(sorted(merged_vertical, reverse=True, key=lambda x: int(x, 2)))
        # Split the merged subarray back into individual digits
        split_vertical = np.array([list(binary_string) for binary_string in sorted_array])
        # Convert the vertical grid back into horizontal format
        horizontal_array = np.array([''.join(split_vertical[:, i]) for i in range(split_vertical.shape[1])])
        sorted_subarrays.append(horizontal_array)
    return np.array(sorted_subarrays)

def append_to_csv(data):
    # Convert binary strings to 2D arrays
    data_2d = []
    for subarray in data:
        subarray_2d = []
        for binary_str in subarray:
            row = [int(digit) for digit in binary_str]
            subarray_2d.append(row)
        data_2d.append(np.array(subarray_2d))

    # Combine 2D arrays horizontally and append to CSV
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in range(len(data_2d[0])):
            csv_row = []
            for subarray in data_2d:
                csv_row += subarray[row].tolist()
                csv_row.append('')
            writer.writerow(csv_row[:-1])
        writer.writerow("")


append_to_csv(arr)

# Round 1 sorting
arr = sort_binary_array(arr)
append_to_csv(arr)
for i in arr:
    i = [hex(int(j, base=2))[2:] for j in i]
    print(" ".join(i))

print("\n")
# Round 2 sorting
arr = sort_binary_array_vertical(arr)
append_to_csv(arr)
for i in arr:
    i = [hex(int(j, base=2))[2:] for j in i]
    print(" ".join(i))