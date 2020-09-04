# Day4Assignment
# Name : Pallavi Aher


#-------------------------day4 assignment 

print("print first armstrong number")

for num in range(1042000,702648265):
    length =int(len(str(num)))
    #print(length)
    sum = 0

    temp=num

    while temp > 0:
        dig=int(temp%10)
        #print("dig ==", dig)
        sum=sum+(dig**length)
        #print("sum ==",sum)
        temp =temp/10

    if num ==sum:
        print(num)
        break







