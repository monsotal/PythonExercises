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