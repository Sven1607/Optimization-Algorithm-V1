import random
import math
data_list = [[12, 17, True], [17, 27, True], [3, 30, True], [19, 24, True], [15, 12, False], [10, 17, True], [21, 14, False], [18, 25, True], [4, 27, True], [10, 11, False], [19, 16, False], [12, 8, False], [19, 21, False], [17, 29, True], [10, 25, True], [5, 21, True], [18, 19, False], [10, 13, True], [22, 28, True], [15, 11, False], [20, 18, False], [13, 25, True], [21, 15, False], [28, 23, False], [7, 5, False], [20, 12, False], [1, 29, True], [2, 25, True], [10, 22, True], [
    3, 30, True], [19, 9, False], [5, 2, False], [20, 2, False], [25, 12, False], [4, 1, False], [9, 3, False], [27, 3, False], [21, 1, False], [4, 2, False], [1, 5, True], [16, 3, False], [6, 4, False], [16, 2, False], [3, 3, False], [3, 4, False], [8, 11, True], [13, 9, False], [9, 2, False], [6, 1, False], [12, 2, False], [3, 3, False], [19, 9, False], [15, 2, False], [11, 2, False], [13, 5, False], [2, 4, True], [11, 4, False], [7, 2, False], [22, 4, False], [3, 1, False]]

bias = 0.005

w = 1 + bias
lower_bound = 0
upper_bound = 10000
c = 0
i = 0


def guess_float(min_value, max_value):
    return random.uniform(min_value, max_value)


for i in range(100):
    for point in data_list:
        x = point[0]
        y = point[1]
        v = point[2]
        result_1 = y/x

        result = result_1*w

        if result >= 1:
            con = True

        if result < 1:
            con = False

        if con == v:
            print("")
            c += 1

        elif con != v:
            i += 1
            print(con)
            p = result-1
            print(p)
            print(point)
            if con == True:
                sum = y/x
                upper_bound = .99999/sum

            if con == False:
                sum = y/x
                lower_bound = 1/sum
            print(upper_bound)
            print(lower_bound)
            w = guess_float(lower_bound, upper_bound) + bias

        print(w)

print(f"correct {c}")
print(f"incorrect {i}")
