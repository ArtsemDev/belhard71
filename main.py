def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]


if __name__ == "__main__":
    print(is_palindrome("hello"))
