# Simple product recommendation system based on user search history

# Sample product categories and recommendations
recommendations = {
    "soap": ["shampoo", "toothpaste", "body wash"],
    "mobile": ["mobile case", "screen protector", "earphones"],
    "toys": ["board games", "action figures", "puzzles"],
    "games": ["gaming console", "gamepad", "video games"],
    "laptop": ["laptop bag", "mouse", "keyboard"],
    "book": ["notebook", "pen", "bookmark"]
}

def recommend_products(search_term):
    search_term = search_term.lower()
    for key in recommendations:
        if key in search_term:
            print(f"Since you searched for '{key}', you might also like:")
            for item in recommendations[key]:
                print(f"- {item}")
            return
    print("Sorry, no recommendations found for your search.")

if __name__ == "__main__":
    user_input = input("Enter what you are searching for: ")
    recommend_products(user_input)