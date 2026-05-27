def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True    
    else:
        return False
    

def main():
    is_leap = is_leap_year(int(input("What is the year you want to check?: ")))
    print(is_leap)

if __name__ == "__main__":
    main()