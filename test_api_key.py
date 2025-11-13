# test_anthropic_key.py
# Simple code to test Anthropic API key directly in Python
# Install library first: pip install anthropic

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# 👇 Paste your Anthropic API key here
ANTHROPIC_API_KEY = "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"

# Initialize client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# Prepare a tiny test prompt
prompt = f"{HUMAN_PROMPT} Say 'OK'. {AI_PROMPT}"

try:
    response = client.completions.create(
        model="claude-3.5",          # You can change to claude-3-opus or claude-3-sonnet if available
        prompt=prompt,
        max_tokens_to_sample=5       # small response
    )

    print("✅ API key works! Response from model:")
    print(response.completion.strip())

except Exception as e:
    print("❌ Something went wrong:")
    print(e)