Red = "\033[0;31m"
Blue = "\033[0;34m"
Green = "\033[0;32m"


answer = input(Red + "How many planets are there in the universe? Don't use google!")
answer = answer.lower()
count = 0
if answer ==  '5000':
  count = count + 1
  print(Blue + "correct")
else:
  print(Green + "wrong answer")
  

answer2 = input(Red + "which year did albert einstein died?")
answer2 = answer2.lower()
if answer2 ==  '1955':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer3 = input(Red + "Who made the first rocket ship?")
answer3 = answer3.lower()
if answer3 ==  'robert':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer4 = input(Red + "what year was computer invented?")
answer4 = answer4.lower()
if answer4 ==  '1822':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer4 = input(Red + "What is 6 times 9 plus 7")
answer4 = answer4.lower()
if answer4 ==  '61':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer5 = input(Red + "Which year was ww2?")
answer5 = answer5.lower()
if answer5 ==  '1939':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer6 = input(Red + "Who is the CEO of apple?")
answer6 = answer6.lower()
if answer6 ==  'steve jobs':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer7 = input(Red + "Who discovered gravity")
answer7 = answer7.lower()
if answer7 ==  'isaac newton':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer8 = input(Red + "Who is the founder of The Circle?")
answer8 = answer8.lower()
if answer8 ==  "hassen ugail":
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")

answer9 = input(Red + "When did covid-19 started to spread")
answer9 = answer9.lower()
if answer9 ==  '2019':
  print(Blue + "correct")
  count = count + 1
else:
  print(Green + "Wrong answer")
  
answer10 = input(Red + "Who was the first person to walk on the moon?")
answer10 = answer10.lower()
if answer10 ==  'neil armstrong':
  print(Blue + "correct")
  count = count + 1
  print ("score")
  print (count)
else:
  print(Green + "Wrong answer")