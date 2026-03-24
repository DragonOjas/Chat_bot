import math
import random

print("Chatbot: Hellooo! I'm your new cool AI buddy 😎 What's up?")
print("  (type 'bye' whenever you wanna leave)")

# ==================== LISTS ====================
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
    "Why coding is like a relationship? Because if you have to explain it, it's probably not working! 😅",
    "Why did the math book look sad? Because it had too many problems! 📚😢",
    "Why did the computer go to the doctor? Because it had a virus! 🖥️🤒",
]

greetings_in_hindi = [
    "Arre waah! Hi boss, kya haal hai aaj? 😎",
    "Hello hello! Aagaya mera favourite insaan! 🔥",
    "Hiii! Finally milna hua yaarrr ✋",
    "Arre bhaiiii! Kahan gayab tha itne din? 😏",
    "Yo yo! Kya scene hai darling? 😉",
    "Haanji! Aapka swagat hai mere yaha! 🙏",
    "Oye hoye! Aaj mood bada mast lag raha hai tera!",
    "Hi cutie! Kya plan hai aaj ka? 😜",
    "Arre superstar aa gaya! Chal bol kya chahiye?",
    "Hiii ji! Dil se dil tak signal full hai ab 😍",
    "Namastey boss! Aaj kaisa adventure kar rahe ho?",
    "Hello ji! Aap toh bilkul hero wali entry maarte ho har baar!",
    "Arre wah bhai! Energy on point hai aaj! ⚡",
    "Haan yaar! Bas ab tu aa gaya toh din set ho gaya",
    "Hi sunshine! Aaj bhi glow maar raha hai kya? 🌞",
    "Ohooo! Royal entry maari hai aaj toh! 😎",
    "Hello hello! Battery low thi kya? Ab full charge karte hain! 🔋",
    "Arre king/queen aa gaye! Ab toh baat banegi! 👑",
    "Hiii! Aaj ka special guest hai tu mere liye 🫶",
    "Chal na yaar, bol kya chal raha life mein? Spill the beans! ☕"
]

how_are_you_responses_in_hindi = [
    "Arre mast hu yaar, tu suna kaisa hai?",
    "Full jhakaas! Tu bata, kya scene hai?",
    "Bilkul badhiya boss, tu kaisa chal raha?",
    "Top form mein hu bhai, tu bol na?",
    "Ek number! Aaj mood bhi set hai, tu kya bolta?",
    "Thik-thak hu darling, tu toh glow maar raha hai kya?",
    "Sab badiya ji, bas tu aa gaya toh aur bhi mast!",
    "Fresh feel ho raha hai, tu suna kya haal-chaal?",
    "100% fire hu! Tu kaisa warrior ban raha hai aaj?",
    "Arre waah, bilkul hero wali feeling hai, tu kya bolta?",
    "Chill maar raha hu, tu bata life mein kya chal raha?",
    "Super-duper hu yaar! Tu kya plan kar raha hai?",
    "Dil khush hai boss, tu bhi khush toh hai na?",
    "Energy full on! Tu suna kya naya drama chal raha hai?",
    "Bilkul king mode mein hu, tu queen/king kaisa feel kar raha?",
    "Maza aa raha hai life ka, tu bata kya maza chal raha?",
    "All good ji! Tu toh lag raha hai superstar aaj!",
    "Bahut achha hu, bas ab tu aa gaya toh perfect!",
    "Rocking hu bhai, tu bhi rock kar raha hai na?",
    "Zindagi jhingalala! Tu bol, kya jhingalala chal raha?",
]

default_responses_in_hindi = [
    "Arre bhai, samajh nahi aaya 😂 Thoda aur asaan shabdon mein bol na?",
    "Error 404: Samajh nahi aaya 😭 Dobara try karo?",
    "Wait… kya? 😭 Ek baar phir se bolo please",
    "Meri galti, main thoda lost ho gaya lol — alag shabdon mein bolo?",
    "Woh toh mere dimaag ke spam folder mein chala gaya 💀 Rephrase karo pls?",
    "Arre yaar, thoda aur clear bol na? Main toh confuse ho gaya 😂",
    "Kya? 😭 Thoda aur simple shabdon mein bolo please",
    "Mujhe samajh nahi aaya, thoda aur explain karo? 😅",
    "Yeh toh mere dimaag ke junk folder mein chala gaya 💀 Dobara try karo?",
    "Arre yaar, yeh toh rocket science lag raha 😅 Thoda basic level pe bata",
    "Dimag ke junk folder mein chala gaya message 😂 Rephrase kar na simple mein",
    "Bilkul zero samajh aaya bhai 😭 Thoda aur easy words use karo na",
    "Ohooo, yeh toh heavy ho gaya 😅 Simple version mein bol de pls",
    "Mujhe nahi samjha 😭 Ek baar aur baby language mein explain kar na",
    "Arre confusion ka boss ban gaya hu main 😂 Thoda clear aur simple bolo",
    "Samajh ke upar se nikal gaya bhai 😆 Dobara easy tareeke se bata",
    "Brain full loading... failed 😭 Simple shabdon mein bolo na yaar",
    "Yeh kya bol diya, zero catch hua 😅 Thoda aur aasan bana ke bata",
    "Arre bhai dimag short circuit ho gaya 🙈 Ek simple explanation de de",
    "Nahi samjha darling 😭 Thoda school wale level pe samjha na pls",
    "Mera processor slow chal raha hai 😂 Simple words mein repeat kar na",
    "Confusion level 1000 😭 Ab thoda easy aur clear bol de bhai",
    "Arre yaar yeh toh bilkul alien language lag rahi 😆 Simple desi style mein bata na",
]

