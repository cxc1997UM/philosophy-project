import matplotlib.pyplot as plt

TRAIN_SPRITE = r"""
     ______
 ___/|__|__|\
|  _       _  |
|_| |_____| |_|
"""

LEVER_PULLER_SPRITE = r"""
   O
  /|\
  / \
"""

NARRATOR_SPRITE = r"""
  .---.
 | :)  |
  '---'
"""

EMPTY_TRACK = r"""
Empty Track (Safe):
  _____________________
 |                     |
 |                     |
 |_____________________|
"""

TRACK_WITH_PEOPLE = r"""
Track with 5 People:
  _____________________
 |   :)  :)  :)  :)  :)  |
 |                     |
 |_____________________|
"""

def explain_utilitarianism(outcome):
    if outcome == "good":
        print("\n[Guide]: Great move! By pulling the lever, you rerouted the train to the empty track. No one died—that's utilitarian thinking, maximizing overall happiness!")
    else:
        print("\n[Guide]: Oops, not so good. Not pulling the lever left the train on the track with people. Five lives were lost, and overall happiness was not maximized.")

def show_happiness_diagram(outcome):
    outcomes = ["Pull Lever", "Don't Pull"]
    
    if outcome == "good":
        happiness_levels = [100, 0]  # Pulling lever saves 5 people → high happiness
    else:
        happiness_levels = [0, 100]  # Not pulling means 5 people die → low happiness
    
    plt.figure(figsize=(6, 4))
    bars = plt.bar(outcomes, happiness_levels, color=["green", "red"])
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height - 10, f"{height}",
                 ha="center", va="center", color="white", fontsize=12)
    
    plt.ylim(0, 120)
    plt.title("Happiness Levels Based on Your Decision")
    plt.xlabel("Decision")
    plt.ylabel("Happiness Level")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def main():

    print("Welcome to the Train Meme Utilitarian Dilemma!")
    print("\n[Narrator Sprite]:")
    print(NARRATOR_SPRITE)
    
    while True:
        print("\n[Narrator]: There's a runaway train approaching!")
        print("[Train Sprite]:")
        print(TRAIN_SPRITE)
        print("[Narrator]: Standing by the lever is our brave Lever Puller:")
        print(LEVER_PULLER_SPRITE)
        print("[Narrator]: Ahead of the train, there are two tracks:")
        print("Track Option 1 (Safe):")
        print(EMPTY_TRACK)
        print("Track Option 2 (Danger):")
        print(TRACK_WITH_PEOPLE)
        
        choice = input("\n[Narrator]: Do you pull the lever to redirect the train to the safe, empty track? (yes/no): ").strip().lower()
        
        if choice == "yes":
            leverPulled = True
            outcome = "good"
            print("\n[Narrator]: You pulled the lever! The train is now headed towards the safe, empty track:")
            print(EMPTY_TRACK)
        else:
            leverPulled = False
            outcome = "bad"   # Train stays on the track with people
            print("\n[Narrator]: You didn't pull the lever. The train stays on course, heading towards the track with people:")
            print(TRACK_WITH_PEOPLE)
        
        explain_utilitarianism(outcome)
        
        show_happiness_diagram(outcome)
        
        play_again = input("\n[Narrator]: Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\n[Narrator]: Thanks for playing!")
            break

if __name__ == "__main__":
    main()
