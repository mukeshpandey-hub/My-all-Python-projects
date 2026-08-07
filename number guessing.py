import random
import time 

print("""Welcome to the Number guessing game !
    I'm thinking of a number between 1 and 100.""")

def main():
    num = random.randint(1,100)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        high_score = 0
        attempts = 0
        chance = 10
        print("Great! You have selected the easy difficulty level")
        start_time = time.time()
        while attempts < chance :
            try:
                guess = int(input("apna number guess karo:"))
            except ValueError:
                print("oyee valid no. daal:")
                continue      
            attempts += 1
            
            if guess < num :
                print("thoda bada no. daal yrr \n")
                if attempts in (2,4,8):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between:{guess- 10} , {guess + 10}" )
            elif guess > num:
                print("thoda chhota no. daal yrr \n")
                if attempts in (2,4):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between: {guess- 10} , {guess + 10}" )
            else:
                print(f"tu jeet gaya: {num}")
                end_time = time.time()
                total_time = end_time - start_time
                print(f"tune total time liya hai : {total_time:.2f}")
                high_score = attempts
                print("abhi tak tera latest high score hai ", high_score)
                break
        else:
            print("tere chance gaye:!!!!")
                    
    elif choice == 2:
        high_score = 0
        attempts = 0 
        chance = 5
        print("Great! You have selected the medium difficulty level")
        start_time = time.time()
        while attempts < chance :
            try:
                guess = int(input("apna number guess karo:"))                
            except ValueError:
                print("oyee valid no. daal:")
                continue      
            attempts += 1
            
            if guess < num :
                print("thoda bada no. daal yrr \n")
                if attempts in (2,4):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between:{guess- 20} , {guess + 20}" )
            elif guess > num:
                print("thoda chhota no. daal yrr \n")
                if attempts in (2,4):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between:{guess- 10} , {guess + 10}" )
            else:
                print(f"tu jeet gaya: {num}")
                end_time = time.time()
                total_time = end_time - start_time
                print(f"tune total time liya hai : {total_time:.2f}")
                high_score = attempts
                print("abhi tak tera latest high score hai ", high_score)
                break
        else:
            print("tere chance gaye:!!!!")
            
    else:
        high_score = 0
        attempts = 0
        chance = 3
        print("Great! You have selected the hard difficulty level")
        start_time = time.time()
        while attempts < chance :
            try:
                guess = int(input("apna number guess karo:"))     
            except ValueError:
                print("oyee valid no. daal:")
                continue      
            attempts += 1
            
            if guess < num :
                print("thoda bada no. daal yrr \n")
                if attempts in (2):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between:{guess- 10} , {guess + 10}" )
            elif guess > num:
                print("thoda chhota no. daal yrr \n")
                if attempts in (2):
                    ask = input("if you are stuck !!! want some hints y or n:")
                    if ask == "y":
                        print(f"your number lies between:{guess- 10} , {guess + 10}" )
            else:
                print(f"tu jeet gaya: {num}")
                end_time = time.time()
                total_time = end_time - start_time
                print(f"tune total time liya hai : {total_time:.2f}")
                high_score = attempts
                print("abhi tak tera latest high score hai ", high_score)
                break
        else:
            print("tere chance gaye:!!!!")
            
            
round = int(input("kitne round khelna chahte ho:"))

for i in (0,int(round)):
    print("""Please select the difficulty level:
    1. Easy (10 chances) and 3 hints
    2. Medium (5 chances) and 2 hints
    3. Hard (3 chances) and 1 hint""")
    main()