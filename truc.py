
s = "Bonjour"

print(s*6)


for  i in range(10):
    print("table de 3 :" , i , "fois 3 = ",  i*3)
 
# afficher les tables de multiplication : 

for i in range(1,11):
    print("")
    print("*"*40)
    print("table de ",i, ":" )
    print("*"*40)
    for j in range(11): 
        print( i * j, " ", end="" )



