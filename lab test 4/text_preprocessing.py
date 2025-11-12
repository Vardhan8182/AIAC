"""
Text Preprocessing Script
==========================
This script demonstrates:
1. Generating random review text data
2. Removing special characters and numbers from reviews
3. Converting text to lowercase and removing stop words
"""

import pandas as pd
import numpy as np
import re
import string
from nltk.corpus import stopwords
import nltk

# Download required NLTK data
print("Downloading NLTK data...")
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# ============================================
# PART 1: Generate Random Review Data
# ============================================

print("\n" + "="*60)
print("PART 1: GENERATING RANDOM REVIEW DATA")
print("="*60)

# Sample reviews with various text patterns
sample_reviews = [
    "This product is AMAZING! 5/5 stars. Worth every penny!!!",
    "Terrible experience. Product broke after 2 days... Not recommended @all",
    "Great quality & excellent customer service. 10/10 would buy again!",
    "Bad packaging. Item arrived damaged. #disappointed #waste123",
    "Love it! Fast shipping & perfect condition. A+ seller!!!",
    "Meh, it's okay. Nothing special but does the job. 3/3.5 stars.",
    "Absolutely horrible! Waste of $50. DO NOT BUY!!!",
    "Fantastic product! Exceeded my expectations. Highly recommended!!!",
    "Disappointing quality. Expected better for the price... :((((",
    "Outstanding service! Product arrived quickly & in perfect condition.",
    "Not worth it. Poor quality & bad design. Return ASAP!!!",
    "Wonderful! Best purchase I've made this year. 5 stars!!!",
    "Okay product, average quality. Could be better for this price point.",
    "Excellent value for money! Great features & solid build quality!!!",
    "Worst product ever!!! Save your money & buy something else!",
]

# Create a DataFrame with review data
np.random.seed(42)
num_reviews = 15

data = {
    'ReviewID': range(1, num_reviews + 1),
    'Product': np.random.choice(['Laptop', 'Phone', 'Headphones', 'Camera'], num_reviews),
    'Review': sample_reviews,
    'Rating': np.random.randint(1, 6, num_reviews)
}

df = pd.DataFrame(data)

print("\nOriginal Reviews Dataset:")
print(df.to_string(index=False))
print(f"\nTotal reviews: {len(df)}")

# ============================================
# PART 2: Remove Special Characters and Numbers
# ============================================

print("\n" + "="*60)
print("PART 2: REMOVING SPECIAL CHARACTERS & NUMBERS")
print("="*60)

def remove_special_chars_and_numbers(text):
    """
    Remove special characters and numbers from text.
    Keeps only alphabetic characters and spaces.
    """
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove special characters (keep only letters, spaces, and apostrophes)
    text = re.sub(r'[^a-zA-Z\s\']', '', text)
    
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Apply the function to create a new column
df['Review_Cleaned_V1'] = df['Review'].apply(remove_special_chars_and_numbers)

print("\nAfter Removing Special Characters & Numbers:")
print(df[['ReviewID', 'Review', 'Review_Cleaned_V1']].head(10).to_string(index=False))

# ============================================
# PART 3: Convert to Lowercase & Remove Stop Words
# ============================================

print("\n" + "="*60)
print("PART 3: LOWERCASE & REMOVE STOP WORDS")
print("="*60)

# Get English stop words
stop_words = set(stopwords.words('english'))

print(f"\nTotal stop words in English: {len(stop_words)}")
print(f"Sample stop words: {list(stop_words)[:20]}")

def preprocess_text(text):
    """
    Complete preprocessing:
    1. Remove special characters and numbers
    2. Convert to lowercase
    3. Remove stop words
    """
    # Step 1: Remove special characters and numbers
    text = remove_special_chars_and_numbers(text)
    
    # Step 2: Convert to lowercase
    text = text.lower()
    
    # Step 3: Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    # Step 4: Join back into a single string
    text = ' '.join(filtered_words)
    
    return text

# Apply complete preprocessing
df['Review_Preprocessed'] = df['Review'].apply(preprocess_text)

print("\nAfter Complete Preprocessing (Lowercase + Stop Words Removal):")
print(df[['ReviewID', 'Review', 'Review_Preprocessed']].head(10).to_string(index=False))

