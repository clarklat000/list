#SECTION #1
color_list = ["red", "green", "blue", "yellow"]
# Print the first element
print(color_list[0])
# Print the last element
print(color_list[-1])

#SECTION #2
# Create num_list
num_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
# Use append to add 5 to num_list and print
num_list.append(5)
print("After appending 5:", num_list)

# Use remove to remove the first occurrence of 4 and then print
num_list.remove(4)
print("After removing first 4:", num_list)

# Use count to count how many times 4 appears in num_list
count_4 = num_list.count(4)
print(f"4 appears {count_4} times in the list")

# Use the index method to find where the 9 is and print the index
index_9 = num_list.index(9)
print(f"9 is at index {index_9}")

#SECTION #3
# First part of section 3
fruit_list = ["apple", "banana", "cherry", "date"]
# Use index operator [] to alter index 1 to orange
fruit_list[1] = "orange"
print("After changing banana to orange:", fruit_list)

fruit_list.pop()
print("After popping the last element:", fruit_list)