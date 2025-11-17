#!/usr/bin/env python3
"""
عميل AI بسيط لـ Termux
Simple AI Client for Termux
"""
import os
import sys

class SimpleAI:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.gemini_key = os.getenv('GEMINI_API_KEY')

    def chat_openai(self, message):
        """دردشة مع OpenAI"""
        if not self.openai_key:
            return "OpenAI API key غير محدد"

        import urllib.request
        import json

        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                'Authorization': f'Bearer {self.openai_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": message}],
                "max_tokens": 100
            }

            req = urllib.request.Request(url, json=data, headers=headers)
            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode())

            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"خطأ OpenAI: {e}"

    def chat_gemini(self, message):
        """دردشة مع Gemini"""
        if not self.gemini_key:
            return "Gemini API key غير محدد"

        import urllib.request

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_key}"
            data = {
                "contents": [{
                    "parts": [{"text": message}]
                }]
            }

            req = urllib.request.Request(url, json=data)
            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode())

            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"خطأ Gemini: {e}"

def main():
    ai = SimpleAI()

    print("🤖 عميل AI بسيط لـ Termux")
    print("اكتب 'exit' للخروج")
    print("=" * 30)

    while True:
        try:
            user_input = input("أنت: ").strip()

            if user_input.lower() in ['exit', 'quit', 'خروج']:
                print("وداعاً! 👋")
                break

            if not user_input:
                continue

            print("🤖 OpenAI: ", end="")
            response = ai.chat_openai(user_input)
            print(response[:150] + "..." if len(response) > 150 else response)

            print("🌟 Gemini: ", end="")
            response = ai.chat_gemini(user_input)
            print(response[:150] + "..." if len(response) > 150 else response)
            print()

        except KeyboardInterrupt:
            print("\nوداعاً! 👋")
            break
        except Exception as e:
            print(f"خطأ عام: {e}")

if __name__ == "__main__":
    main()
