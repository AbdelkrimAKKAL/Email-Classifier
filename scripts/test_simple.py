import requests

BASE_URL = "http://127.0.0.1:8000"

def run_classify_test(text):
    payload = {"content": text}
    try:
        response = requests.post(f"{BASE_URL}/classify", json=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"--- SUCCESS ---")
            print(f"Text: {text[:50]}...")
            print(f"Category: {result['category']}")
            print(f"Confidence: {result['confidence']}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    print("Testing Simple Email Classifier...")
    run_classify_test("Hello, I need help with my order #123.")
    run_classify_test("WIN A FREE IPHONE NOW! CLICK HERE!")