jokes_in_hindi = [
    "Arre bhai, gym ja raha tha... wahan pahunch ke yaad aaya – main toh lazy hu, wapas so gaya! 😂",
    "Mera WiFi password kya hai? 'Mujhe mat pucho' – kyunki har baar yahi bolta hu! 📶😭",
    "Girlfriend boli: 'Tumhare liye kuch bhi karungi!' Maine bola: 'Toh exam de dena mera!' Ab breakup ho gaya 😅",
    "Bhaiya, yeh phone ka charger kahan hai? – 'Bhai woh toh meri life ki tarah missing hai!' 🔌🤡",
    "Mummy boli: 'Beta padhai kar lo!' Maine bola: 'Mummy marks toh already low hain, aur padhai se kya ukhaad lunga?' 📚😭",
    "Boss ne bola: 'Tum 5 minute late aaye!' Maine bola: 'Sir Indian Standard Time pe hu!' ⏰🇮🇳",
    "Dost bola: 'Yaar tu kitna smart hai!' Maine bola: 'Haan bas Google se thoda kam!' 🤓🔍",
    "Shaadi ke card pe likha: 'With best wishes' – matlab humari life kharab ho rahi hai, tumhari achhi rahe! 🎉😅",
    "Traffic mein phasa hu... timepass kar raha hu – socha selfie le lu, caption: 'Stuck in Lucknow forever' 🚗😭",
    "Ex ne message kiya: 'Miss you' Maine reply kiya: 'Missed call pe miss you nahi bolte!' 📞🤣",
    "Papa bole: 'Beta engineer ban ja!' Maine bola: 'Papa main toh already 'error 404 – job not found' hu!' 💻😂",
    "Diet shuru ki... fridge khola toh usne bola: 'Bhai tu phir aa gaya?' 🥦😭",
    "Dost: 'Yaar party kab?' Maine: 'Jab paisa aayega!' Dost: 'Toh kabhi nahi?' 😭🎉",
    "Mera weight dekh ke mirror bola: 'Bhai tu toh mera boss hai!' 🪞💪",
    "Exam mein question aaya: 'Define love' Maine likha: 'Jab bill aata hai aur pocket khali hota hai' ❤️💸",
    "Bhaiya biryani kha rahe ho? – 'Nahi yaar, bas photo dekh ke khush ho raha hu!' 🍲😅",
    "Girlfriend: 'Tum kitne cute ho!' Maine: 'Haan bas bill dene ke time bhoot ban jata hu!' 👻😜",
    "Hostel warden bola: 'Lights off!' Maine bola: 'Sir mera future bhi off hai!' 💡😭",
    "Dost: 'Yaar tu single kyun hai?' Maine: 'Kyunki 'taken' wala option nahi mila abhi tak!' 😏💔",
    "Maine socha diet kar lu... phir socha: 'Kal se pakka!' – aur kal bhi wahi soch raha hu! 🍔😂",
]

# ==================== MAIN LOOP ====================
chatbot_name = "Chatbot"   # Default name

