import math
import random

print("Chatbot: Hellooo! I'm your new cool AI buddy 😎 What's up?")
print("  (type 'bye' whenever you wanna leave)")

greetings = [
    "Hey there! How's it going?",
    "Hello! What can I do for you today?",
    "Hiya! Need any help or just wanna chat?",
    "Heyy! 👋 Finally you're here! What’s on your mind today?",
    "😊 What adventure are we starting today?",
    "Hello hello! 🎉 Ready when you are~",
    "Yo! Your favorite chat buddy has arrived ✌️ What's up?"
]

how_are_you_responses = [
    "I'm doing great, thanks for asking! How about you?",
    "Feeling fantastic! What about you?",
    "I'm good, just hanging out in the digital world. How are you?",
    "Yo Im gooddd, just chilling in the cloud ☁️ you tho? 😏",
    "Honestly? Living my best binary life 😎 How you holding up?",
    "Im 10/10 charged and ready to cause chaos (or help, your call) — wbu??",
    "Vibing at 100%, no cap. What’s the mood on your end today?"
]

default_responses = [
    "Bruh my Wi-Fi in the cloud just lagged 😂 Say that again?",
    "Error 404: understanding not found 😭 Try rewording?",
    "Wait… what? 😭 Hit me with that one more time please",
    "My bad, I'm lost lol — different words maybe?",
    "That went straight to my spam folder in my brain 💀 Rephrase pls?"
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything! 😂",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😄",
    "Why don't skeletons fight each other? They don't have the guts! 💀😆",
    "why coding is like a relationship? Because if you have to explain it, it's probably not working! 😅",
    "Why did the math book look sad? Because it had too many problems! 📚😢",
    "Why did the computer go to the doctor? Because it had a virus! 🖥️🤒",
]
  
while True:
    user_input = input("you: ").strip().lower()

    if user_input == "bye":
        print("Chatbot: see you later! Take care! 👋")
        break  

    if user_input in ["hello", "hi", "hey", "yoo", "heyy", "hii"]:
        print( "chatbot:" + random.choice(greetings))
        continue


    if user_input in ["how are you", "how are you?", "how r u", "wbu", "how you doing?", "how's it going?", "how are you doing?"]:
        print( "chatbot:" + random.choice(how_are_you_responses))
        continue
    if user_input in ["what's your name?", "what is your name?", "who are you?", "what do i call you?", "name?"]:
        print(f"chatbot: I don't have any name yet , can give me a name insted!!  😎")
        name = input("you: ").strip()
        print(f"chatbot: heyy, I love the name {name}! Thanks for giving me a name! 😊")
    if user_input in ["what's your name again?", "what is your name again?", "who are you again?", "remind me your name?", "name again?"]:
        print(f"{name}: remember? you named me {name}! 😎")
        continue

    if user_input in ["tell me a joke", "joke", "make me laugh", "funny"]:
        print(f"{name}: Here's a joke for you! " + random.choice(jokes))
        continue
    else:
        print(f"{name}: {random.choice(default_responses)}")

  
    if user_input in ["what can you do?", "what are your capabilities?", "what can you help me with?", "help", "what do you do"]:
        print(f"{name}: I can do some basic math calculations for you!")
        print(f"{name}: addition, subtraction, multiplication, division")
        print(f"{name}: exponentiation (power), square root")
        print(f"{name}: floor (smallest integer), ceil (largest integer), absolute value")
        print("Just type the number from the menu below!")
        print("1: addition")
        print("2: subtraction")
        print("3: multiplication")
        print("4: division")
        print("5: exponentiation")
        print("6: square root")
        print("7: floor (smallest integer ≤ number)")
        print("8: ceil (largest integer ≥ number)")
        print("9: absolute value")
        print("(or just type 'bye' to leave)")
       
        user_input = input("you: ").strip()

  
    if user_input == "1":
        print(f"{name}: Great! Let's do some addition. Just enter two numbers and I'll add them for you :)")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 + number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "2":
        print(f"{name}: Subtraction, got it! Just enter two numbers and I'll subtract the second from the first.")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 - number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "3":
        print(f"{name}: Multiplication, nice choice! Just enter two numbers and I'll multiply them for you.")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 * number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "4":
        print(f"{name}: Division, got it! Just enter two numbers and I'll divide the first by the second. (But no dividing by zero, please!)")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            if number2 == 0:
                print(f"{name}: Error! Division by zero is not allowed.")
            else:
                result = number1 / number2
                print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "5":
        print(f"{name}: Exponentiation, cool! Just enter the base and the exponent, and I'll calculate it for you.")
        try:
            number1 = float(input("Enter the base number: "))
            number2 = float(input("Enter the exponent: "))
            result = math.pow(number1, number2)
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "6":
        print(f"{name}: Square root, nice! Just enter a number and I'll give you its square root. (No negative numbers, please!)")
        try:
            number = float(input("Enter the number: "))
            if number < 0:
                print(f"{name}: Error! Cannot calculate square root of a negative number.")
            else:
                result = math.sqrt(number)
                print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "7":
        print(f"{name}: Floor function, got it! Just enter a number and I'll give you the largest integer less than or equal to that number.")
        try:
            number = float(input("Enter the number: "))
            result = math.floor(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "8":
        print(f"{name}: Ceil function, nice choice! Just enter a number and I'll give you the smallest integer greater than or equal to that number.")
        try:
            number = float(input("Enter the number: "))
            result = math.ceil(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "9":
        print(f"{name}: Absolute value, got it! Just enter a number and I'll give you its absolute value.")
        try:
            number = float(input("Enter the number: "))
            result = math.fabs(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{name}: That's not a valid number bro 😅 Try again from start.")
        continue

    
    if user_input in ["rock", "paper", "scissors", "can you play any games with me?", "play a game", "game", "let's play a game"]:
        if user_input in ["can you play any games with me?", "play a game", "game", "let's play a game"]:
            print(f"{name}: OH YEAH! I can play rock-paper-scissors with you! Just type 'rock', 'paper', or 'scissors' to make your move. Let's see who wins!")
            continue

     
        print(f"{name}: Okay let's go!")
        moves = ["rock", "paper", "scissors"]
        chatbot_move = random.choice(moves)
        print(f"Chatbot: I chose {chatbot_move}!")

        if user_input == chatbot_move:
            print(f"{name}: It's a tie! noiceee u played WELL!!! 😮")
        elif (user_input == "rock" and chatbot_move == "scissors") or \
             (user_input == "paper" and chatbot_move == "rock") or \
             (user_input == "scissors" and chatbot_move == "paper"):
            print(f"{name}: You win! Congrats! well playeddd buddy...🎉")
        else:
            print(f"{name}: I won! come with more luck next time :)) 😎")
        continue

  
    
    

   
