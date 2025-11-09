
import random
subjects=[
    "Rohit sharma",
    "virat kohli",
    "prime minister modi ji",
    "outo rikshaw driver",
    "mithali raj"
]

actions=[
    "playing",
    "enjoy life",
    "cancles",
    "order",
    "celebration",
    "eats",
    "declares war on"
]

places_or_things=[
    "in mumbai ",
    "in courte",
    "in ipl match",
    "india get",
    "hedrabad",
    "in ganga ghat"
]

#head line generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input=input("\nDo you want another headline? Yes or No:").strip()
    if user_input=="no":
        break
print("\nthanks for using the fake news headline generator . hav  e a fun day")