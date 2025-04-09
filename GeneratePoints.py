import csv
import random
# Ask the user for the number of points to generate
num_points = int(input("Enter the number of points to generate: "))
# Generate random points with x between 1 and 500, and y between 1 and 1200
points = [(random.randint(1, 500), random.randint(1, 1200)) for _ in
range(num_points)]
# Define the CSV filename
filename = "PointsGen.csv"
# Write the points to a CSV file using ';' as the delimiter
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # Write headers
    writer.writerow(["x", "y"])
    # Write each point
    writer.writerows(points)
print(f"{num_points} points have been generated and saved to {filename}.")