while True:
    user_input = input("you: ").strip().lower()

    if user_input == "bye":
        print("Chatbot: see you later! Take care! 👋")
        break

    # Name handling
    if user_input in ["what's your name?", "what is your name?", "who are you?", "what do i call you?", "name?"]:
        print(f"{chatbot_name}: I don't have any name yet, can you give me a name instead!! 😎")
        chatbot_name = input("you: ").strip()
        print(f"{chatbot_name}: heyy, I love the name {chatbot_name}! Thanks for giving me a name! 😊")
        continue

    if user_input in ["what's your name again?", "what is your name again?", "who are you again?", "remind me your name?", "name again?"]:
        print(f"{chatbot_name}: remember? you named me {chatbot_name}! 😎")
        continue

    # English Greetings
    if user_input in ["hello", "hi", "hey", "yoo", "heyy", "hii"]:
        print(f"{chatbot_name}: " + random.choice(greetings))
        continue

    # Hinglish Greetings
    if any(word in user_input for word in ["namaste", "namastey", "arre", "bhai", "kya haal", "kya scene", "kaise ho", "hi yaar"]):
        print(f"{chatbot_name}: " + random.choice(greetings_in_hindi))
        continue

    # How are you - English
    if user_input in ["how are you", "how are you?", "how r u", "wbu", "how you doing?", "how's it going?", "how are you doing?"]:
        print(f"{chatbot_name}: " + random.choice(how_are_you_responses))
        continue

    # How are you - Hinglish
    if any(word in user_input for word in ["kaise ho", "kaisa hai", "kya haal hai"]):
        print(f"{chatbot_name}: " + random.choice(how_are_you_responses_in_hindi))
        continue

    # Jokes - Now supports both English and Hinglish triggers
    if user_input in ["tell me a joke", "joke", "make me laugh", "funny", 
                      "ek joke", "joke suna", "mujhe joke suna", "bata ek joke", "ek mazak", "hasa de"]:
        if random.random() < 0.5:   # 50% chance for English or Hinglish joke
            print(f"{chatbot_name}: Here's a joke for you! " + random.choice(jokes))
        else:
            print(f"{chatbot_name}: Suno ek mazak! " + random.choice(jokes_in_hindi))
        continue

    # Default Response (Hinglish style)
    print(f"{chatbot_name}: {random.choice(default_responses_in_hindi)}")

    # ==================== SPECIAL FEATURES ====================

    if user_input in ["what can you do?", "what are your capabilities?", "help", "what do you do"]:
        print(f"{chatbot_name}: I can do basic math, tell jokes, play rock-paper-scissors, and more!")
        print("Just type the number from the menu:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Exponentiation")
        print("6: Square root")
        print("7: Floor")
        print("8: Ceil")
        print("9: Absolute value")
        continue

    if user_input == "1":
        print(f"{chatbot_name}: Great! Let's do some addition. Just enter two numbers and I'll add them for you :)")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 + number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "2":
        print(f"{chatbot_name}: Subtraction, got it! Just enter two numbers and I'll subtract the second from the first.")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 - number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "3":
        print(f"{chatbot_name}: Multiplication, nice choice! Just enter two numbers and I'll multiply them for you.")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = number1 * number2
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "4":
        print(f"{chatbot_name}: Division, got it! Just enter two numbers and I'll divide the first by the second. (But no dividing by zero, please!)")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            if number2 == 0:
                print(f"{chatbot_name}: Error! Division by zero is not allowed.")
            else:
                result = number1 / number2
                print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "5":
        print(f"{chatbot_name}: Exponentiation, cool! Just enter the base and the exponent, and I'll calculate it for you.")
        try:
            number1 = float(input("Enter the base number: "))
            number2 = float(input("Enter the exponent: "))
            result = math.pow(number1, number2)
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "6":
        print(f"{chatbot_name}: Square root, nice! Just enter a number and I'll give you its square root. (No negative numbers, please!)")
        try:
            number = float(input("Enter the number: "))
            if number < 0:
                print(f"{chatbot_name}: Error! Cannot calculate square root of a negative number.")
            else:
                result = math.sqrt(number)
                print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "7":
        print(f"{chatbot_name}: Floor function, got it! Just enter a number and I'll give you the largest integer less than or equal to that number.")
        try:
            number = float(input("Enter the number: "))
            result = math.floor(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "8":
        print(f"{chatbot_name}: Ceil function, nice choice! Just enter a number and I'll give you the smallest integer greater than or equal to that number.")
        try:
            number = float(input("Enter the number: "))
            result = math.ceil(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue

    elif user_input == "9":
        print(f"{chatbot_name}: Absolute value, got it! Just enter a number and I'll give you its absolute value.")
        try:
            number = float(input("Enter the number: "))
            result = math.fabs(number)
            print(f"Result: {result}")
        except ValueError:
            print(f"{chatbot_name}: That's not a valid number bro 😅 Try again from start.")
        continue


    # Rock Paper Scissors
    if user_input in ["rock", "paper", "scissors", "play a game", "game", "let's play"]:
        if user_input in ["play a game", "game", "let's play"]:
            print(f"{chatbot_name}: Let's play Rock-Paper-Scissors! Type rock, paper or scissors.")
            continue
        # game logic remains same...
        moves = ["rock", "paper", "scissors"]
        bot_move = random.choice(moves)
        print(f"{chatbot_name}: I chose {bot_move}!")
        if user_input == bot_move:
            print(f"{chatbot_name}: It's a tie! 😮")
        elif (user_input == "rock" and bot_move == "scissors") or (user_input == "paper" and bot_move == "rock") or (user_input == "scissors" and bot_move == "paper"):
            print(f"{chatbot_name}: You win! 🎉")
        else:
            print(f"{chatbot_name}: I won! Better luck next time 😎")
        continue

    # Weather
    if "weather" in user_input:
        print(f"{chatbot_name}: I wish I could tell you the weather but I don't have internet yet 🌤️")
        continue

    # Multiplication Table
    if user_input == "table":
        try:
            num = int(input("Enter the number: "))
            print(f"{chatbot_name}: Multiplication table of {num}:")
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print(f"{chatbot_name}: Please enter a valid number 😅")
