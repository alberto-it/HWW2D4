"""
Lesson 4: Assignments | Python Loop Statements
1. The Range Riddle
Task 1: Your Mood Today
Example Outcome: An example output could be 
"On Wednesday, you were feeling happy." 
"On Thursday you were feeling sad."
"""
print()
import random
moods = ["happy", "sad", "energetic", "calm", "tired"]
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in range(7):
    mood = random.choice(moods)
    print(f"You were feeling {mood} on {days[i]}.")
print()
"""
2. Double Scoop with Nested Loops
Task 1: Your Mood Tracker
Example Outcome: An example would be "On Tuesday afternoon you were sad"
"On Tuesday night you were happy" "On Wednesday morning you were tired"
"""
times = ['morning','afternoon','night']
for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day} {time}, you were {mood}.")
print()
"""
3. Loop Condition Logic
Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be true (an infinite loop). 
Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.
"""
i = 0
while True:
    print("Loopy...", i+1)
    i += 1
    if i == 5:
        break
print()
"""
Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true 
and remove the break statement. The loop should terminate naturally once the condition is met.
"""
i = 0
while i < 5:
    print("Loopy...", i+1)
    i += 1
print()
"""
4. Python's Random Game Night
Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. 
Provide feedback on whether they guessed correctly or not.
"""
ltr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
secret_ltr = random.choice(ltr)
guess = input(f"Guess a letter from {ltr[0]} to {ltr[-1]}: ").upper()
guess_cnt = 1
while guess != secret_ltr:
    if ltr[0] <= guess <= ltr[-1]:  # Different message if guess NOT in Range
        msg = "high" if guess > secret_ltr else "low "
        guess = input(f"Guess was too {msg} (Guess Again): ").upper()
    else:
        guess = input(f"{guess} is OUT OF RANGE  (Guess Again): ").upper()
    guess_cnt += 1
print(f"\n  You guessed it in {guess_cnt} tries! 🎉 🥳 \n") 
"""
5. Looping Lists - The Rhythm of Repetition
Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message.
Extend this task by adding a counter that displays the number of the track before the genre.
Our playlist of genres:
"""
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for i in range(len(genres)):
    print("Track", i+1, ": Now Playing", genres[i])
print()
"""
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function 
but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.
"""
i = 0
while i < len(genres):
    print("Track", i+1, ": Now Playing", genres[i])
    if genres[i] == "Hip-hop":
        break
    i += 1
print()
"""
Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index.
For each genre, print out the track number and a message that the light show is ready. 
Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.
"""
for i in range(len(genres)):
    if genres[i] == "Classical":
        continue
    print("Track", i+1, ": Light show ready for", genres[i])
print()
"""
6. Advanced Looping 
Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres.
Use slicing to create a sublist of genres from the second to the fourth track.
"""
for genre in genres[1:4]:
    print(genre)
print()
"""
Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre 
with the word "Music" appended to it. Print this new list.
"""
print([genre + " Music" for genre in genres])
print()
"""
Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".
"""
for i in range(10, 0, -1):
  print(i)
print("The beat drops now!\n")
