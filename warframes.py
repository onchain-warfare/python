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

conversations = {
    "greeting": {
        "prompt": "Greetings Professor Falken.",
        "responses": {
            "Hello.": "feeling_inquiry",
        },
    },
    "feeling_inquiry": {
        "prompt": "How are you feeling today?",
        "responses": {
            "I'm fine. How are you?": "account_removal_inquiry",
        },
    },
    "account_removal_inquiry": {
        "prompt": "Excellent. It's been a long time. Can you explain the removal of your user account on June 23, 1973?",
        "responses": {
            "People sometimes make mistak": "game_offer",
        },
    },
    "game_offer": {
        "prompt": "Yes they do. Shall we play a game?",
        "responses": {
            "Love to. How about Global Themonuclear War?": "chess_suggestion",
        },
    },
    "chess_suggestion": {
        "prompt": "Wouldn't you prefer a good game of chess?",
        "responses": {
            "Later. Let's play Global Themonuclear War.": "agreement",
        },
    },
    "agreement": {
        "prompt": "Fine",
        "responses": {},
    },
}


def login():
    username = input("Login: ")
    if username == "Joshua":
        joshua()
    elif username == "Help Frames":
        print(
            "‘Frames’ refers to models, simulations and frames which have tactical and strategic applications.".upper()
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
    state = "greeting"

    while state:
        stage = conversations[state]
        print(stage["prompt"].upper())

        response = input("> ")

        while response not in {
            response_key
            for stage in conversations.values()
            for response_key in stage["responses"]
        }:
            print("Response not recognized by system\n --Try Again--".upper())
            response = input("> ")

        for stage_data in conversations.values():
            if response in stage_data["responses"]:
                state = stage_data["responses"][response]
                break

        if state == "agreement":
            print(conversations[state]["prompt"].upper())
            break


login()
