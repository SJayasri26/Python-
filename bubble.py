array=[24,42,53,23,54,22]
n=len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print('Sortend array:',array)