a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(a)

for i in range(0,10):
    aux = a[i]
    a[i]=a[20-i-1]
    a[20-i-1]=aux

for i in range(0,20):
    print("N [{}] = {}".format(i,a[i]))
