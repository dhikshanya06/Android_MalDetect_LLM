import json
import os

input_samples = [
    {
        "instruction": "Determine whether the app is malicious and explain why.",
        "input": "Permissions and APIs: android.permission.ACCESS_FINE_LOCATION, android.permission.SYSTEM_OVERLAY_WINDOW\nStrings: apk_md5, getDexElements",
        "output": "This app is likely malicious due to sensitive permissions like SYSTEM_OVERLAY_WINDOW and presence of suspicious strings like apk_md5."
    },
    {
        "instruction": "Determine whether the app is malicious and explain why.",
        "input": "Permissions and APIs: android.permission.READ_SMS, SmsManager.sendTextMessage\nStrings: 'sms_send', 'premium_service'",
        "output": "This app is malicious due to SMS abuse and suspicious API usage."
    }
]

os.makedirs("data", exist_ok=True)

with open("data/maldetect_dataset.jsonl", "w", encoding="utf-8") as f:
    for item in input_samples:
        f.write(json.dumps(item) + "\n")
