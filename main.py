# IMPORTANT NOTE - if you want to skip straight to the main menu when testing out my code, go to the second last line of this program and un-comment "# mainMenu()"

# import external packages
import time
import os
import random

import sys
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import track


# import external files
import data

# function to introduce users to the app
def introduction():
  # print an introduction
  write("\x1B[3mHi, I'm Eddie Woo! Welcome to the Virtual Woo Experience!\x1B[0m")
  time.sleep(1)
  print()
  print("Are you ready to explore the exciting world of mathematics? Well you're in the right place! This app is designed specifically for students in year 7-8 who want to learn maths in a fun and engaging way.\n")
  time.sleep(4)
  print("Eddie Woo is a renowned maths teacher who has been inspiring students for years. With this app, you can now experience the same joy of learning from the comfort of your own home.\n")
  time.sleep(4)
  write("\x1B[3mWell, what are you waiting for? Enter your name below to begin!\x1B[0m")

  # recieve the user's name and store it
  data.user["name"] = input("\n> ")
  reset(0.5)

  # print the app instructions
  write("\x1B[3mAwesome! Before we get started, there are a few instructions we need to get through.\x1B[0m\n")
  print()
  time.sleep(1)
  print("From the main menu you can access the learning page, settings, instructions or exit the app. Type in a letter to choose the corresponding option.")
  print()
  time.sleep(3)
  print("On the learning menu, you will see a list of topics to choose from. Select the topic you would like to learn by following the on-screen instructions.")
  print()
  time.sleep(3)
  print("Topics are broken up into levels. Complete the quiz at the end of each level to progress to the next one!")
  print()
  time.sleep(3)
  print("For each answer you get correct you earn 5 points! Any mistake and you lose 2 :( Your final score is displayed on the exit screen!")
  print()
  time.sleep(3)
  print("Type exit at any time to return to the previous menu. There is no shame in retrying a quiz!\n")
  time.sleep(3)
  print()
  write("\x1B[3mWith that out of the way, let's have a quick look at the settings! Press <enter> to continue. \x1B[0m")
  input()
  
  settings()

# main menu function
def mainMenu():
  options = ''
  reset()

  #display a title
  f = Figlet(font='straight')
  print(f.renderText('Main Menu'))

  print("Enter A, B, C, D or X to select an option.\n")

  # display options
  print("A: Learning\nB: Settings\nC: Instructions\nD: Results\nX: Exit")
  print()

  # recieve an input and open corresponding function
  while True:
    options = input("> ")
    match options:
      case 'A':
        learnMenu()
      case 'B':
        settings()
      case 'C':
        instructions()
      case 'D':
        results()
      case 'X':
        results(True)
        exit()
      case _:
        # default case, in case of submission errors
        print("\nWoops! That's not an option. Please select A, B, C, D or X.\n")

#function to display the app instructions
def instructions():
  reset()

  # display a heading
  f = Figlet(font='straight')
  print(f.renderText('Instructions'))

  # print instructions
  print("From the main menu you can access the learning page, settings, instructions or exit the app. Type in a letter to choose the corresponding option.\n\nOn the learning menu, you will see a list of topics to choose from. Select the topic you would like to learn by following the on-screen instructions.\n\nTopics are broken up into levels. Complete the quiz at the end of each level to progress to the next one!\n\nFor each answer you get correct you earn 5 points! Any mistake and you lose 2 :( Your final score is displayed on the exit screen!\n\nType exit at any time to return to the previous menu. There is no shame in retrying a quiz!\n")
  input("Type <enter> to return to the menu: ")
  mainMenu()

# function to select topics to learn
def learnMenu():
  reset()
  options = ''
  
  # print heading
  f = Figlet(font='straight')
  print(f.renderText('Topics'))

  # print each module and any levels the user has completed.
  print("Choose a module. Enter A, B, C, D or E to begin!\n")
  print("Module A: Algebra & Equations (" + str(data.user["level"]["A"] - 1) + "/3)")
  print("Module B: Angles (" + str(data.user["level"]["B"] - 1) + "/2)")
  print("Module C: BODMAS (" + str(data.user["level"]["C"] - 1) + "/1)")
  print("Module D: Area & Perimeter (" + str(data.user["level"]["D"] - 1) + "/3)")
  print("Module E: Pythagoras' Theorem (" + str(data.user["level"]["E"] - 1) + "/2)\n")
  
  while True:
    # recieve a module selection
    options = input("> ")

    # open corresponding module
    match options:
      case 'A':
        openModule("A")
      case 'B':
        openModule("B")
      case 'C':
        openModule("C")
      case 'D':
        openModule("D")
      case 'E':
        openModule("E")
      case 'exit':
        mainMenu()
      case _:
        # default case to catch submission errors
        print("\nWoops! That's not an option. Please select A, B, C, D, E or 'exit'\n")
  
