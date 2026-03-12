def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """
    Return the first and last item in the list.
    If the list is empty return (None, None).
    """
    if len(items) == 0:
        return (None, None)

    return (items[0], items[-1])


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """
    Return up to size items starting from index start.
    """
    if start < 0 or start >= len(items):
        return []

    if size <= 0:
        return []

    return items[start:start + size]


def first_supply_index(items: list[object], target: object) -> int:
    """
    Return the first index of target or -1 if not found.
    """
    for i in range(len(items)):
        if items[i] == target:
            return i

    return -1


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """
    Return (count, first_index) of target.
    """
    count = 0
    first_index = -1

    for i in range(len(items)):
        if items[i] == target:
            count += 1
            if first_index == -1:
                first_index = i

    if count == 0:
        return (0, -1)

    return (count, first_index)


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """
    Return a new list with urgent_item added to the front.
    """
    return [urgent_item] + items