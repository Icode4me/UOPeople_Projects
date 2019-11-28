"""
Date:
11/28/2019

Description:
The volume of a sphere is 4/3πr3, where π has the value of "pi" given in Section 2.1 of your textbook. 
Write a function called print_volume (r) that takes an argument for the radius of the sphere, and prints
the volume of the sphere.

Call your print_volume function three times with different values for radius.

Include all of the following in your Learning Journal:

The code for your print_volume function.
The inputs and outputs to three calls of your print_volume.
"""

#Objectiive: calculate volume based on radius given

print("\n")
print("\n")
print("Learning Journal Uniit 2 | Assignement Part1")

def print_volume(radius):
    
    # declaring Pi
    pi=3.1415926535897931
    #Math op / expression to find volume of sphere using radius
    volume = 4.0/3.0*pi* radius**3
    #placeholder text to let End-User know we are working 
    print("I'm finished with my calculations...")
    #placeholder text to let End-User know we are done
    print("Here are the result")
    #the result for entered radius in volume cubic inches
    print(">>>> The volume for sphere with radius", radius, " is: ", volume, " in Cubic inches")



# commented the next line only needed to verify that print volume function does actually work
#print_volume(radius)

# the following step will run my function 3 times to provide volume for different sphere radius
def run_three_times():
    print_volume(radius = int(input("please enter radius in inches and Python will calculate the volume?")))
    print_volume(radius = int(input("please enter radius in inches and Python will calculate the volume?")))
    print_volume(radius = int(input("please enter radius in inches and Python will calculate the volume?")))
    
#calling the run_three_times function    
run_three_times()
