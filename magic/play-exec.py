


"""
Having presented eval for turing strings into Pyhton code,
we take the opportunity to also describe the related exec
function to execute a string containning arbitary Python code,
not only an expression. Suppose the user can write a formula 
as input to the program, and that we want to turn this formula into a callable Python function.
That is, writing sin(x)*cos(3*x)+x**2 as the formula, we would like to get a function
"""

def givenf(x):
    return sin(x)*cos(3*x)+x**2

""" 
This is easu with exec:
"""

formula=input('Write a formula involving x:')
code="""
def f(x):
    return %s
    """%formula
exec(code)

"""
If we respond with the text sin(x)*cos(3*x)+x**2
to the equation, formula will hold this text, which is inserted int the code string such that it become
""
def f(x):
    return sin(x)*cos(3*x)+x**2
""
Thereafter ,exec(code) executes the code as if we had written the contents ofthe code
string directly into the program by hand.
With this technique, we can turn any user-given formula into Python function!!!
Lets us try out such code generation on the fly.We add a while loop
to the previous code snippet defining f(x) such that we can provide x values and f(x) evaluated:
"""

x=0
while x is not None:
    x=eval(input('Given x (None to quit):'))
    if x is not None:
        print('f(%g)=%g'%(x,f(x)))