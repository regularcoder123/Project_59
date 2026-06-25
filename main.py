import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(Fore.GREEN + "Welcome User! Type anything and I will analyze your mood and give you a curated response!")
name = input("What is your name?:")
if not name:
    name = "Mystery"
    print("Hello Mystery!")
else:
    print(f"Hello {name}")
while True:
    user_mood = input("Type Your Sentence Here:")
    polarity = TextBlob(user_mood).sentiment.polarity
    if polarity > 0.25:
        print("Mood Detected: Positive")
        print("According to my complicated robot brain, I think you are happy!")
        sport =input("Since Your happy, whats your favourite sport?:")
        print(f"I like {sport} too!")
       
    elif polarity < -0.25:
        print("Mood Detected: Negative ")
        print("Aww, I hope you feel better")
        sad_song = input("Since I feel you are sad, what is your favourite sad song?:")
        print(f"I like to listen to {sad_song} too sometimes")
    else:
        print("Mood Detected: Neutral ")
        print("At least your not sad!")

    quit = input("Do you want to continue? (y/n)")
    if quit.lower() == "quit":
        print("Thanks for chatting with me!")
        break
    else:
        continue


