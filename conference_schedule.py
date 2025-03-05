def maxPresentations(scheduleStart, scheduleEnd):
    # Step 1: Pair the start and end times and sort by end times
    presentations = sorted(zip(scheduleEnd, scheduleStart))  # Sort by end time
    count = 0
    last_end_time = 0

    # Step 2: Iterate and select non-overlapping presentations
    for end, start in presentations:
        if start >= last_end_time:  # If it starts after the last attended presentation ends
            count += 1
            last_end_time = end  # Update the last attended presentation's end time

    return count

# Function to handle input format
def main():
    # Read input for scheduleStart
    n = int(input().strip())  # Number of presentations
    scheduleStart = [int(input().strip()) for _ in range(n)]

    # Read input for scheduleEnd
    n = int(input().strip())  # Again read the number of presentations
    scheduleEnd = [int(input().strip()) for _ in range(n)]

    # Call the function and print the result
    print(maxPresentations(scheduleStart, scheduleEnd))

# Run the main function
if __name__ == "__main__":
    main()
