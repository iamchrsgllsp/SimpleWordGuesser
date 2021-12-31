from random import randint

words = ["daisy","tulip","flower","rose","lily"]
word = words[randint(0,len(words)-1)]

def play():
  tries = 5
  while tries > 0:
    print(f"Your word has {len(word)} characters!")
    guess = input("Guess the word:\n")

    if len(guess) < len(word):
      print("Sorry thats too little")
      play()
    elif len(guess) > len(word):
      print("Sorry thats too many")
      play()
    else:
      print("You have the right amount")
      correctg = check(guess)
      if correctg[1] == 1:
        print(correctg[0])
        print("You have guessed correctly")
        break
      else:
        print(correctg[0])
        tries = tries -1
  else:
    print("You have run out of attempts")
    

def check(guess):
  count = 0
  correct = 0
  letters = []
  for i in guess:
    if i == word[count]:
      count = count + 1
      correct = correct + 1
      letters.append(i)
    else:
      count = count + 1
      
  if correct == len(word):
    print("correct")
    return letters, 1
  else:
    print("incorrect")
    return letters, 0
        


play()