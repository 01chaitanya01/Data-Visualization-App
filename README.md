# Data-visualization-app

This is a Streamlit web application for dynamic graph plotting from CSV files, with an added feature to convert files to Excel format.

## Features

- **Matplotlib Graphs**: Plot graphs using Matplotlib.
- **Streamlit Graphs**: Plot graphs using Streamlit's built-in plotting capabilities.
- **CSV to Excel Converter**: Convert CSV files to Excel format.

## Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/01chaitanya01/Data-visualization-app.git
   cd Data-visualization-app
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```
   streamlit run welcome.py
   ```

4. **Open the application in your browser:**
   ```
   http://localhost:8501
   ```

## Project Structure

- **`welcome.py`**: Main Python script containing the Streamlit web application.
- **`pages/`**: Folder containing Python scripts for different functionalities:
  - `1_matplot_graphs_plot.py`: Script for plotting graphs using Matplotlib.
  - `2_streamlit_plot.py`: Script for plotting graphs using Streamlit's built-in plotting capabilities.
  - `3_CSV_to_Excel.py`: Script for converting CSV files to Excel format.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or create a pull request.
