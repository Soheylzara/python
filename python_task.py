scores = [
    int(input("Enter Your score 1: ")),
    int(input("Enter Your score 2: ")),
    int(input("Enter Your score 3: ")),
    int(input("Enter Your score 4: ")),
    int(input("Enter Your score 5: "))
]
average = sum(scores) / len(scores)
minimum = min(scores)
maximum = max(scores)
variance = ((scores[0] - average) ** 2 +
            (scores[1] - average) ** 2 +
            (scores[2] - average) ** 2 +
            (scores[3] - average) ** 2 +
            (scores[4] - average) ** 2) / len(scores)
print("---------------------------------------")
print(f"Your average score: {average}")
print("---------------------------------------")
print(f"Your minimum score: {minimum}")
print("---------------------------------------")
print(f"Your maximum score: {maximum}")
print("---------------------------------------")
print(f"Your variance score: {variance}")
print("---------------------------------------")
