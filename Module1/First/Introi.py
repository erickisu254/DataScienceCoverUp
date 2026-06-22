number = "100"
int(number)

age = 20
name = "John"

print(f"Your name is {name} and your age is{age}")

def averageGpa(resultsA, resultsB, resultsC) -> float:
    sum = resultsA + resultsB + resultsC
    average = sum/3
    print(average)


finalResult = averageGpa(30, 40, 50)
print(f'Your final result is {finalResult}')

