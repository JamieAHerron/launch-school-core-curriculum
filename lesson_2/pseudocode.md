
START 

#Given two numbers return the sum of both

GET first number
GET second number

SET sum of both numbers to result 

RETURN result

END 

#make sure to convert strings to integers if needed
#possibly account for errors (missing numbers, incorrect data types)

#Corrected version of above pseudocode
START
  # Given two numbers, return their sum
  
  IF first number is not a number type
    CONVERT first number to number
  
  IF second number is not a number type
    CONVERT second number to number
    
  SET result = first number + second number
  
  RETURN result
END
-------------------------------------------------------------

#a function that takes a list of strings, and returns a
#string that is all those strings concatenated together

START 
    IF argument is not a list raise error 
    SET empty string variable
    
    WHILE looping through list of strings, add each one 
    to empty string variable

    PRINT newly populated string variable
END 

#example answer to my above attempt 
START
  # Given a list of strings, return all strings concatenated together
  
  IF input is not a list
    RAISE error
    
  SET result = empty string
  
  SET iterator = 0
  WHILE iterator < length of input list
    SET current_string = value at position iterator in the list
    SET result = result + current_string
    SET iterator = iterator + 1
    
  RETURN result
END
----------------------------------------------------------------
# a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element.

START
  IF input is not a list
    RAISE error
  
  SET result = empty list

  WHILE iterator is less than list length
    start at first item in list
    add list item to result
    iterate by 2 to skip every second number
  
  RETURN result
END