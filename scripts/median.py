import csv
import statistics

# Path to the CSV file
csv_file_path = "output/Average_COICOP3.csv"


def calculate_median_total(csv_path):
    totals = []

    with open(csv_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            # Convert all but the first two columns (Geographic Code and population) to floats and sum them
            total = sum(float(value) for value in row[2:])
            totals.append(total)

    # Calculate the median of the totals
    median_total = statistics.median(totals)
    return median_total


median_total = calculate_median_total(csv_file_path)
print(f"The median of the totals is: {median_total}")
