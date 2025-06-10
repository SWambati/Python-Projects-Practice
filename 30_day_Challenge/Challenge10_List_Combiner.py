#this program allows a user to enter a list, combines them and generates a final list with no duplicates in a random order

input1 = input("Enter a list of values. Remember to space your values: ")
input2 = input("Enter another list of values. Remember to space your values: ")

list1 = input1.split()
list2 = input2.spilt()

combined_list = list1 + list2

final_list = list(set(combined_list))

print("The final combined list of unique values: ",final_list)