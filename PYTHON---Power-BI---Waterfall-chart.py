import pandas as pd
import matplotlib.pyplot as plt

def waterfall_chart(data, title):
    plt.figure(figsize=(10, 6))
    
    # Initialize y-axis position
    y_pos = data['Start'].values
    
    # Plot starting bars
    plt.bar(data['Category'], data['Start'], color='grey')
    
    # Plot positive changes
    plt.bar(data['Category'], data['Change'].where(data['Change'] > 0), bottom=y_pos, color='g')
    y_pos += data['Change'].where(data['Change'] > 0).fillna(0).values
    
    # Plot negative changes
    plt.bar(data['Category'], data['Change'].where(data['Change'] < 0), bottom=y_pos, color='r')
    y_pos += data['Change'].where(data['Change'] < 0).fillna(0).values
    
    # Plot the final values
    plt.bar(data['Category'], data['End'] - data['Start'], bottom=y_pos, color='b')
    
    # Add title and labels
    plt.title(title)
    plt.xlabel('Category')
    plt.ylabel('Value')
    
    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')
    
    # Show plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Start': [100, 200, 150, 300, 250],
    'Change': [50, 100, -30, -50, 70],
}

# Calculate the end values
data['End'] = data['Start'] + data['Change']

# Plot the waterfall chart
waterfall_chart(pd.DataFrame(data), title='Waterfall Chart Example')
