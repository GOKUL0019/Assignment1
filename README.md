# Project Description:
Interactive Data Analysis and Visualization App with LLM

This project is a web application built using Streamlit, Pandas, and Matplotlib, integrated with a Language Model (LLM) powered by GPT-2 for natural language query interpretation. The app allows users to upload a CSV file and perform interactive data analysis by simply asking questions in natural language.

Once the dataset is uploaded, users can query the application for various types of visualizations (e.g., bar charts, line charts, pie charts) or ask questions about specific data insights such as the highest or lowest values, or top N records. The application uses the GPT-2 model to interpret the queries and suggest the best chart types or data operations. Based on these interpretations, the app generates appropriate visualizations using Matplotlib.

This interactive approach to data analysis allows non-technical users to easily visualize and explore datasets.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Features
Dataset Upload: Upload any CSV dataset through the sidebar.
Natural Language Query Interpretation: Enter natural language queries to generate graphs and extract insights (e.g., "Show sales trend over time" or "Top 5 products by sales").
Graph Generation: Automatically generate various types of visualizations such as:
Bar Chart for comparisons.
Line Chart for time-series data or trends.
Pie Chart for percentage-based data.
Scatter Plot for correlation analysis.
Histogram for frequency distributions.
Advanced Queries: Get answers for queries such as highest/lowest values or top/bottom N records in a dataset.
Interactive Interface: Built using Streamlit, making it simple to interact with and explore data.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Technologies Used

Python: Programming language used for building the app.
Streamlit: Framework for building the interactive web app.
Pandas: For data manipulation and analysis.
Matplotlib: For data visualization (charts and graphs).
Transformers: For utilizing GPT-2 for natural language query interpretation.
Installation and Setup

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### To run this application on your local machine, follow these steps:

Prerequisites
Ensure you have Python 3.7 or later installed. If not, download and install it from python.org.

Steps to Install
Clone the Repository
First, clone this repository to your local machine using the following command:
```
git clone https://github.com/GOKUL0019/Assignment1.git
cd Assignment1
```
Navigate to the Project Directory
Go to the project folder:
```
cd interactive-data-visualization
```
Create a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment for your project:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Required Libraries
Install all the required libraries by running:
```
pip install -r requirements.txt
```

If the requirements.txt file doesn't exist, manually install the dependencies with:

'''
pip install pandas matplotlib streamlit transformers
'''
## Run the Application
After the installation is complete, run the Streamlit app:
```
streamlit run app.py
```
This will start the app, and you should be able to access it in your browser at http://localhost:8501.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Usage

Upload a Dataset: On the sidebar, click "Upload a CSV file" to upload your dataset. The dataset will be previewed in the main area of the app.

Ask a Query: Use the "Ask Your Query" section to type a natural language query, like:

"Show sales trend over time"
"What is the highest sales value?"
"Top 10 products by sales"
The app will interpret the query and, if possible, generate the appropriate graph or data analysis.

View Results: The app will display the relevant graph or data table based on your query.

Example Queries
"Show sales trend over time."
The app will generate a line chart showing how sales change over time, assuming the dataset contains time-based and sales-related columns.

"What are the top 5 products by sales?"
The app will display the top 5 products based on the sales column.

"Show distribution of product categories."
A pie chart will be generated based on the distribution of product categories.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Troubleshooting

Issue: The app doesn't display the dataset after upload.
Solution: Make sure the uploaded file is in the correct CSV format, and ensure it has headers (column names) for proper interpretation.

Issue: The app can't interpret the query correctly.
Solution: The query might not contain enough information for the model to understand. Try to use specific phrases like "sales trend" or "top N."

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure that your contributions are well-documented and follow the existing code style.

