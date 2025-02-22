#1:Set up logic statement with boolean variable (only can be true/false)
from operator import truediv
isSunny = False

if isSunny:
    print('It is beautiful out!') # this will not run because the condition is false
else:
    print('No! It is snowing out!') # this will run because the if statement was not executed

#2: # "for" loops --> w/ 1 argument treated as stop value, 2 argument treated as start and stop, 3 arguments treated as start, stop, and step.
for x in range(7):
    print(x)
for x in range(1,4):
    print(x)
for x in range(0,100, 10):
    print(x)
#3: # While loops, loops that itirates when a specific condition is met, you can also control the intervals of counting
count = 0
while count <5:
    print(count)
    count+= 2

count = 5
while count <25:
    print(count)
    count+= 5

#4: breaking a loop
count = 0
while True:
    print(count)
    count+= 1
    if count > 10:
        break

for x in range(10): #using "%' I can check if a number in the range is divisible by three, and skip tho numbers in the output
    if x % 3 == 0:
        continue
    print(x)

#5:practicing inputs() and print()
name = ("Mia Lynne Hensgen")
print(name + " is learning how to code!")

C6H12 = ("Cyclohexane")
C8H14 = ("Cyclooctane")
print (C6H12 + " has less angle strain than " + C8H14)
#6:practicing storing info in dictionaries
grades = {
    "Bio" : "A",
    "Data" : "A",
    "Orgo" : "C",
    "Lab" : "A",
    "English" : "-A",
    "History" : "A"
}
print(grades)

grades = {
    "Bio" : "A",
    "Data" : "A",
    "Orgo" : "C",
    "Lab" : "A",
    "English" : "-A",
    "History" : "A"
}
del grades["Orgo"]
print(grades)
#7:making a claculator
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Division by zero"
    return x / y

def power(x,y):
    return x ** y

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

choice = input("Enter choice (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1,num2)}")
    elif choice == '5':
        print(f"{num1} ** {num2} = {power(num1,num2)}")
else:
    print("Invalid Input")
#8:web scraping --> scraping hyperlinks
import requests
from bs4 import BeautifulSoup
#fetch the webpage
url = 'https://www.bbc.com'
response = requests.get(url)

#ensure the webpage is fetched successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
#Parse the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
#Find all the headline links (usually <h3> or <a> tags
links = soup.find_all('a')
# loop through the headlines and print them
for link in links:
    href = link.get('href')
    if href:
        print(href)
    else:
        print("no href attribute found for this link.")
else:
    print(f"failed")
#9: Create a madlib story
#Define the story with placeholders
story = """
Once upon a time, a [adjective] [noun] decided to [verb] in the [place].
It was a very [adjective] day, and the [noun] was feeling quite [emotion].
"""

#Get user input
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
emotion = input("Enter an emotion: ")
noun2 = input("Enter another noun: ")

# Replace placeholders
story = story.replace("[adjective]", adjective1, 1)
story = story.replace("[noun]", noun1, 1)
story = story.replace("[verb]", verb, 1)
story = story.replace("[place]", place, 1)
story = story.replace("[adjective]", adjective2, 1)
story = story.replace("[emotion]", emotion, 1)
story = story.replace("[noun]", noun2, 1)

#Print the final story
print("\nHere’s your Mad Libs story:\n")
print(story)

#10 --> make a simple password generator
import random
import string

# Function to generate a random password
def generate_password(length):

    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    punctuation = string.punctuation  # !@#$%^&*() etc.

    # Combine all character sets into one pool
    all_characters = lower + upper + digits + punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(password_length)

# Output the generated password
print("\nGenerated Password:", password)