# ============================================
# PART 4: Detailed Comparison & Statistics
# ============================================

print("\n" + "="*60)
print("PART 4: PREPROCESSING STATISTICS")
print("="*60)

# Calculate statistics
df['Original_Length'] = df['Review'].str.split().str.len()
df['Cleaned_V1_Length'] = df['Review_Cleaned_V1'].str.split().str.len()
df['Preprocessed_Length'] = df['Review_Preprocessed'].str.split().str.len()

df['Words_Removed'] = df['Original_Length'] - df['Preprocessed_Length']
df['Removal_Percentage'] = (df['Words_Removed'] / df['Original_Length'] * 100).round(2)

print("\nWord Count Comparison:")
print(df[['ReviewID', 'Original_Length', 'Cleaned_V1_Length', 
          'Preprocessed_Length', 'Words_Removed', 'Removal_Percentage']].to_string(index=False))

print(f"\n\nAverage words removed per review: {df['Words_Removed'].mean():.2f}")
print(f"Average removal percentage: {df['Removal_Percentage'].mean():.2f}%")

# ============================================
# PART 5: Detailed Example with Step-by-Step
# ============================================

print("\n" + "="*60)
print("PART 5: DETAILED EXAMPLE (Step-by-Step Preprocessing)")
print("="*60)

example_review = df['Review'].iloc[0]
print(f"\nOriginal Review:")
print(f"  {example_review}")

step1 = remove_special_chars_and_numbers(example_review)
print(f"\nAfter removing special characters & numbers:")
print(f"  {step1}")

step2 = step1.lower()
print(f"\nAfter converting to lowercase:")
print(f"  {step2}")

words = step2.split()
filtered = [w for w in words if w not in stop_words]
step3 = ' '.join(filtered)
print(f"\nAfter removing stop words:")
print(f"  {step3}")
print(f"\nStop words removed: {set(words) - set(filtered)}")

# ============================================
# PART 6: Export Results to CSV
# ============================================

print("\n" + "="*60)
print("PART 6: EXPORTING RESULTS")
print("="*60)

# Create output DataFrame
output_df = df[['ReviewID', 'Product', 'Rating', 'Review', 
                'Review_Cleaned_V1', 'Review_Preprocessed', 'Original_Length', 
                'Preprocessed_Length', 'Removal_Percentage']].copy()

output_file = r"c:\Users\kavati dikshitha\OneDrive\Desktop\AIAC\lab test-4\preprocessed_reviews.csv"
output_df.to_csv(output_file, index=False)

print(f"\n✓ Results exported to: {output_file}")
print(f"✓ Total records processed: {len(output_df)}")

# ============================================
# PART 7: Word Frequency Analysis
# ============================================

print("\n" + "="*60)
print("PART 7: WORD FREQUENCY ANALYSIS (Top 15 Words)")
print("="*60)

from collections import Counter

# Get all words from preprocessed reviews
all_words = []
for review in df['Review_Preprocessed']:
    all_words.extend(review.split())

word_freq = Counter(all_words)
top_words = word_freq.most_common(15)

print("\nMost frequent words in preprocessed reviews:")
for i, (word, count) in enumerate(top_words, 1):
    print(f"  {i:2d}. {word:15s} - {count:3d} times")

# ============================================
# PART 8: Summary Report
# ============================================

print("\n" + "="*60)
print("SUMMARY REPORT")
print("="*60)

print(f"""
Dataset Statistics:
  - Total reviews processed: {len(df)}
  - Products covered: {df['Product'].nunique()}
  - Average rating: {df['Rating'].mean():.2f}/5

Text Preprocessing Results:
  - Average original words per review: {df['Original_Length'].mean():.2f}
  - Average preprocessed words per review: {df['Preprocessed_Length'].mean():.2f}
  - Average words removed: {df['Words_Removed'].mean():.2f} ({df['Removal_Percentage'].mean():.2f}%)
  
Processing Details:
  - Special characters removed: Yes
  - Numbers removed: Yes
  - Converted to lowercase: Yes
  - Stop words removed: Yes ({len(stop_words)} stop words)
  - Extra spaces cleaned: Yes

Output Files:
  - CSV with results: preprocessed_reviews.csv
""")

print("✓ Script completed successfully!\n")