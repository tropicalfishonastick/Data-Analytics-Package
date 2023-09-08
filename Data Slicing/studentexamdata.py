import csv

# This function processes a chunk of student scores and calculates the average score
def process_chunk(chunk):
    total_score = 0
    num_students = 0
    
    # Iterate through each student's data in the chunk
    for row in chunk:
        # Convert the score to a float and add it to the total score
        total_score += float(row['Scores'])
        num_students += 1  # Count the number of students in the chunk
        
    # Calculate and return the average score for the chunk
    return total_score / num_students

def main():
    chunk_size = 100  # Define the size of each data chunk
    file_path = r'C:\Users\Ayushi Tripathi\OneDrive\Documents\Github\DataSliceMaster'
    with open('student_scores.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Create a CSV reader for the file
        print(reader.fieldnames)  # This will print the column names
        chunk = []  # Initialize an empty list to hold the current chunk of data
        chunk_count = 0  # Initialize a counter for the current chunk

        # Iterate through each row in the CSV file
        for row in reader:
            chunk.append(row)  # Add the row to the current chunk
            
            # Check if the chunk has reached the desired size
            if len(chunk) == chunk_size:
                # Calculate the average score for the current chunk
                average_score = process_chunk(chunk)
                # Print the chunk number and its average score with 2 decimal places
                print(f"Chunk {chunk_count + 1}: Average Score = {average_score:.2f}")
                
                # Reset the chunk and move to the next one
                chunk = []
                chunk_count += 1

        # Process any remaining data in the last chunk
        if len(chunk) > 0:
            average_score = process_chunk(chunk)
            print(f"Chunk {chunk_count + 1}: Average Score = {average_score:.2f}")

# Execute the main function when the script is run
if __name__ == '__main__':
    main()
