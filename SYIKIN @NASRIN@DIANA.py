import random

def main():
    """Start an element guessing game."""
    print("Guess an element!")

    elements = [
        "H",
        "B",
        "N",
        "C",
        "F",
        "K",
        "Be",
        "Mg",
        "Li",
        "He"
        ]
    
    x = random.choice(elements)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element am I thinking of? "))

        if x == guess:
            print("You guessed {He}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {H}.Unfortunately you got the wrong answer. Please try again!".format(guess))
         
            guess = str(input("What element am I thinking of? "))

        if x == guess:
                print("You guessed {B}. Congratulations you got it right!".format(guess))
                break
        else:
            print("You guessed {Li}. Unfortunately you got the wrong answer. Please try again!".format(guess))
          
            guess = str(input("What element am I thinking of? "))

        if x == guess:
                print("You guessed {F}. Congratulations you got it right!".format(guess))
                break
        else:
            print("You guessed {Mg}. Unfortunately you got the wrong answer. Please try again!".format(guess))

            guess = str(input("What element am I thinking of? "))

        if x == guess:
             print("You guessed {C}. Congratulations you got it right!".format(guess))
             break
        else:
            print("You guessed {Be}. Unfortunately you got the wrong answer. Please try again!".format(guess))
        
            guess = str(input("What element am I thinking of? "))

        if x == guess:
             print("You guessed {K}.Congratulations you got it right!".format(guess))
             break
        else:
             print("You guessed {N}. Unfortunately you got the wrong answer. Please try again!".format(guess))

    main()
                    
                    
                      
