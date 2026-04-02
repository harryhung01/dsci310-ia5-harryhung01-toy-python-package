def split_once(text: str, sep: str) -> list[str]:
    """Split a single string into a list using the provided separator."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(sep, str):
        raise TypeError("sep must be a string")
    return text.split(sep)
