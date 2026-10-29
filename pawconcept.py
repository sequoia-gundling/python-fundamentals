"""
Princess Pawkour
Fundamentals Demo

Concept:
Princessy Crown has been overthrown by Sir Barks-a-lot and
banished to the Real World. She must collect Yarn Crystals
through pawkour challenges to return home.
"""

# -------------------
# VARIABLES
# -------------------

princess_name = "Princessy Crown"
villain_name = "Sir Barks-a-lot"
yarn_crystals = 0

print("🐱 PRINCESS PAWKOUR 🐱")
print(f"The evil {villain_name} has stolen the throne!")
print(f"Princess {princess_name} must return to Purrsia.\n")

# -------------------
# LIST
# -------------------

obstacles = [
    "Cardboard Box Canyon",
    "The Vacuum of Doom",
    "Mount Laundry",
]

print("Upcoming Pawkour Challenges:")

for obstacle in obstacles:
    print(f"- {obstacle}")

print()

# -------------------
# DICTIONARY
# -------------------

crystal_rewards = {
    "Cardboard Box Canyon": 1,
    "The Vacuum of Doom": 2,
    "Mount Laundry": 3
}

# -------------------
# FUNCTION
# -------------------

def attempt_pawkour(obstacle):
    """
    Complete a challenge and
    return the crystal reward.
    """

    reward = crystal_rewards[obstacle]

    print(f"🏃‍♀️ {princess_name} clears {obstacle}!")
    print(f"✨ Earned {reward} Yarn Crystal(s).\n")

    return reward


# -------------------
# LOOP
# -------------------

for obstacle in obstacles:
    yarn_crystals += attempt_pawkour(obstacle)

print(f"Total Yarn Crystals: {yarn_crystals}\n")

# -------------------
# CONDITIONALS
# -------------------

if yarn_crystals >= 6:
    print("🌟 The portal home begins to open!")
else:
    print("❌ Not enough crystals yet.")


# -------------------
# CLASS
# -------------------

class CatHero:

    def __init__(self, name, agility):
        self.name = name
        self.agility = agility

    def introduce(self):
        print(
            f"\n👑 Princess {self.name} enters the arena!"
        )

    def pawkour_move(self):

        if self.agility >= 90:
            print(
                "🐾 Performs a legendary triple-wall jump!"
            )

        elif self.agility >= 60:
            print(
                "🐾 Executes a graceful bookshelf leap!"
            )

        else:
            print(
                "📦 Gets distracted by a cardboard box."
            )


# -------------------
# OBJECT
# -------------------

whiskerina = CatHero(
    "Whiskerina",
    95
)

whiskerina.introduce()
whiskerina.pawkour_move()

# -------------------
# USER INPUT
# -------------------

print("\nFinal Challenge!")

answer = input(
    "Should Princess Princessy Crown confront Sir Barks-a-lot? (yes/no): "
)

if answer.lower() == "yes":
    print(
        "⚔️ Sir Barks-a-lot has been defeated!"
    )
    print(
        "🏰 Princess Princessy Crown reclaims the throne of Purrsia!"
    )
else:
    print(
        "🐱 She decides to train at Pawkour Academy first."
    )
