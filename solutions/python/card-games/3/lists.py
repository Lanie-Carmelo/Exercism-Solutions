"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int, count: int = 3) -> list[int]:
    """Create a list containing the current round number and the next rounds.

    :param number: int - current round number.
    :param count: int - number of rounds to generate (default is 3).
    :return: list[int] - list of consecutive round numbers starting at `number`.
    """
    return list(range(number, number + count))


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list[int] - first rounds played.
    :param rounds_2: list[int] - second set of rounds played.
    :return: list[int] - all rounds played.
    """
    combined_rounds = rounds_1.copy()
    combined_rounds.extend(rounds_2)
    return combined_rounds


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list[int] - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and return the average card value from the list.

    :param hand: list[int] - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) ==
    calculated average.

    :param hand: list[int] - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    true_average = card_average(hand)
    return true_average in (first_last_average, middle_card)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed
    card values).

    :param hand: list[int] - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    average_even = card_average(even_cards)
    average_odd = card_average(odd_cards)
    return average_even == average_odd


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list[int] - cards in hand.
    :return: list[int] - hand with Jacks (if present) value doubled.
    """
    new_hand = hand.copy()
    if new_hand[-1] == 11:
        new_hand[-1] *= 2
    return new_hand
