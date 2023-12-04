def process_lines(lines):
    cards = []
    for line in lines:
        key, value = line.split(": ")
        value_parts = [set(v.strip().split()) for v in value.split(" | ")]
        cards.append(
            {
                "key": key,
                "winning_numbers": value_parts[0],
                "my_numbers": value_parts[1],
            }
        )
    return cards


def count_wins(cards):
    for card in cards:
        card["wins"] = sum(
            1 for number in card["winning_numbers"] if number in card["my_numbers"]
        )


def calculate_result_part1(cards):
    return sum(2 ** (card["wins"] - 1) for card in cards if card["wins"] > 0)


def calculate_result_part2(cards):
    result = 0
    counts = {0: 1}
    for i, card in enumerate(cards):
        count = counts.get(i, 1)
        if card["wins"] > 0:
            for j in range(i + 1, i + card["wins"] + 1):
                counts[j] = counts.get(j, 1) + count
        result += count
    return result


cards = process_lines(lines)
count_wins(cards)
result_part1 = calculate_result_part1(cards)
result_part2 = calculate_result_part2(cards)

print("Part1", result_part1)
print("Part2", result_part2)