# function to change settings
def settings():
  options = ""
  reset()

  # display a title
  f = Figlet(font='straight')
  print(f.renderText('Settings'))

  # check if its a users first time visiting the instructions
  if data.user["beginner"] ==  True:
    write("\x1B[3mTo toggle a setting on or off, type in its number. If you just want to keep going, press <enter>.\x1B[0m\n")
    data.user["beginner"] = False
  else:
    print("Select a number to toggle a setting or type 'exit' to return to the menu.")
    print()

  # display the settings
  print("1) Eddie Woo Speech Is Instant |", data.settings["opt1"])
  print("2) Eddie Woo Question Tips |", data.settings["opt2"])
  print()

  # recieve inputs
  while True:
    options = input("> ")

    # change respective settings
    match options:
      case "":
        reset()
        # display a progress bar
        for _ in track(range(100), description='[green]Saving Preferences'):
          process_data()
        mainMenu()
      case "exit":
        reset()
        # display a progress bar
        for _ in track(range(100), description='[green]Saving Preferences'):
          process_data()
        mainMenu()
      case "1":
        # check if setting is on or off and toggle it
        if data.settings["instant_eddie"] == 0.01:
          data.settings["instant_eddie"] = 0.0
          data.settings["opt1"] = "ON"
        else:
          data.settings["instant_eddie"] = 0.01
          data.settings["opt1"] = "OFF"
        reset()
        settings()
      case "2":
        # check if setting is on or off and toggle it
        if data.settings["eddie_hints"] == 1:
          data.settings["eddie_hints"] = 10
          data.settings["opt2"] = "ON"
        else:
          data.settings["eddie_hints"] = 1
          data.settings["opt2"] = "OFF"
        reset()
        settings()
      case _:
        # in case of other inputs
        print()
        print("Woops! That's not an option. Please select 1, 2 or <enter> to exit.\n")
    
    
# function to open the selected module and show the lesson exlpanation
def openModule(module):
  level = data.user["level"][module]
  quiz_selection = ''

  # clear the sreen and display a title
  reset()
  print("Module", module, "Level", data.user["level"][module])
  print()

  # try to open the exlanation for the module but if it doesn't exist, exit to the menu
  try:
    console = Console()
    console.print(data.explanations[module][level], "\n", overflow="fold")
  except KeyError:
    reset()
    print("Oops, it looks like you've already completed this module! Type <enter> to return to the menu and choose a new topic.\n")
    input("> ")
    learnMenu()

  # check if the user wants to do the quiz
  while True:
    quiz_selection = input("Press <enter> to start the quiz or 'exit' to leave: ")

    # process response
    if quiz_selection == "":
      reset()
      questions(module)
    elif quiz_selection == "exit":
      reset()
      learnMenu()
    else:
      reset()
      print("Woops! That's not an option.\n")

