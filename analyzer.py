# =======================================================
# Bilingual Word Frequency Analyzer
# Author: Salik Hussain
# Date: July 2026
# CS50P Project 2
# =======================================================

import re
import csv
import sys
from collections import Counter

def get_top_words(text, top_n=10):
    """
    Takes text and returns the top N most common words.
    Works for both English and Urdu Roman script.
    """
    # 1. Make everything lowercase so 'The' and 'the' are same
    text = text.lower()
    
    # 2. Use regex to find words
    words = re.findall(r"[a-zA-Z0-9']+", text)
    
    # 3. Count how many times each word appears
    word_counts = Counter(words)
    
    # 4. Get the most common N words
    return word_counts.most_common(top_n)

def save_to_csv(word_list, filename):
    """
    Saves the word list to a CSV file
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Word', 'Frequency']) # header
            for word, count in word_list:
                writer.writerow([word, count])
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to run the program
    """
    print("=== Bilingual Word Frequency Analyzer ===")
    
    # Check if user gave a filename
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py filename.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    # Get top 10 words
    top_words = get_top_words(text)
    
    # Print to screen
    print("\nTop 10 Most Common Words:")
    print("-" * 25)
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i}. {word}: {count}")
    
    # Save to CSV
    save_to_csv(top_words, "results.csv")

if __name__ == "__main__":
    main()