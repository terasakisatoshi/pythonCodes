
def good_det(mat):
    
    a=mat.a 
    b=mat.b
    c=mat.c
    d=mat.d
    det=a*d-b*c
    return det

def bad_det(mat):

    a=mat.a 
    b=mat.b
    c=mat.c
    d=mat.d
    det=a*b-c*d
    return det

class Matrix():
    """
    define matrix object
    A=Matrix(a,b,c,d) is equivalent to
    A=
    \begin{bmatrix}
        a & b
        c & d
    \end{bmatrix}
    """
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def miss_det(self):
        """this program is intentionaly debug"""
        return A

def main():
    mat=Matrix(1,2,3,4)
    good_det(mat)
    bad_det(mat)

if __name__ == '__main__':
    main()
