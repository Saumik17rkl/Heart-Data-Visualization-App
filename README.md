# Heart Data Visualization App

This is a Streamlit-based web application for visualizing heart data from a CSV file. The app allows users to generate various charts and analyze data interactively.

## Features

- Upload and preview heart dataset
- View summary statistics of the dataset
- Select and generate different types of visualizations:
  - Line Chart
  - Bar Chart
  - Scatter Plot
  - Histogram
  - Correlation Heatmap

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/Saumik17rkl/Heart-Data-Visualization-App.git
   cd heart-data-visualization
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the App

1. Ensure you have a dataset named `heart.csv` in the working directory.
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## File Structure

```
heart-data-visualization/
│── app.py              # Main application script
│── heart.csv           # Sample dataset
│── requirements.txt    # Required dependencies
│── README.md           # Project documentation
```

## Error Handling

- If `heart.csv` is missing, an error message will be displayed.
- Any unexpected errors will be caught and shown in the app.

