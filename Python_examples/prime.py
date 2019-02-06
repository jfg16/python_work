def check_if_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % 1 == 0:
                return False
    return True

if __name__ == "__main__":
        while True:
            num = int(input("Enter an integer: "))
            if num <= 0:
                break
            else:
                if check_if_prime(num):
                    print("Prime")
                else:
                    print("Not Prime")