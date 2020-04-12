class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        half = n // 2
        total = 0
        for i in range(1,half+1):
            if n%i == 0:
                total += i
                #+ n is to handle the num being a divisor of itself.
        return total + n


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
