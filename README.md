# Words-to-digits

A simple Python script to convert numbers written in English words into their digit (numeric) form.

## Features

- Converts numbers like `"one thousand two hundred thirty four"` to `1,234`
- Supports negative numbers (e.g., `"minus five hundred"`)
- Handles large numbers (thousand, million, billion, etc.)
- Supports fractional numbers (e.g., `"three hundredths"` → `0.03`)
- Ignores the word `"and"` for natural phrasing

## Usage

1. Clone or download this repository.
2. Run the script:

   ```
   python "import re.py"
   ```

3. Enter a number in words when prompted.

   **Example:**
   ```
   Enter a number in words: two thousand and nineteen and three hundredths
   2,019.03
   ```

## File

- `import re.py` — Main script for converting words to digits.

## License

This project is open source and free
