def solution(n, m):
    def gcd(x,y):
        x, y = max(x,y), min(x,y) 
        if x % y == 0:
            return y     
        y,x = x % y,y
        return gcd(x,y)   
    
    return [gcd(n,m), n*m/gcd(n,m)]