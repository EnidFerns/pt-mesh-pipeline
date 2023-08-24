import pandas as pd

# Load the CSV file into a Pandas DataFrame
filename = "tender_details.csv"
df = pd.read_csv(filename)

# Open a text file for writing analysis results
analysis_filename = "data_analysis_results.txt"
with open(analysis_filename, "w") as f:
    f.write("Tender Details Analysis\n\n")

    # Display the first few rows of the DataFrame
    f.write("First Few Rows:\n")
    f.write(str(df.head()) + "\n\n")

    # Get basic statistics of the dataset
    f.write("Basic Statistics:\n")
    f.write(str(df.describe()) + "\n\n")

    # Count the number of tenders
    num_tenders = len(df)
    f.write("Number of tenders: {}\n\n".format(num_tenders))

    # Find the tender with the earliest closing date
    earliest_closing_date = df['Closing Date'].min()
    earliest_tender = df[df['Closing Date'] == earliest_closing_date]['Tender Title'].values[0]
    f.write("Tender with earliest closing date: {}\n\n".format(earliest_tender))

    # Find the average bid opening time in hours
    df['Bid Opening Date'] = pd.to_datetime(df['Bid Opening Date'])
    df['Closing Date'] = pd.to_datetime(df['Closing Date'])
    df['Time Difference'] = (df['Bid Opening Date'] - df['Closing Date']).dt.total_seconds() / 3600
    average_time = df['Time Difference'].mean()
    f.write("Average bid opening time (hours): {:.2f}\n".format(average_time))

print("Analysis results saved to", analysis_filename)
