import sys

scores = []
for arg in sys.argv[1:]:
    scores.append(float(arg))

if not scores:
    print("No valid scores provided, using default.")
    scores = [10, 20, 30, 40]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print(f"Scores: {scores}")
print(f"Sum of scores: {total}")
print(f"Average of scores: {average:.2f}")
print(f"Maximum score: {maximum}")
print(f"Minimum score: {minimum}")
