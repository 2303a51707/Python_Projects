import random
import game_data
import art

print(art.logo)

celebrities = game_data.data

def random_celeb():
    return random.choice(celebrities)

def format_celeb(celeb):
    return f"{celeb['name']}, a {celeb['description']}"

def higher_lower_game():
    score = 0
    game_continue = True

    celeb_a = random_celeb()
    celeb_b = random_celeb()
    while celeb_a == celeb_b:
        celeb_b = random_celeb()

    while game_continue:
        print(f"\nCompare A: {format_celeb(celeb_a)}")
        print(art.vs)
        print(f"Compare B: {format_celeb(celeb_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_followers = celeb_a["followers"]
        b_followers = celeb_b["followers"]

        if (a_followers > b_followers and guess == "A") or \
           (b_followers > a_followers and guess == "B"):
            score += 1
            print(f" You're right! Current score: {score}")
            celeb_a = celeb_b
            celeb_b = random_celeb()
            while celeb_a == celeb_b:
                celeb_b = random_celeb()
        else:
            print(f" Sorry, that's wrong. Final Score: {score}")
            print(f"A had {a_followers}M and B had {b_followers}M followers.")
            game_continue = False

higher_lower_game()
