'''
Python - Validate a list of credit cards from AAAA Bank which have the following characteristics:
It must start with a 4,5  or 6
It must contain exactly 16 digits
It must only consist of digits (0-9)
It may have digits in groups of 4, separated by one hyphen "-"
It must NOT use any other separator like ' ' , '_', etc
It must NOT have 4 or more consecutive repeated digits
Examples:
Valid Credit Card Numbers
4254625873615486

5535535535553555

5322-2348-7964-3124

Invalid Credit Card Numbers

42546258776197837       #17 digits in card number → Invalid

2215555513331333        #Consecutive digits are repeating 4 or more times → Invalid

5322-2348-7974 - 3124   #Separators other than '-' are used → Invalid

44155x4423332333        #Contains non digit characters → Invalid

0535372585962598        #Doesn't start with 4, 5 or 6 → Invalid

 '''




import re


# match regex against user input , removes hyphens for "check-repeated_digits" method call

def matchCreditCard(num):

      pattern = r"^([4|5|6]\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4})$"

      if re.match(pattern,num):
         f = [x for x in num if x!= "-"]
         f = ("".join(f))
         a = (check_repeated_digits(f))

         if a == None:
            print("Congratulations ! The Card You entered is valid !")

      else:
         print("The Card number you Entered is not Valid")




# splits entire string to quad strings and check for -4- consecutive occurrences

def check_repeated_digits(digitstring):

   current = 0
   for i in digitstring:
      quad =(digitstring[current:current+4])
      current +=1

      if quad.count(quad[0]) == 4:
         print("The Card you Entered is not Valid")
         return 1



userinput = input("Please Provide a Valid Credit Card Number \n"
                "-------------------------------------------\n"
                "Card number should match these compliances:\n"
                "must start with a 4,5  or 6\n"
                "must contain exactly 16 digits\n"
                "must only consist of digits (0-9)\n"
                "may have digits in groups of 4, separated by one hyphen '-' \n"
                "must NOT use any other separator like ' ' , '_', etc\n"
                "must NOT have 4 or more consecutive repeated digits\n")


matchCreditCard(userinput)


