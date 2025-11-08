FILEPATH = "ch02.txt"
with open(FILEPATH, 'r', encoding='utf-8') as file:
    lines = file.readlines()

number_list = []
for lin in lines:
    number_list.append([int(num) for num in lin.split()])


def is_safe(line):
    """given a line determine if it's safe or not"""
    increasing = None
    false_count = 0
    for index in range(len(line)-1):
        if line[index+1] == line[index]:
            false_count+= 1
            # return False
        
        elif line[index+1] > line[index]:
            if increasing is False:
                false_count+= 1
                # return False
            elif (line[index+1] - line[index])>3:
                false_count+= 1
                # return False
            else:
                increasing = True
                
        elif line[index+1] < line[index]:
            if increasing is True:
                false_count+= 1
                # return False
            elif (line[index] - line[index+1])>3:
                false_count+= 1
                # return False
            else:
                increasing = False
    return false_count<=1


safe = 0
for line in number_list:
    if is_safe(line):
        safe+= 1


print(safe)
    