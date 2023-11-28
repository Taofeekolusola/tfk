from collections import Counter
import statistics

# Given data
data = {
    'Monday': ['green', 'green', 'green', 'red', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'pink', 'orange', 'white', 'white'],
    'Tuesday': ['arsh', 'green', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'pink', 'orange', 'orange', 'white', 'white', 'white'],
    'Wednesday': ['green', 'green', 'red', 'yellow', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'pink', 'orange', 'orange', 'white', 'white', 'white'],
    'Thursday': ['cream', 'green', 'green', 'red', 'yellow', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'pink', 'orange', 'orange', 'white', 'white', 'white'],
    'Friday': ['black', 'green', 'green', 'red', 'red', 'red', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'white', 'white', 'white', 'white', 'white']
}

# Flatten the list of colors for each day
all_colors = [color for colors in data.values() for color in colors]

# Calculate mean color
mean_color = statistics.mode(all_colors)

# Calculate most worn color
most_worn_color = Counter(all_colors)

# Calculate variance of colors
variance_colors = statistics.variance([all_colors.count(color) for color in set(all_colors)])
# Count the number of times red appears
red_count = all_colors.count('red')

# Calculate the total number of possible outcomes
total_outcomes = len(all_colors)

# Calculate the probability
probability_red = red_count / total_outcomes

# Print results
print("Probability that the color is red:", probability_red)
print("Mean Color:", mean_color)
print("Most Worn Color:", most_worn_color)
print("Variance of Colors:", variance_colors)
