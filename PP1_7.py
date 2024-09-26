def q1():
  trueOrFalseQ1 = True
  print(trueOrFalseQ1)

def q2():
  numQ2 = input("Input an integer: ")
  numQ2 = int(numQ2)
  bool2 = 5 < numQ2
  print(bool2)

def q3():
  letterQ3 = input("Input the letter a: ")
  letterQ3 = str(letterQ3)
  bool3 = "a" == letterQ3
  print(bool3)

def q4():
  wordQ4 = input("Input a word earlier in the dictionary than google: ")
  wordQ4 = str(wordQ4)
  bool4 = wordQ4 < "google"
  print(bool4)

def q5():
  numQ51 = input("Input an integer: ")
  numQ52 = input("Input another integer: ")
  numQ51 = int(numQ51)
  numQ52 = int(numQ52)
  bool5 = numQ51 * numQ52 > 40
  print(f"Your numbers multiplied together are greater than 40: {bool5}")

#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
