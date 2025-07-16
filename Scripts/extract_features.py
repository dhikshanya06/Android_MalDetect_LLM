# File: extract_features.py
# Extract permissions, API calls, and strings from decompiled APK

import os
import xml.etree.ElementTree as ET

APK_FOLDER = '../Adware_Beauty'
FEATURES_OUT = '../features/extracted_features.json'

import json

def extract_permissions(manifest_path):
    permissions = []
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    for perm in root.findall('uses-permission'):
        name = perm.attrib.get('{http://schemas.android.com/apk/res/android}name')
        if name:
            permissions.append(name)
    return permissions

def extract_api_calls(smali_dir):
    api_calls = set()
    for root, _, files in os.walk(smali_dir):
        for file in files:
            if file.endswith(".smali"):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.strip().startswith("invoke") and '->' in line:
                            method = line.strip().split('->')[1].split('(')[0]
                            api_calls.add(method)
    return list(api_calls)

def extract_strings(xml_path, smali_dir):
    strings = set()
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for s in root.findall('string'):
            if s.text:
                strings.add(s.text)
    except:
        pass

    for root, _, files in os.walk(smali_dir):
        for file in files:
            if file.endswith(".smali"):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if 'const-string' in line:
                            parts = line.split(',')
                            if len(parts) > 1:
                                s = parts[1].strip().strip('"')
                                strings.add(s)
    return list(strings)

def main():
    manifest_path = os.path.join(APK_FOLDER, 'AndroidManifest.xml')
    smali_dir = os.path.join(APK_FOLDER, 'smali')
    strings_xml = os.path.join(APK_FOLDER, 'res', 'values', 'strings.xml')

    features = {
        'permissions': extract_permissions(manifest_path),
        'api_calls': extract_api_calls(smali_dir),
        'strings': extract_strings(strings_xml, smali_dir)
    }

    os.makedirs(os.path.dirname(FEATURES_OUT), exist_ok=True)
    with open(FEATURES_OUT, 'w', encoding='utf-8') as f:
        json.dump(features, f, indent=2)

    print("[+] Feature extraction complete.")

if __name__ == '__main__':
    main()