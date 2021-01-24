class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n): 
        div_by_n =[]
        for i in range(1,n+1):
            if n % i == 0:
                div_by_n.append(i)
        return(sum(div_by_n))