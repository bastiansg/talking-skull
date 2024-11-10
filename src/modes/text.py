from .morse_map import morse_map


def normalize_text(text: str) -> str:
    text = " ".join(text.split())
    return text


def get_encoded_chars(word: str, char_pause_symbol: str) -> str:
    encoded_chars = f"{char_pause_symbol}".join(
        morse_map[char] for char in word
    )

    return encoded_chars
