import numpy as np

def interpolate(color_arr, mul):
    pat_num = int(color_arr[:, 1].size) #初期色数
    print("pat_num: "+ str(pat_num))
    ret_arr = np.empty((0,3), int)

    for i in range(pat_num-1):
        dif = (color_arr[i+1] - color_arr[i] )/mul
        print(dif)
        for j in range(mul):
            col_tmp = (int(color_arr[i,0] + j*dif[0]), int(color_arr[i,1] + j*dif[1]),int(color_arr[i,2] + j*dif[2]))
            print(col_tmp)
            ret_arr = np.append(ret_arr, np.array([col_tmp]), axis=0)
            print("ret_array: " + str(ret_arr))

    print("ret_array: " + str(ret_arr.size))
    return ret_arr
