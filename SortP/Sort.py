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

if __name__ == "__main__":
    num = [9.2,2,31,1,62,5.1,8,7]
    print("None:"+str(num))
    print("Bubble:"+str(bubble(num)))
    num = [9.2,2,31,1,62,5.1,8,7]
    print("Insertion:"+str(insertion(num)))