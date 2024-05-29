import numpy as np 


# Numpy Universal functions 

# np1 = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5])

# print(np.min(np1))

# print(np.max(np1))

# # print(np.sqrt(np1))

# print(np.abs(np1))

# print(np.exp(np1))

# print(np.sign(np1))

# print(np.sin(np1))

# print(np.cos(np1))

# print(np.log(np1))


# Copy vs view 

# np1 = np.array([1, 2, 3, 4, 5])

# np2 = np1.view()

# print(f"Original np1 {np1}")
# print(f"Original np2 {np2}")

# np1[3] = 10
# np2[0] = 20

# print(f"Current np1 {np1}")
# print(f"Current np2 {np2}")


# np2 = np1.copy()

# print(f"Original np1 {np1}")
# print(f"Original np2 {np2}")

# np1[3] = 10
# np2[0] = 20

# print(f"Current np1 {np1}")
# print(f"Current np2 {np2}")



# Shape and Reshape 

# np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(np1)

# print(np1.shape)


# np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

# print(np2)

# print(np2.shape)

# np3 = np1.reshape((3, 4))

# print(np3)

# print(np3.shape)

# np4 = np.arange(1, 13).reshape((2, 3, 2))

# print(np4)

# print(np4.shape)

# np5 = np2.reshape(3, 2, 2)

# print(np5)

# print(np5.shape)

# # np6 = np5.reshape(-1)
# np6 = np5.flatten()

# print(np6)

# print(np6.shape)



# Iterating through Numpy arrays 


# np1 = np.arange(1, 11)

# for x in np1: 
#     print(x)
    
# np2 = np.arange(1, 11).reshape(2, 5)

# for x in np2:
#     for y in x:
#         print(y, end=" ")
#     print()


# np3 = np.arange(1, 13).reshape(2, 2, 3)

# for x in np3:
#     for y in x:
#         for z in y:
#             print(z, end=" ")
#         print()
#     print()
    
    
# # nditer

# for x in np.nditer(np3):
#     print(x)




# Numpy Array Sorting

# np1 = np.array([5, 4, 7, 9, 3])

# print(np1)

# print(np.sort(np1))

# print(np1)


# np2 = np.array(["John", "Tina", "Aron", "Sam"])

# print(np.sort(np2))

# print(np2)


# np3 = np.array([True, False, False, True])

# print(np.sort(np3))

# print(np3)


# np4 = np.array([[6, 3, 9, 1], [5, 8, 4, 7]])

# print(np.sort(np4))

# print(np4)

# print(np.sort(np4.flatten()).reshape(2, 4))  # Combine different methods





# Searching in Numpy array


# np1 = np.array([*(np.arange(1, 11)), 3, 2, 4, 3])

# print(np1)

# x = np.where(np1 == 3)

# print(x[0])


# y = np.where(np1 % 2 == 0)

# print(y[0])

# z = np.where(np1 % 2 == 1)

# print(z[0])


# Filtering in Numpy array

# np1 = np.arange(1, 11)

# print(np1)

# fil = [True, False, True, True, False, False, False, True, False, False]

# new_filtered = np1[fil]

# print(new_filtered)



# fil = []

# for num in np1:
#     if num % 2 == 0:
#         fil.append(True)
#     else:
#         fil.append(False)
        
# print(fil)

# new_filtered = np1[fil]

# print(new_filtered)



# fil = [True if num % 2 == 0 else False for num in np1]

# print(fil)

# new_filtered = np1[fil]

# print(new_filtered)



# fil = np1 % 2 == 0 

# new_filtered = np1[fil]

# print(fil)

# print(new_filtered)




































