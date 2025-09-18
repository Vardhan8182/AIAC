from collections import Counter

def top_3_frequent_words(text):
    # Step 1: Normalize the text
    words = text.lower().split()
    
    # Step 2: Count frequencies of each word
    word_count = Counter(words)
    
    # Step 3: Sort words first by count (descending), then lexicographically (ascending) if counts are tied
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Step 4: Return the top 3 words
    return sorted_words[:3]

# Example usage
sample_text = "to be or not to be that is the question" 
""
output = top_3_frequent_words(sample_text)
print(output)
