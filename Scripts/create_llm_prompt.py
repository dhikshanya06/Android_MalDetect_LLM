# File: create_llm_prompt.py
# Combine filtered features and summary into final LLM prompt

import json

TOP_FEATURES_FILE = '../features/top_features.json'
STRING_SUMMARY_FILE = '../features/strings_summary.txt'
LLM_PROMPT_FILE = '../outputs/final_prompt.txt'

with open(TOP_FEATURES_FILE, 'r', encoding='utf-8') as f:
    top_features = list(json.load(f).keys())

with open(STRING_SUMMARY_FILE, 'r', encoding='utf-8') as f:
    string_summary = f.read()

# Create final LLM prompt text
prompt = f"""
This application has the following notable features:

Permissions and APIs:
{', '.join(top_features)}

String Analysis:
{string_summary}

Based on this information, determine whether the app is malicious and explain why.
"""

with open(LLM_PROMPT_FILE, 'w', encoding='utf-8') as f:
    f.write(prompt)

print("[+] Final LLM input prompt created.")
