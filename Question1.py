DictionaryOne = {11812570 : "Saksham", 11815241 : "Vishal", 11813189 : "Saurabh", 11814197 : "Anuj", 11819663 : "Shivam"}
DictionaryTwo = {11812570 : 98, 11815241 : 56, 11813189 : 67, 11814197 : 88, 11819663 : 72}

DictionaryThree = {}

for X in DictionaryOne and DictionaryTwo:
    
    print ("Registration Number : ",X)
    print ("Name : ",DictionaryOne[X])
    Temp = DictionaryTwo[X]
    Temp2 = DictionaryOne[X]
    print ("Marks Obtained : ",DictionaryTwo[X]) 
    
    if (Temp >= 90) and (Temp <= 100):
        Grade="O"
        print ("Grade : 'O'")
        DictionaryThree[Temp2] = Grade
        
    if (Temp >= 80) and (Temp < 90):
        Grade="A+"
        print ("Grade : 'A+'")
        DictionaryThree[Temp2] = Grade
        
    if (Temp >= 70) and (Temp < 80):
        Grade="A"
        print ("Grade : 'A'")
        DictionaryThree[Temp2] = Grade
        
    if (Temp >= 60) and (Temp < 70):
        Grade="B+"
        print ("Grade : 'B+'")
        DictionaryThree[Temp2] = Grade
        
    if (Temp >= 50) and (Temp < 60):
        Grade="B"
        print ("Grade : 'B'")
        DictionaryThree[Temp2] = Grade

    print (" ")

print (DictionaryThree)
