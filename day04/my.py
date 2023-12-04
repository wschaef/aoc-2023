# split lines by : and split second part by |
# and store in a dict
cards = []
for line in lines:
    line = line.split(": ")
    key = line[0]
    value = line[1].split(" | ")
    value = [v.strip().split() for v in value]
    value = [set(v) for v in value]
    # remove empty values for both parts
    cards.append({"key": key, "winning_numbers": value[0], "my_numbers": value[1]})

# iterate over all cards and count the matches
for card in cards:
    wins = 0
    for a in card["winning_numbers"]:
        if a in card["my_numbers"]:
            wins += 1
    card["wins"] = wins

# calculate the result for part 1
result_part1 = 0
for card in cards:
    wins = card["wins"]
    if wins > 0:
        result_part1 += 2 ** (wins - 1)

print("Part1", result_part1)

# calculate the result for part 2
result_part2 = 0
counts = {0: 1}
for i, card in enumerate(cards):
    wins = card["wins"]
    count = counts.get(i, 1)
    if wins > 0:
        for j in range(i + 1, i + wins + 1):
            counts[j] = counts.get(j, 1) + count
    result_part2 += count

print("Part2", result_part2)
