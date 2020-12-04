def main():
    number = int(input("Insert a number:\t"))
    if(is_prime(number)):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} isn't a prime number.")

def is_prime(num):
    if(num < 2):
        return 0 #all numbers < 2 are not prime numbers
    count = num - 1
    while(count > 1):
        if(num % count == 0):
            return 0 #is not a prime number
        count -= 1
    return 1 #is a prime number

if __name__ == "__main__":
    main()