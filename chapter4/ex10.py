cubes_list =[number**3 for number in range (1,10)]
for cube in cubes_list:
    print(cube)
print(f"The first three items in the list are:. {cubes_list[:3]} ")
print(f"Three items from the middle of the list are:. {cubes_list[3:6]} ")
print(f"The last three items in the list are: {cubes_list[-3:]}")
