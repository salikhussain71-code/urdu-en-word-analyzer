# Urdu-EN Word Frequency Analyzer

A Python command-line tool that analyzes word frequency in both English and Urdu Roman text. Built to solve a real problem for bilingual users in Pakistan.

## Problem
Most NLP tools ignore Urdu Roman script, which millions of Pakistanis use daily on WhatsApp, Facebook, and Twitter.

## Solution
This tool reads `.txt` files, counts word frequency using regex and `collections.Counter`, and exports results to CSV.

## Features
- Handles both English and Urdu Roman text
- Outputs top 10 most frequent words to terminal
- Exports results to `results.csv`
- UTF-8 support for Urdu characters

## How to Run
```bash
python analyzer.py sample_en.txt
python analyzer.py sample_urdu.txt
