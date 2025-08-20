def analyze_review():
    positive_keywords = ['good', 'great', 'excellent', 'amazing', 'fantastic', 'love', 'wonderful', 'best', 'awesome', 'positive']
    negative_keywords = ['bad', 'terrible', 'awful', 'worst', 'hate', 'poor', 'disappointing', 'negative', 'boring', 'horrible']

    review = input("Enter your review: ").lower()
    pos_count = sum(word in review for word in positive_keywords)
    neg_count = sum(word in review for word in negative_keywords)

    if pos_count > neg_count:
        print("Positive review")
    elif neg_count > pos_count:
        print("Negative review")
    else:
        print("Unable to determine sentiment")

# Example usage
if __name__ == "__main__":
    analyze_review()