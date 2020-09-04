#Assignment1 Day3
# Name : Pallavi aher


#----------------------------day3 assignment 1


alt= input("Enter the altitude required  for landing in ft");
alt=int(alt);

if(alt< 1000):
    print("Output : Safe is land");
elif((alt>1000) and (alt<5000)):
    print("Bring down to 1000");
else:
    print("Turn around");

#---------------------------day3 assignment 2

print("print all prime number bet 1 to 200");
for num in range(1,200):
    if num > 1 :
        for i in range(2,num):
            if(num % i)==0:
                break
        else:
            print(num)







