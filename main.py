import random, math, time, datetime, json

try:
    with open("./question.json", "r", encoding="UTF-8") as file:
        letter = json.load(file)
except FileNotFoundError:
    letter = {}

def shuffle_list(lst):
    shuffled_list = list(lst.copy())
    for i in range(len(shuffled_list)):
        j = random.randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    return shuffled_list

data, quest, correct, start = shuffle_list(letter), 0, 0, time.time()
for char in data:
    quest += 1
    question = input(str(quest) + ". " + char + " : ")
    if (str.lower(letter[char]) == str.lower(question)):
      print(f"{quest}. Correct!")
      correct += 1
    else:
      print(f"{quest}. Incorrect! The answer is {char}({letter[char]}) ")
end = time.time()
print(f"Correct Answer: {correct}/{len(letter)} | Time elapsed: {str(datetime.timedelta(seconds=math.floor(end - start)))}")
print(f"Marks: {str(math.floor((correct/len(letter)) * 100))}/100")