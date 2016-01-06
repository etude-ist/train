from gcd import gcd

def solution(N, M):
    d = gcd(N, M)
    return N / d

def tests():
    assert solution(10, 4) == 5
    assert solution(415633212, 234332) == 103908303
    print 'tests pass'    

        
    
    
