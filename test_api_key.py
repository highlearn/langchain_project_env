from openai import OpenAI
import os

# ✅ Step 1: Set your API key here OR in environment variable
# You can either:
# Option 1: Hardcode temporarily (for testing only)
# client = OpenAI(api_key="your_api_key_here")

# Option 2 (Recommended): Use environment variable
#    setx OPENAI_API_KEY "your_api_key_here"   <-- Run this once in Windows Command Prompt
# Then just do:
client = OpenAI()

# ✅ Step 2: Simple test call
try:
    response = client.models.list()
    print("✅ API key works! Connection successful.")
    print("Here are some available models:")
    for model in response.data[:5]:  # show only first 5
        print(" -", model.id)
except Exception as e:
    print("❌ Error: API key might be invalid or not set correctly.")
    print("Details:", e)