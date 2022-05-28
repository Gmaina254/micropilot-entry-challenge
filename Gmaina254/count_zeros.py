def CountZeros(A):
    count= 0
    for i in A:
        if i == 0:
            count += 1
    return count
A = [2,3,1,2,1,2,70,4,5,6,2,0,0,0,0]
print(CountZeros(A))
