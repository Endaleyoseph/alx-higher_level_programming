#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum1, sum2 = 0, 0
        for i in my_list:
            sum1 += i[0] * i[1]
        for j in my_list:
            sum2 += j[1]
        return sum1 / sum2
    else:
        return 0
