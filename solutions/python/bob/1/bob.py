"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited. This function takes a string and returns Bob's response to it.
"""

def response(hey_bob: str) -> str:
    """
    Returns Bob's response to the given input string.
    Args:
        hey_bob (str): The input string to which Bob will respond.
    Returns:
        str: Bob's response to the input string.
    """
    stripped_hey_bob = hey_bob.strip()
    if stripped_hey_bob.endswith("?") and stripped_hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if stripped_hey_bob.endswith("?"):
        return "Sure."
    if stripped_hey_bob.isupper():
        return "Whoa, chill out!"
    if stripped_hey_bob == "":
        return "Fine. Be that way!"
    return "Whatever."
