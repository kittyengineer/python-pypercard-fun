from pypercard import Inputs, Card, CardApp
import sys


def to_exit(data_store, form_data):
    sys.exit(0)

stack = [
    Card(
        "Home",
        text="You're leaving the comfort of your home to go trick or treating ...",
        buttons=[
            {"label": "go left", "target": "Elm Street left"},
            {"label": "go right", "target": "Elm Street right"},
        ],
    ),

    Card(
        "Elm Street left",
        text="The street is strangely quiet. Where do you want to go from here ...",
        buttons=[
            {"label": "house 1", "target": "Dead End"},
            {"label": "house 2", "target": "Toothbrush house"},
            {"label": "house 3", "target": "Dead End"},
            {"label": "forward", "target": "Park"},
        ],
    ),

    Card(
        "Toothbrush house",
        text="The house door creaks open, light hits your gaze, and you are hit by something hard. It bounces off your head and falls to the ground. Ew.. A toothbrush.",
        auto_advance=3,
        auto_target="Elm Street left"
    ),


    Card(
        "Park",
        text="The street ends in a park filled with gloom and whistles from the wind. To the right there is an old house that looks abandoned. To the left is a house that looks inviting. There is a light on in the window.",
        buttons=[
            {"label": "approach abandoned house", "target": "Haunted House"},
            {"label": "approach house with light", "target": "Happy House"},
        ]
    ),

    Card(
        "Haunted House",
        text="The abandon house seems to groan. It smells of rotting meat. Enter?",
        buttons=[
            {"label": "open door", "target": "Dead End"},
            {"label": "go back", "target": "Park"},
        ]
    ),

    Card(
        "Happy House",
        text="As you approach you here some music playing inside and there is a smell of pop corn in the air.",
        buttons=[
            {"label": "knock on door", "target": "Elderly Lady"},
            {"label": "go back", "target": "Park"},
        ]
    ),


    Card(
        "Elderly Lady",
        text="Music spills out onto the porch as an elderly lady opens the door. What do you do?",
        buttons=[
            {"label": "run in fear", "target": "Park"},
            {"label": "trick or treat!", "target": "Trick or Treat"},
        ]
    ),

    Card(
        "Trick or Treat",
        text="She throws much candy and money into your bag. You win!!!",
        text_color="white",
        background="orange",
        auto_advance=5,
        auto_target=to_exit
    ),

    Card(
        "Elm Street right",
        text="You come to a dead end with an old home in front of you. There's a pond and shed on the property.",
        buttons=[
            {"label": "approach house", "target": "Dead End"},
            {"label": "check pond", "target": "Dead End"},
            {"label": "open shed", "target": "Dead End"},
        ],
    ),

    Card(
        "Dead End",
        text="Suddenly everything goes dark. You feel a moment of panic as the cold embrace of death takes hold of your mortality. THE END.",
        text_color="black",
        background="red",
        auto_advance=5,
        auto_target=to_exit
    )

]



app = CardApp("Halloween Trick or Treat!", stack=stack)
app.run()
