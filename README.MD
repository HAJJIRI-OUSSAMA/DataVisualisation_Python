
# 📊 Data Analysis and Visualization App

This is a Python application built using Streamlit for visualizing and analyzing data from an Excel file. The app allows users to upload an Excel file and perform statistical calculations along with various data visualizations.

---

## 🚀 Features
- **Data Preview**: Displays the first few rows of the uploaded Excel data.
- **Statistical Calculations**:
  - Mean (Moyenne)
  - Median
  - Mode
  - Variance
  - Standard Deviation (Écart-Type)
  - Range (Étendue)
- **Data Visualizations**:
  - Line Plot
  - Scatter Plot
  - Box Plot
  - Histogram
  - KDE Plot
  - Violin Plot

---

## 📂 Project Structure
```
.
├── app.py                  # Main application file
├── requirements.txt        # Dependencies required to run the app
├── book.xlsx               # Sample Excel file for testing
└── README.md               # Project documentation
```

---

## 🛠️ Prerequisites

Make sure you have **Python 3.x** installed on your machine.

You'll also need to install the following Python packages:

- `streamlit`
- `pandas`
- `seaborn`
- `matplotlib`
- `numpy`

These are listed in the `requirements.txt` file.

---

## 💻 Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/HAJJIRI-OUSSAMA/DataVisualisation_Python.git
    cd DataVisualisation_Python
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    streamlit run app.py
    ```

5. **Open your browser** and go to:
    ```
    http://localhost:8501
    ```

---

## 📁 Usage

1. **Upload an Excel file** (`.xlsx`) using the file uploader.
2. **Data Preview**: View the first few rows of your data.
3. **Statistical Analysis**:
   - Select a numeric column from the dropdown.
   - Click on "Calculate Statistics" to get statistical measures.
4. **Data Visualization**:
   - Choose a visualization type from the dropdown.
   - Select a numeric column (and another for scatter plots).
   - Click on "Show Visualization" to generate the plots.

---

## 🧪 Testing with Sample Data
To test the app, you can use the included `book.xlsx` file:

- Upload `book.xlsx` using the file uploader.
- Explore the statistical calculations and visualizations.

---

## 🔧 Troubleshooting
If you encounter issues:
- Ensure all dependencies are installed correctly using:
  ```bash
  pip install -r requirements.txt
  ```
- Make sure your Excel file is correctly formatted and not empty.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or want to improve the app.

1. Fork the project
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements
- Built with [Streamlit](https://streamlit.io/)
- Inspired by data analysis tools and statistical visualization.
