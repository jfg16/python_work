from __future__ import print_function 

def even_fib(n):
    total =0    
    f1, f2 =1,2
    while f1 <n:
        if f1 %2==0:            
            total = total + f1        
        f1, f2 = f2, f1 + f2 
    return total 

if __name__ == "__main__":    
    limit = raw_input("Enter the max Fibonacci number: ")    
    print(even_fib(int(limit)))