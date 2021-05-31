from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [5, 10, 15, 20, 25]
data2 = [6, 12, 6, 12, 6]

print(areDistinct(data1))
print(areDistinct(data2))
