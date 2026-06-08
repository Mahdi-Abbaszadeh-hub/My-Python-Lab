# Set

# How is the set introduced?
my_set_1 = {1, 2, 3, 4, 5, 6}
my_set_2 = {4, 5, 6, 7, 8, 9}
my_set_1.add(7)  # ---> {1,2,3,4,5,6,7}
my_set_1[1]  # ---> Can not acsses to value to this method
my_set_1.remove(1)  # ---> {2,3,4,5,6}
my_set_1 | my_set_2  # ---> {1,2,3,4,5,6,7,8,9}
my_set_1 & my_set_2  # ---> {4,5,6}
my_set_1 - my_set_2  # ---> {1,2,3}
my_set_1 ^ my_set_2  # ---> {1,2,3,7,8,9} (my_set_1 | my_set_2) - (my_set_1 & my_set_2)
