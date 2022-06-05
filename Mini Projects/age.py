def findAge(cdate, cmonth, cyear, bdate, bmonth, byear):
     
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (bdate > cdate):
        cmonth = cmonth - 1
        cdate = cdate + month[bmonth-1]
         
    if (bmonth > cmonth):        
        cyear = cyear - 1
        cmonth = cmonth + 12
    
    fdate = cdate - bdate;
    fmonth = cmonth - bmonth;
    fyear = cyear - byear;
    print("\nPresent Age")
    print("\nYears: ",fyear, "\tMonths: ",fmonth, "\tDays: ",fdate)

def findGap(bdate1, bmonth1, byear1, bdate2, bmonth2, byear2):

    if(byear1 > byear2):
        fdate = bdate2 - bdate1
        fmonth = bmonth2 - bmonth1
        fyear = byear2 - byear1
    if(byear2 > byear1):
        fdate = bdate1 - bdate2
        fmonth = bmonth1 - bmonth2
        fyear = byear1 - byear2 
    print("\nAge Gap is")
    print("\nYears: ",(abs(fyear)-1), "\tMonths: ",abs(fmonth),"\tDays: ",abs(fdate))

exit=1
while exit==1:
    print("\n1. Find Age\n2. Find Age Gap")
    c = int(input("\nEnter your choice: "))
    if c==1:
        current = input("\nEnter the current date in dd/mm/yyyy format: ")
        a = current.split("/")
        cdate = int(a[0])
        cmonth = int(a[1])
        cyear = int(a[2])
        birth = input("\nEnter the birth date in dd/mm/yyyy format: ")
        b = birth.split("/")
        bdate = int(b[0])
        bmonth = int(b[1])
        byear = int(b[2])
        findAge(cdate, cmonth, cyear, bdate, bmonth, byear)
        exit = int(input("\nEnter 1 if you want to continue and press any other key to exit: "))
        if exit==1:
            continue
        else: 
            break
    elif c==2:
        birth1 = input("\nEnter the first birth date in dd/mm/yyyy format: ")
        b = birth1.split("/")
        bdate1 = int(b[0])
        bmonth1 = int(b[1])
        byear1 = int(b[2])
        birth2 = input("\nEnter the second birth date in dd/mm/yyyy format: ")
        c = birth2.split("/")
        bdate2 = int(c[0])
        bmonth2 = int(c[1])
        byear2 = int(c[2])
        findGap(bdate1, bmonth1, byear1, bdate2, bmonth2, byear2)
        exit = int(input("\nEnter 1 if you want to continue and press any other key to exit: "))
        if exit==1:
            continue
        else: 
            break
