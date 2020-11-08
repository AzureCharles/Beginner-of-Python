#matrix change in simplex method

#code from https://zhuanlan.zhihu.com/p/61336821

import numpy as np
B_1 = np.matrix([[1., 0., 0.],
                 [0., 2., 0.],
                 [0., 2., 1.]])
B_1_I = B_1.I
print("B_1_I")
print(B_1_I)
print("\n")

B_2 = np.matrix([[1., 0., 1.],
                 [0., 1., 0.],
                 [0., 0., 3.]])
B_2_I = B_2.I
print("B_2_I")
print(B_2_I)
print("\n")

B_3 = np.matrix([[1., 0., 1.],
                 [0., 2., 0.],
                 [0., 2., 3.]])
B_3_I = B_3.I
print("B_3_I")
print(B_3_I)
print("\n")

print("B_2_I*B_1_I")
print(B_2_I*B_1_I)
print("\n")

# IF B_3_I = B_x *B_1_I, B_x = B_3_I *B_1_I.I
B_x = B_3_I *B_1_I.I
print("B_x.I")
print(B_x.I)
print("\n")import numpy as np
B_1 = np.matrix([[1., 0., 0.],
                 [0., 2., 0.],
                 [0., 2., 1.]])
B_1_I = B_1.I
print("B_1_I")
print(B_1_I)
print("\n")

B_2 = np.matrix([[1., 0., 1.],
                 [0., 1., 0.],
                 [0., 0., 3.]])
B_2_I = B_2.I
print("B_2_I")
print(B_2_I)
print("\n")

B_3 = np.matrix([[1., 0., 1.],
                 [0., 2., 0.],
                 [0., 2., 3.]])
B_3_I = B_3.I
print("B_3_I")
print(B_3_I)
print("\n")

print("B_2_I*B_1_I")
print(B_2_I*B_1_I)
print("\n")

# IF B_3_I = B_x *B_1_I, B_x = B_3_I *B_1_I.I
B_x = B_3_I *B_1_I.I
print("B_x.I")
print(B_x.I)
print("\n")