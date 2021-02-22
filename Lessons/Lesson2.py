
def Sets():
    var1 = {3,2.1,'red',2.1}
    #gets rid of duplicates
    print(var1)

def Dictionaries():
    var9 = {'name': 'Julia', 'age': 25, 'hobbies': ['ski', 'music', 'blog']}
    var9['name'] #output is Julia




def Index():
    var1 = [1,2,3,4,5,6]

    print(var1[2]) #shows the 2nd value in the list

    print(var1[::2]) #prints every other value
    



def countVowles():

    s = str(input("Insert your sentence here: "))

    Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    NumVowles = 0
 
    for i in s:
        if i in Vowels:
            NumVowles = NumVowles + 1
    
    print("This sentence has", str(NumVowles), "vowels")


countVowles()
#Index()

