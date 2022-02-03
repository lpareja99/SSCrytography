
import numlib as nl
from sympy.ntheory.factor_ import totient


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
codes = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
p = 1162281642500018516457695142918123385886797686236787603454999
q = 1576485350800305182150586120662765326256410287326195239351103


def decipherToNum(e,n,num):
    order_n = totient(n) # the euler phi function returns the order of n 
    q,inverse,s = nl.xgcd(e,order_n)
    d= inverse
    solution=pow(num,d,n)
    print(solution)

 

def decipherToCHar(e,n):
    order_n = totient(n) # the euler phi function returns the order of n
    q,inverse,s = nl.xgcd(e,order_n)
    d= inverse
    R =  nl.Zmod(n) 
    numbers = [5047,7985,1614,483,5954,7310,249,856]
    print(numbers)
    solution = []
    for ele in numbers:
        m = R(ele**d)
        if m < 10: 
            m = "000" + str(m)
            
        elif m < 100:
            m = "00" + str(m)
        
        elif m < 1000:
            m = "0" + str(m) 
            
        else:
            m = str(m)
        solution.append(m)
    print("code dephicer: ", solution)
        


    #turn match m's to codes and pass to letters
    code_sol = []
    for block in solution:
        first = block[0]+block[1]
        second = block[2]+block[3]
        code_sol.append(first)
        code_sol.append(second)
    print("code divided to letters: ", code_sol)

    #match code with letter
    sentence = []
    final = ""
    for block in code_sol:
        index = codes.index(block)
        l = letters[index]
        sentence.append(l)
    print("final sentence:", sentence)
        
    




def encodeFromChar(e,n):
    order_n = totient(n) # the euler phi function returns the order of n
    q,inverse,s = nl.xgcd(e,order_n)
    d= inverse
    R =  nl.Zmod(n)   
    # god made the integers - the rest in the work of man - Leopold Kronecker
    # all mathematicians are doing number theory - it's just that they don't know it yet
    print("\n\n")
    #chiper
    phraseString =  "allmathematiciansaredoingnumbertheory-itsjustthattheydontknowityet"
    letter_code = []
    #n = 5429
    #e = 4117

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
    codes = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

    #create list to chiper
    for i in range (0,len(phraseString)):
        
        letter = phraseString[i]
        pos = letters.index(letter)
        code = codes[pos]

        if i%2 == 1:
            nextCode = temp + code
            letter_code.append(nextCode)
        temp = code
    print("codes before chiper:", letter_code)

    chiper_msg = []
    for ele in letter_code:
        number = int(ele)
        m = number**e
        block = R(m)
        print(block)
        chiper_msg.append(block)
        
    print("\n",chiper_msg)
    #d = 11
    #dechiper = (m^e)^d
    #m^e = 149 
    #find number that elevated to e.mod(On) gives m
    order_n = 2800
    d= inverse

    # decrypt the just encrypted message
    numbers= chiper_msg
    solution = []
    for ele in numbers:
        m = R(ele**d)
        if m < 10: 
            m = "000" + str(m)
            
        elif m < 100:
            m = "00" + str(m)
        
        elif m < 1000:
            m = "0" + str(m) 
            
        else:
            m = str(m)
        solution.append(m)
    print("code dephicer: ", solution)
        
    #translate back
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
    codes = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]

    #turn match m's to codes and pass to letters
    code_sol = []
    for block in solution:
        first = block[0]+block[1]
        second = block[2]+block[3]
        code_sol.append(first)
        code_sol.append(second)
    print("code divided to letters: ", code_sol)

    #match code with letter
    sentence = []
    final = ""
    for block in code_sol:
        index = codes.index(block)
        l = letters[index]
        sentence.append(l)
    print("decrypted:", sentence)

