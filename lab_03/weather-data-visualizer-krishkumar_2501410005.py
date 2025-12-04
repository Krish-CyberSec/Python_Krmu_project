import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Data Acquisition and Loading
def load_data(file_path):
    """Load the weather data from a CSV file and display basic information."""
    try:
        # Load the CSV file into a pandas DataFrame
        data = pd.read_csv(file_path)
        
        # Print first few rows of the data to understand its structure
        print("First 5 rows of the dataset:")
        print(data.head())
        print("\nData Info:")
        print(data.info())
        print("\nData Description:")
        print(data.describe())
        
        return data
    except FileNotFoundError:
        print("The file at the specified path does not exist.")
        return None

# Task 2: Data Cleaning
def clean_data(data):
    """Clean the weather data by handling missing values and correcting data types."""
    if data is None:
        return None
    
    # Convert 'Date/Time' column to datetime format for easier manipulation
    data['Date/Time'] = pd.to_datetime(data['Date/Time'], errors='coerce')
    
    # Drop rows with missing important columns like 'Date/Time' or 'Temp_C'
    data.dropna(subset=['Date/Time', 'Temp_C'], inplace=True)
    
    # Fill missing temperature values with the median temperature
    data['Temp_C'].fillna(data['Temp_C'].median(), inplace=True)
    
    return data

# Task 3: Basic Statistics
def compute_statistics(data):
    """Compute basic statistics like average temperature."""
    if data is None:
        return None
    
    # Calculate average temperature
    avg_temp = data['Temp_C'].mean()
    print(f"\nAverage Temperature: {avg_temp:.2f}°C")
    
    return avg_temp

# Task 4: Visualization with Matplotlib
def create_visualizations(data):
    """Create a simple line plot for temperature over time."""
    if data is None:
        return
    
    # Line chart: Plot temperature over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date/Time'], data['Temp_C'], label='Temperature (°C)', color='blue')
    plt.title("Temperature Over Time")
    plt.xlabel("Date/Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function to run the tasks
def main():
    # Load data
    file_path = 'data/Weather_Data.csv'
    data = load_data(file_path)

    if data is not None:
        # Clean the data
        data = clean_data(data)

        # Compute and print basic statistics
        compute_statistics(data)

        # Create visualizations
        create_visualizations(data)

if __name__ == '__main__':
    main()
