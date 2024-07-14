# Input the marks of N students
def avg(mark_list, n):
    print ("Avg: ", sum(mark_list)/n)

def high_low(marks_list):
    highest = max(marks_list)
    lowest = min(marks_list)
    print("highest: ", highest, " and lowest: ", lowest)

def absent(mark_list):
    result = 0
    for x in mark_list:
        if(x < 0):
            result += 1
        else:
            continue
    print("number of absent students: ",result)

def passFail(mark_list, n):
    passed = 0
    for x in mark_list:
        if(x < 33):
            passed += 1
    print("Passed %: ", (passed*100)/n)
    print("Failed %: ",(n-passed)*100/n)


def highest_freq(marks_list):
    dict = {}
    for x in marks_list:
        if dict.get(x) in dict.values():
            dict[x] += 1
        else:
            dict[x] = 1
    
    highest_f = max(dict.values())
    key_list = list(dict.keys())
    value_list = list(dict.values())
    print("highest frequency is: ")
    for x in range(len(value_list)):
        if(value_list[x] == highest_f):
            print(key_list[x])


n = int(input("Total number of students: "))
marks_list = list()

for x in range(0, n):
    mark = int(input("Enter marks of roll no %d: "%(x+1)))
    marks_list.append(mark)

print(" ")
avg(marks_list, n)
high_low(marks_list)
absent(marks_list)
passFail(marks_list, n)
highest_freq(marks_list)