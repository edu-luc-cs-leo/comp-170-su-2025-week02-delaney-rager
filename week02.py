# WRITE YOUR CODE HERE
## Function to greet a person

def greet(name):
    print(f"Hello {name}. How are you?")

greet("Thomas")


my_friends=["Lindsay", "Liam", "Hanna Mae","Kaia"] #list of strings

def greet_friends(names): #function to greet friends from list
    for i in my_friends:
        greet(i)

greet_friends(my_friends)

def solve_quadratic(a,b,c): #solve quadratic function
    inequality = b**2-4*a*c
    if inequality <= 0:
        print(f'no real solutions')
    else:
        x_1 = (-b-((b**2-4*a*c)**(0.5))/ (2*a))
        x_2 = (-b+((b**2-4*a*c)**(0.5))/(2*a)) 
        print(x_1,x_2)
   
    
solve_quadratic(10,10,-3.3)   

