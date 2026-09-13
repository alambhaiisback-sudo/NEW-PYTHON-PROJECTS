text = input("Enter a sentence: ")

words = len(text.split())
characters = len(text)
spaces = text.count(" ")

print("\n--- RESULT ---")
print("Words:", words)
print("Characters:", characters)
print("Spaces:", spaces)