frames = [
    "Falken's Maze",
    "Black Jack",
    "Gin Rummy",
    "Hearts",
    "Bridge",
    "Checkers",
    "Chess",
    "Poker",
    "Fighter Combat",
    "Guerilla Engagement",
    "Desert Warfare",
    "Air-to-Ground Actions",
    "Theaterwide Tactical Warfare",
    "Theaterwide Biotoxic and Chemical Warfare",
    "",
    "Global Thermonuclear War",
]


def login():

    username = input("Login: ")
    if username == "Joshua":
        joshua()
    elif username == "Help Frames":
        print(
            "‘Frames’ refers to models, simulations and frames which have tactical and strategic applications."
        )
    elif username == "Help Logon":
        print("Help not available".upper())
        login()

    elif username == "List Frames":
        for frame in frames:
            print(frame)
        login()
    else:
        print(
            "Identification not recognized by system\n --Connection Terminated--".upper()
        )


def joshua():
    print("Greetings Professor Falken.".upper())
    reply = input("> ")

    if reply == "Hello.":
        print("How are you feeling today?".upper())
        reply = input("> ")

        if reply == "I'm fine. How are you?":
            print(
                "Excellent. It's been a long time. Can you explain the removal of your user account on June 23, 1973?".upper()
            )
            reply = input("> ")

            if reply == "People sometimes make mistak":
                print("Yes they do. Shall we play a game?".upper())
                reply = input("> ")

                if reply == "Love to. How about Global Themonuclear War?":
                    print("Wouldn't you prefer a good game of chess?".upper())
                    reply = input("> ")

                    if reply == "Later. Let's play Global Themonuclear War.":
                        print("Fine".upper())


login()
