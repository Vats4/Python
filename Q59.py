#Q59.Calculate how many numbers are divisible by 7 from 1to100.

for i in range(1, 100+1):
    if i%7==0:
        print(i,end=" ")