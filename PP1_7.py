'''
    Practice Questions: Booleans
    Author: Johnny Zhao
    Date Creatd: Sept 25, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
  trueOrFalseQ1 = True #set variable trueOrFalseQ1 to True
  print(trueOrFalseQ1) #outputting trueOrFalseQ1

def q2():
  numQ2 = input("Input an integer: ") #asking the user to input an integer
  numQ2 = int(numQ2) #turning the result into an integer datatype
  bool2 = 5 < numQ2 #checking if the integer is greater than 5(True or False)
  print(bool2) #outputting the result(True or False)

def q3():
  letterQ3 = input("Input the letter a: ") #asking the user to input the letter a
  letterQ3 = str(letterQ3) #turning the result into a string datatype
  bool3 = "a" == letterQ3 #checking if the user put in an a(True or False)
  print(bool3) #outputting the result(True or False)

def q4():
  wordQ4 = input("Input a word earlier in the dictionary than google: ") #asking the user to input a word that's earlier in the dictionary than "google"
  wordQ4 = str(wordQ4) #turning the result to a string datatype
  bool4 = wordQ4 < "google" #checking ig the result is ealier in the dictionary than "google"(True or False)
  print(bool4) #outputting the result(True or False)

def q5():
  numQ51 = input("Input an integer: ") #asking the user to input an integer
  numQ52 = input("Input another integer: ") #asking the user to input another integer
  numQ51 = int(numQ51) #turning the first result into an integer datatype
  numQ52 = int(numQ52) #turning the second result into an integer datatype
  bool5 = numQ51 * numQ52 > 40 #checking if the two results multiplied is greater than 40(True or False)
  print(f"Your numbers multiplied together are greater than 40: {bool5}") #outputting the result(True or False) with "Your numbers multiplied together are greater than 40: " in front

#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
