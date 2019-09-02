  
# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

code:
test =int(input())              #we give input as 12 because then we have to pass exactly 12 commands from insert 0 5 to print.
s=[]
for _ in range (test):            #so for loop will run 12 times.by convention _ is used for unused variable.
    cmd=input().split()            #split method returns list of strings. when we give 1st command out of 12 commands i.e. insert 0 5, then it is stored as list ['insert','0','5'] in cmd.
    
    if cmd[0]=='insert':          #here cmd[0] means first element of string which is insert and it matches with insert, hence if condition is satisfied.
        s.insert(int(cmd[1]),int(cmd[2]))          #insert takes 2 arguments: first argument is position which is cmd[1] i.e. 0 and second argument is value cmd[2] i.e.5
                                                         #int is placed before cmd[0] to convert string '0' to integer
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))

    elif cmd[0]=="append":
        s.append(int(cmd[1]))

    elif cmd[0]=="sort":
        s.sort()

    elif cmd[0]=="pop":
        s.pop()

    elif cmd[0]=="reverse":
        s.reverse()

    elif cmd[0]=="count":
        v=s.count(int(cmd[1]))
        print(v)

    elif cmd[0]=="index":
        x=s.index(int(cmd[1]))
        print(x)
   
    elif cmd[0]== 'print':
        print(s)



