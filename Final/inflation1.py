def curValue(sy,sa, r, ey):
    n = ey - sy   # number of years 
    amount =  sa * ((1 + r/100) * n)
    
    print(f"{'Starting Year' : ^20}{'$Starting Year' : <20}{'Inflation Rate %' : ^20}{'Ending Year' : ^20}{'$Ending Year' : <20}")
    print(f"{'{0:.0f}'.format(sy) : <20}{'${0:,.2f}'.format(sa) : <20}{'{0:,.2f}'.format(r) : ^20}{'{0:.0f}'.format(ey) : >20}{'${0:,.2f}'.format(amount) : <20}")
    return amount

## Find the future value for a saving account deposit
startYr = eval(input("Enter starting year (must be on/after 2000): "))
startAmt = eval(input("Enter dollar amount in starting year: "))
r = eval(input("Enter the average annual inflation rate %: "))
endYr = int(input("Enter the ending year "))
endAmt = curValue(startYr,startAmt,r,endYr)