# File: Zeller.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 02/06/2023
# Description of Program: So basically what this program does is when you put in the year, month , and day. It will spit out what day exactly it was on that date you put in. This is made possible via the zeller equation. 
def main():
    print()
    Y = int(input("Enter year (e.g., 2008): "))
    if Y < 1752:
        print("Year must be > 1752. Illegal year entered:", Y)
        return
    m = int(input("Enter month (1-12): "))
    if m in range(1, 13):
        if m in [1,2]:
            m = m + 12
            Y = Y - 1
    else:
        print("Month must be in [1..12]. Illegal month entered:", m)
        return
    d = int(input("Enter day of the month (1-31): "))
    if d in range(1, 32):
        pass
    else:
        print("Day must be in [1..31]. Illegal day entered:", d)
    K = int(str(Y)[2:])
    J = int(str(Y)[:2])
    h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7
    days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
    print("Day of the week is",days[h])
    print()
    
if __name__ == "__main__":
    main()
