class my_stat():
    def cal_sigma(self,m,n):
        
        result = 0
        for i in range(n,m+1):
            result = result +i
            
        return (result)
    
    def pi(self, n, m):
        result = 1
        for i in range(n, m+1):
            result *= i
        return result
        
    def factorial(self, m):
        result = 1
        for i in range(1, m+1):
            result *= i
        return result
    
    def permutation(self, n, m):
        return self.factorial(m) // self.factorial(m-n)
        
