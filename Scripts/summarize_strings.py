# File: summarize_strings.py
# Generate summary from extracted strings using simple rules (mock LLM)

import json

FEATURES_FILE = '../features/extracted_features.json'
STRINGS_SUMMARY_OUT = '../features/strings_summary.txt'

with open(FEATURES_FILE, 'r', encoding='utf-8') as f:
    features = json.load(f)

# Mock summarization (you could call an LLM API here)
def summarize(strings):
    suspicious_keywords = [s for s in strings if 'sms' in s.lower() or 'apk' in s.lower() or 'track' in s.lower()]
    if not suspicious_keywords:
        return "No suspicious behavior detected in strings."
    return f"Suspicious indicators found: {', '.join(suspicious_keywords)}"

summary = summarize(features.get('strings', []))

with open(STRINGS_SUMMARY_OUT, 'w', encoding='utf-8') as f:
    f.write(summary)

print("[+] String summary created.")
