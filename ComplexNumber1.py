class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,others):
        return (f"{self.real+others.real}+{self.imaginary+others.imaginary}i")


c1=ComplexNumber(real=2,imaginary=2)
c2=ComplexNumber(real=1,imaginary=2)

print(c1+c2)

