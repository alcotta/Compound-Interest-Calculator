print ("This program will calculate your compound interest")
principal = int( input ("Enter amount of principal originally deposited: " ))
apr = int( input ("Enter the annual interest rate paid by the account (if 5% type 5): "))
timesPerYear = int( input ("Enter the times per year interest is compounded (if quarterly enter 4): "))
numberOfYears = int( input ("Enter the number of years account will be left to earn interest: "))

compoundInterest = principal*((1+ (apr/timesPerYear))*(timesPerYear * numberOfYears))

print (" Amount in account: ") 
print (compoundInterest)

print ("Amanda Alcott-Herr")
#Create a program that will calculate the compound interest
#Formuala A = P((1+ (r/n))^nt) 
#A = amount of money in account after a specifed number of years
#P = principal amount originally deposited into account
#r = annual interest rate
#n = number of times per year interest is compounded
#t = number of years
