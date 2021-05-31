def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([5, 10, 15, 20, 25, 30, 35]))
