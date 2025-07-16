# File: mutual_info_filter.py
# Apply mutual information filtering on binary feature vectors

import json
import pandas as pd
from sklearn.feature_selection import mutual_info_classif

FEATURES_FILE = '../features/extracted_features.json'
LABEL = 1  # 1 = malware, 0 = benign (set manually for now)
OUT_TOP_FEATURES = '../features/top_features.json'

# Load feature data (single APK for now)
with open(FEATURES_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Simulate feature matrix for one APK (binary vectors)
all_features = list(set(data['permissions'] + data['api_calls']))
X = pd.DataFrame([[1] * len(all_features)], columns=all_features)
Y = [LABEL]  # single-label entry for now

# Apply mutual information (dummy for 1-sample)
# For real batch use: aggregate multiple APKs and labels
mi = pd.Series([1]*len(all_features), index=X.columns)  # placeholder since MI needs >1 sample

# Select top N (simulate)
top_features = mi.sort_values(ascending=False).head(20)

with open(OUT_TOP_FEATURES, 'w', encoding='utf-8') as f:
    json.dump(top_features.to_dict(), f, indent=2)

print("[+] Top features selected using mutual information (placeholder)")
