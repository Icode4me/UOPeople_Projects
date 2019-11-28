"""

Write your own function that illustrates a feature that you learned in this unit. The function must take at least one argument. The function should be your own creation, not copied from any other source. Do not copy a function from your textbook or the Internet.

Include all of the following in your Learning Journal:

The code for the function that you invented.
The inputs and outputs to three calls of your invented function.
A description of what feature(s) your function illustrates.  


"""

def myBio():
    name=input("enter your name?")
    dob=input("enter your date of birth?")
    cob=input("enter your country of birth?")
    c_or_d=input("do you like cats or dogs?")
    print("\n")
    print("Here's a Bio based on the info you provided ... ", "\n")
    print("Your name is: ", name, "\n")
    print("Your birthdate is: ", dob, "\n")
    print("Your country of birth is: ", cob, "\n")
    print("You are a ", c_or_d, " person")
    
myBio()   



"""

The results from the interpeter as follows:

Here's a Bio based on the info you provided ...  

Your name is:   John Doe 

Your birthdate is:   09/14/1978 

Your country of birth is:   Nomad - World Citizen 

You are a   Cats  person

"""
