"""
Ask N from user. N means number of lines.Then print the following pattern.
Enter n = 8

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
6 6 6 6 6
7 7 7 7 7 
8 8 8 8 8
"""
n=int(input("Enter number of lines= " ))



for i in range(1,n+1):
      for j in range(1,6):
            print(i,end=" ")
      print()