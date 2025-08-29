import re

# Mapping of words to numbers
num_words = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
    'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
    'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
}

scales = {
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,

    'tenths': 0.1,
    'hundredths': 0.01,
}

def text2num(text):
    text = text.lower().replace('-', ' ')
    words = re.findall(r'\w+', text)
    current = result = 0
    val = ""
    for word in words:
        if word == 'minus':
            val = "-"
            continue
        if word in num_words:
            current += num_words[word]
        elif word in scales:
            if current == 0:
                current = 1
            current *= scales[word]
            result += current
            current = 0
        elif word == 'and':
            if current !=0:
                result += current
            current = 0
            continue
        else:
            raise ValueError(f"Unknown number word: {word}")
    return val + "{:,}".format(result + current)

# Example usage:
if __name__ == "__main__":
    s = input("Enter a number in words: ")
    print(text2num(s))