class Calculator:
    def __init__(self) -> None:
        pass

    def add(self,a:int,b:int) -> int:
        '''Adds two numbers.'''
        return a + b

    def subtract(self,a:int,b:int) -> int:
        '''Substracts second number from first.'''
        return a-b

    def product(self,a:int,b:int) -> int:
        '''Multiplies two numbers.'''
        return  a*b

    def divide(self,a:int,b:int) -> int:
        if b == 0:
            raise ValueError
        else:
            return a/b