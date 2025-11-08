
FILEPATH = "ch01.txt"
with open(FILEPATH, 'r', encoding='utf-8') as file:
    lines = file.readlines()

numbers_1 = []
numbers_2 = []
for line in lines:
    numbers_1.append(line.split()[0]) 
    numbers_2.append(line.split()[1]) 

numbers_1.sort()
numbers_2.sort()

# sum = 0
# for index in range(len(numbers_1)):
#     sum += abs(int(numbers_1[index]) - int(numbers_2[index]))
# print(sum)
sum  = 0
dictionary = {}
for number in numbers_1:
    if number not in dictionary:
        count= numbers_2.count(number)
        dictionary[number] = count
    sum += int(number)*dictionary[number]
print(sum)
    

