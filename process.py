import sys
import math
import random


def number_puzzle(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        # If the number is even, calculate its square root.
        return ['even',f"sqrt is {math.sqrt(number)}"]
    else:
        # If the number is odd, calculate its cube.
        return ['odd',f"cube is {number ** 3}"]

def text_puzzle(text):
    # Convert the text message to binary
    binary_list = []
    for char in text:
        ascii_code = ord(char)
        binary = format(ascii_code, '08b')
        binary_list.append(binary)
    binary_text = ' '.join(binary_list)

    # Count the number of vowels in the text message
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1

    return [binary_text, vowel_count]

def treasure_hunt():
    attempts = 5
    attempt_count = 0
    # Generate a random number between 1 and 100
    target = random.randint(1, 100)
    html_output = f"<p>- The secret number is {target}.</p>"
    
    # Loop through the attempts
    while attempt_count < attempts:
        guess = random.randint(1, 100)
        attempt_count += 1
        if guess == target:
            html_output += f"""
            <p>-Attempt {attempt_count}: {guess} (Correct!)</p>
            <p>You found the treasure in {attempt_count} attempts!</p>"""
            return html_output
        else:
            if guess > target:
                html_output += f"<p>-Attempt {attempt_count}: {guess} (Too high!)</p>"
            else:
                html_output += f"<p>-Attempt {attempt_count}: {guess} (Too low!)</p>"
    return html_output

if __name__ == "__main__":
    number = int(sys.argv[1])
    text = sys.argv[2]
    
    oddOrEven,number_result = number_puzzle(number)
    binary,vowel = text_puzzle(text)
    treasure_result = treasure_hunt()

    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Calculation Results</title>
    </head>
    <body>
    <h2>Number Puzzle:</h2>
    <p>- The number {number} is {oddOrEven}. Its {number_result}.</p>
    <h2>Text Puzzle:</h2>
    <p>- Binary: {binary}</p>
    <p>- Vowel Count: {vowel}</p>
    <h2>Treasure Hunt:</h2>
    {treasure_result}
    </body>
    </html>
    """
    print(f"{html_output}")
