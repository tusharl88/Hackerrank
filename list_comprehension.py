see problem here: https://www.hackerrank.com/challenges/list-comprehensions/problem

#without list_comprehension
X = int(input()) + 1;     
Y = int(input()) + 1; 
Z = int(input()) + 1;
N = int(input());
lst = [];
for x in range(X):
    for y in range(Y):
        for z in range(Z): 
            if (x + y + z) != N: 
                lst.append([x,y,z]);

print(lst);

#tushar press shift +enter and give input equal zero to all three X,Y, AND Z then 
#list will remain empty because X+Y+Z=0 will become equal to N i.e 0which is not according to question

#here +1 is added to x,y and z because if user gives input 0 to all X,Y, AND Z
#then range will become 0+1=1 hence loop will run atleast one time i.e.at 0
#otherwise if 1 is not added then range will become 0(if user gave X=Y=Z=0) and it means -1 due to which loop will not run


#with list_comprehension

#here list comprehension is used

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1 #another way of adding +1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)

#simple_code

#here we have made code simpler:

X,Y,Z,N=[int(input()) for i in range(4)]                #so for loop runs four times 0,1,2,3 
                                                        #and each times gives value to one variable.

X += 1 #another way of adding +1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)
