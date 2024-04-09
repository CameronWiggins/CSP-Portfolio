import turtle as trtl
import random as rand

#setup

hitImage = "hit.gif"
standImage = "stand.gif"
resetImage = "resetButton.gif"
card1_11 = "card 1_11.gif"
card2 = "card 2.gif"
card3 = "card 3.gif"
card4 = "card 4.gif"
card5 = "card 5.gif"
card6 = "card 6.gif"
card7 = "card 7.gif"
card8 = "card 8.gif"
card9 = "card 9.gif"
card10 = "card 10.gif"
cardBack = "card back.gif"

wn = trtl.Screen()
wn.bgcolor("green")

wn.addshape(hitImage)
wn.addshape(standImage)
wn.addshape(resetImage)
wn.addshape(card1_11)
wn.addshape(card2)
wn.addshape(card3)
wn.addshape(card4)
wn.addshape(card5)
wn.addshape(card6)
wn.addshape(card7)
wn.addshape(card8)
wn.addshape(card9)
wn.addshape(card10)
wn.addshape(cardBack)

wn.tracer(False)

hitButton = trtl.Turtle()
standButton = trtl.Turtle()
hitButton.penup()
standButton.penup()
hitButton.goto(-70, 0)
standButton.goto(70, 0)
hitButton.turtlesize(3)
standButton.turtlesize(3)
hitButton.shape(hitImage)
standButton.shape(standImage)

writer = trtl.Turtle()
writer.hideturtle()
writer.penup()

resetButton = trtl.Turtle()
resetButton.hideturtle()
resetButton.shape(resetImage)
resetButton.penup()
resetButton.turtlesize(3)
resetButton.goto(0, -95)

wn.tracer(True)

deck = []
userHand = []
dealerHand = []
dealerTurtles = []
userTurtles = []

for num in range(1, 11):
  if (num == 10):
    for i in range(16):
      deck.append(num)
  else:
    deck.append(num)
    deck.append(num)
    deck.append(num)
    deck.append(num)

#functions


def reset(x, y):
  hitButton.showturtle()
  standButton.showturtle()
  writer.clear()
  resetButton.hideturtle()
  for num in range(1, 11):
    if (num == 10):
      for i in range(16):
        deck.append(num)
    else:
      deck.append(num)
      deck.append(num)
      deck.append(num)
      deck.append(num)
  setup()


def setup():
  wn.tracer(False)
  writer.goto(-335, -45)
  writer.write("Lets Play \nBlackack", font=("Arial", 30, "bold"))
  writer.goto(125, -45)
  writer.write(
    "How to Play:\nTry to beat the Dealer's Score but don't \ngo over 21 or you'll fail. Press 'hit' to get \nanother card and 'stand' when your \nconfident in your sum to see if the \ndealer can beat you or fail trying.",
    font=("Arial", 10, "bold"))
  writer.goto(-90, 40)
  writer.write("Dealer Hand /\\", font=("Arial", 20, "bold"))
  writer.goto(-80, -75)
  writer.write("User Hand \/", font=("Arial", 20, "bold"))
  for x in range(2):
    num = deck.pop(rand.randint(0, len(deck) - 1))
    dealerHand.append(num)
    dcard = trtl.Turtle()
    dcard.penup()
    dealerTurtles.append(dcard)
    if (x == 0):
      dcard.shape(cardBack)
    elif ((num == 1) or (num == 11)):
      dcard.shape(card1_11)
    elif (num == 2):
      dcard.shape(card2)
    elif (num == 3):
      dcard.shape(card3)
    elif (num == 4):
      dcard.shape(card4)
    elif (num == 5):
      dcard.shape(card5)
    elif (num == 6):
      dcard.shape(card6)
    elif (num == 7):
      dcard.shape(card7)
    elif (num == 8):
      dcard.shape(card8)
    elif (num == 9):
      dcard.shape(card9)
    elif (num == 10):
      dcard.shape(card10)
  dealerTurtles[0].goto(-75, 250)
  dealerTurtles[1].goto(75, 250)

  for x in range(2):
    num = deck.pop(rand.randint(0, len(deck) - 1))
    userHand.append(num)
    ucard = trtl.Turtle()
    ucard.penup()
    userTurtles.append(ucard)
    if ((num == 1) or (num == 11)):
      ucard.shape(card1_11)
    elif (num == 2):
      ucard.shape(card2)
    elif (num == 3):
      ucard.shape(card3)
    elif (num == 4):
      ucard.shape(card4)
    elif (num == 5):
      ucard.shape(card5)
    elif (num == 6):
      ucard.shape(card6)
    elif (num == 7):
      ucard.shape(card7)
    elif (num == 8):
      ucard.shape(card8)
    elif (num == 9):
      ucard.shape(card9)
    elif (num == 10):
      ucard.shape(card10)
  userTurtles[0].goto(-225, -250)
  userTurtles[1].goto(-75, -250)
  wn.tracer(True)


