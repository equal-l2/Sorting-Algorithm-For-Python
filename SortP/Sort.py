def bubble(num):
    for i in reversed(range(len(num))):
        for j in range(i):
            print(num)
            if num[j] > num[j + 1]:
                tmp = num[j]
                num[j] = num[j + 1]  
                num[j + 1] = tmp
    return num
def insertion(num):
    for i in range(1,len(num)):
        tmp = num[i]
        print(num)
        if num[i - 1] > tmp:
            j = i
            while j > 0 and num[j - 1] > tmp:
                num[j] = num[j - 1]
                j -= 1
            num[j] = tmp
    return num
def selection(num):
    for i in range(len(num)):
        print(num)
        min_num = num[i]
        min_index = i;
        tmp = num[i]
        if i < len(num):
            for j in range(i,len(num)):
                if min_num > num[j]:
                    min_num = num[j]
                    min_index = j
            num[min_index] = tmp
            num[i] = min_num
    return num
def quick(num):
    pass
    
if __name__ == "__main__":
    num = [-9.2,2,31,1,-62,5.1,8,7,1,3,4,2,4,5,5.4,2,1.2,-1,2,3,2,11]
    print("None:"+str(num))
    #print("Bubble:"+str(bubble(num)))
    #print("Insertion:"+str(insertion(num)))
    #print("Selection:"+str(selection(num)))
