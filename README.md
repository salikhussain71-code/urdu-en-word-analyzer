# Bilingual Word Frequency Analyzer (Urdu + English)

A Python tool that reads a text file containing English or Roman Urdu text, counts how often each word appears, and outputs the top 10 most frequent words to a CSV file.

## Why I Built This

This is early groundwork for a bigger research idea I'm working toward: PAKGOV-RAG, a bilingual Urdu-English retrieval system for Pakistani government documents. Before building anything with embeddings or retrieval, I wanted to understand basic text processing first — how to clean raw text, tokenize it, and count frequency, since that's the foundation any NLP pipeline sits on.

Roman Urdu (Urdu written in Latin script, e.g. "main seekh raha hun") is common in everyday Pakistani text but rarely gets dedicated tooling. This analyzer works on it directly since it doesn't rely on Urdu script libraries — just Latin-character regex, which both English and Roman Urdu use.

## What It Does

- Reads any `.txt` file (English or Roman Urdu)
- Lowercases text and extracts words using regex (`[a-z]+`)
- Counts frequency using `collections.Counter`
- Prints the top 10 most frequent words
- Saves the full ranked list to `output/results.csv`
- Raises custom exceptions if the file is missing or empty, instead of crashing

## How It Works

1. `read_file()` opens the file in UTF-8 and raises `FileNotFoundInAnalyzerError` if the path doesn't exist
2. `clean_and_split()` lowercases the text and uses `re.findall(r"[a-z]+", text)` to pull out words, ignoring punctuation and numbers. Raises `EmptyFileError` if nothing is found
3. `count_words()` wraps the word list in a `Counter`, which handles frequency counting in one line
4. `get_top_words()` calls `.most_common(n)` on the counter to get the top results
5. `save_to_csv()` writes word-count pairs to `output/results.csv` using the `csv` module

## Concepts Used (CS50P)

- File I/O (reading and writing files)
- Regular expressions (`re.findall`)
- Dictionaries / `collections.Counter`
- Custom exceptions

## How to Run