def wipe():
  wn.tracer(False)
  writer.clear()
  hitButton.hideturtle()
  standButton.hideturtle()
  deck.clear()
  sum = 0
  for num in userHand:
    sum += num
  writer.goto(-170, -190)
  writer.write("User's Hand:", font=("Arial", 30, "bold"))
  writer.goto(120, -190)
  writer.write(sum, font=("Arial", 30, "bold"))
  userHand.clear()
  sum = 0
  for num in dealerHand:
    sum += num
  writer.goto(-195, 100)
  writer.write("Dealer's Hand:", font=("Arial", 30, "bold"))
  writer.goto(155, 100)
  writer.write(sum, font=("Arial", 30, "bold"))
  dealerHand.clear()
  for num in dealerTurtles:
    num.hideturtle()
  dealerTurtles.clear()
  for num in userTurtles:
    num.hideturtle()
  userTurtles.clear()
  resetButton.showturtle()
  writer.goto(-175, -50)
  writer.write("Wanna Play Again?", font=("Arial", 30, "bold"))


def win():
  wipe()
  wn.bgcolor("green")
  writer.goto(-230, -20)
  writer.write("You Win!", font=("Arial", 80, "bold"))
  wn.tracer(True)


def lose():
  wipe()
  wn.bgcolor("green")
  writer.goto(-253, -20)
  writer.write("You Lose!", font=("Arial", 80, "bold"))
  wn.tracer(True)


def push():
  wipe()
  wn.bgcolor("green")
  writer.goto(-215, -20)
  writer.write("Its a Tie!", font=("Arial", 80, "bold"))
  wn.tracer(True)


def compare():
  userCount = 0
  userCount2 = 0
  for num in userHand:
    if (num == 1):
      userCount += num
      userCount2 += 11
    else:
      userCount += num
      userCount2 += num
  if (userCount2 > userCount and userCount2 <= 21):
    userCount = userCount2
  dealerCount = 0
  dealerCount2 = 0
  for num in dealerHand:
    if (num == 1):
      dealerCount += num
      dealerCount2 += 11
    else:
      dealerCount += num
      dealerCount2 += num
  if (dealerCount2 > dealerCount and dealerCount2 <= 21):
    dealerCount = dealerCount2
  if (userCount > dealerCount):
    win()
  elif (dealerCount > userCount):
    lose()
  else:
    push()


def dealer():
  new = deck.pop(rand.randint(0, len(deck) - 1))
  dealerHand.append(new)


def hit(x, y):
  new = deck.pop(rand.randint(0, len(deck) - 1))
  userHand.append(new)
  wn.tracer(False)
  ucard = trtl.Turtle()
  ucard.penup()
  userTurtles.append(ucard)
  if ((new == 1) or (new == 11)):
    ucard.shape(card1_11)
  elif (new == 2):
    ucard.shape(card2)
  elif (new == 3):
    ucard.shape(card3)
  elif (new == 4):
    ucard.shape(card4)
  elif (new == 5):
    ucard.shape(card5)
  elif (new == 6):
    ucard.shape(card6)
  elif (new == 7):
    ucard.shape(card7)
  elif (new == 8):
    ucard.shape(card8)
  elif (new == 9):
    ucard.shape(card9)
  elif (new == 10):
    ucard.shape(card10)
  ucard.goto(userTurtles[len(userTurtles) - 2].xcor() + 150, -250)
  wn.tracer(True)
  count = 0
  count2 = 0
  for num in userHand:
    if (num == 1):
      count += num
      count2 += 11
    else:
      count += num
      count2 += num
  if (count > 21 and count2 > 21):
    lose()


def stand(x, y):
  x = 0
  while x != 100:
    dealer()
    count = 0
    count2 = 0
    for num in dealerHand:
      if (num == 1):
        count += num
        count2 += 11
      else:
        count += num
        count2 += num
    if (count > 21 and count2 > 21):
      win()
      x = 100
    elif (count <= 21 and count >= 18):
      compare()
      x = 100
    else:
      x += 1


setup()
hitButton.onclick(hit)
standButton.onclick(stand)
resetButton.onclick(reset)

wn.mainloop()