# a module to display questions, recieve responses and check if they are correct
def questions(module):
  # initialise important variables
  level = data.user["level"][module]
  mistakes = 0
  question_num = 1
  cont = ''

  # loop through each question and take an input for the answer
  for question in data.questions[module][level]:
    reset()
    print("Question", question_num)
    print(question, end="\n\n")
    answer = input("> ")

    # check if the answer is true
    while True:
      if answer == "":
        print("\nNo answer submitted. Please type in your response below: \n")
      # if the inputted answer matches the real answer
      elif answer.lower() == str(data.questions[module][level][question]):
        # print a message to tell the user they are correct
        print("\n" + data.correct[random.randint(0, len(data.correct)) - 1])
        reset(1)

        # increase the user's correct answers
        data.user["correct"] += 1
        break
      # if the user has run out of attempts
      elif mistakes == 3:
        # tell the user to retry
        print()
        print(data.try_limit[random.randint(0, len(data.try_limit)) - 1] + " Have another read of the lesson " + data.user["name"] + ".\n") 
        # print an encouragement and restart the module
        eddie_speech("encouragement")          
        input("Press <enter> to continue: ")
        openModule(module)
      elif answer == 'exit':
        # display a saving message and leave to the menu
        reset()
        for _ in track(range(100), description='Saving Data'):
          process_data()
        learnMenu()
      else:
        # display a retry message and/or a hint
        print("\n" + data.try_again[random.randint(0, len(data.try_again)) - 1] + "\n")
        eddie_speech("hints")

        # increase the user's total mistakes and the mistakes in this level
        mistakes += 1
        data.user["incorrect"] += 1

      # get the next answer input
      answer = input("> ")

    # reset the mistakes variable and increase the level
    mistakes = 0
    question_num += 1
    print()

  # increase the users level in the module
  data.user["level"][module] += 1
  reset()

  # check if there is a next level and print a congratulatory message if there isn't
  try:
    data.explanations[module][data.user["level"][module]]
  except KeyError:
    print("Awesome work " + data.user["name"] + "! You've completed all levels in module " + module + ". Press <enter> to return to the menu!\n")
    input("> ")
    learnMenu()

  # congratulate the user for completing the level
  print("Congratulations " + data.user["name"] + "! You completed Level", level, "of Module", module + "!")

  # check if the user wants to progress to the next level
  while True:
    cont = input("Would you like to progress to the next level (<enter>) or exit to the main menu ('exit')? ")

    if cont == "":
      openModule(module)
    elif cont == "exit":
      # if the user types exit, display a saving bar and exit to the main menu
      reset()
      for _ in track(range(100), description='[green]Saving Progress'):
        process_data()
      mainMenu()
    else:
      reset()
      print("Woops! That's not an option.\n")

# a function to display the user's score and exit the program
def exit():
  # print a thank you message to the user
  write("\n\x1B[3mThanks for stopping by " + data.user["name"] + ". I hope to see you back here soon!\x1B[0m")
  write("\x1B[3m- Eddie Woo\x1B[0m")

  # input enter to quit
  input("\n<enter> to quit: ")
  reset()
  quit()

def results(exit = False):
  reset()

  # initialise key variables
  zeros = 5
  total_modules = 0

  # display a Results heading
  f = Figlet(font='straight')
  if exit == True:
    print(f.renderText('Final Score'))
  else:
    print(f.renderText('Results'))

  # dislpay a loading bar
  for _ in track(range(100), description='Calculating Score'):
    process_data()
  print()

  # go through each module and check if the user has completed any levels
  for topic in data.user["level"]:
    if data.user["level"][topic] != 1:
      # if the user has completed one or more levels
      total_modules += data.user["level"][topic] - 1
    else:
      zeros -= 1
  
  if zeros == 0:
    # if the user didn't complete any levels, print a message of encouragement
    print("Score: 0.\n")
    write("\x1B[3mBetter luck next time!\x1B[0m")
  else:
    # otherwise, print a congratulatory message with the user's completed levels and score
    print("Completed Levels: " + str(total_modules))
    print("Score: " + str(5 * data.user["correct"] - 2 * data.user["incorrect"])  + "\n")
    write("\x1B[3m" + data.congratulations[random.randint(0, len(data.congratulations)) - 1] + "\x1B[0m")

  if exit == True:
    return
  
  # prompt the user to return to the menu
  while True:
    print("\nPress <enter> to return to the menu.")
    i = input("> ")

    if i == "":
      reset()
      mainMenu()
    elif i == "exit":
      reset()
      exit()
    else:
      reset()
      print("Woops! That's not an option.\n")
  reset()
  quit()

# a function to display Eddie Woo speech
def eddie_speech(reason):
  rand = random.randint(0, data.settings["eddie_hints"])

  # attempt to print speech and return if index is out of range
  try:
    write(data.eddie_speech[reason][rand])
    print()
  except IndexError:
    return

# a function to clear the screen after a given period of time
def reset(seconds = 0):
  # wait for a period then clear the screen
  time.sleep(seconds)
  os.system("clear")

# a function to print text with a typewriter-esque effect
def write(text, speed = data.settings["instant_eddie"]):
  # for each character in the inputted string, wait a period of time then print it
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(random.uniform(speed, speed * 10))
  print("")

# a function that is called in order for loading bars to progress
def process_data():
    time.sleep(0.01)

# if the function is run, open the main menu
if __name__ == "__main__":
  # mainMenu()
  introduction()