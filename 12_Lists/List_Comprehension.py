n = 5
table = []

for i in range(1,11):
    table.append(n*i)

print(table)    


# LIST COMPREHENSION ---->

# LIST COMPREHENSION IS HELPFULL TO WRITE THE CODE SHORTLY

table = [5*i for i in range(1,11)]
print(table)