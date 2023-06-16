# create a list of squared numbers (n*n). It needs to return a list of squares of consecutive numbers
#between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].
def create_squered_nums(start,end):
    return [ num**2 for num in range(start,end+1)]

print(create_squered_nums(2,3))
#longer solution:
list_of_squered_nums = []
def create_squred_nums2(start,end):
    for num in range(start,end+1):
        squered_num = num**2
        list_of_squered_nums.append(squered_num)
    return list_of_squered_nums
print(create_squred_nums2(2,3))