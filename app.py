import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import io
from transformers import pipeline
import re
import random

# Load the LLM (Language Model) for query interpretation
nlp = pipeline("text-generation", model="gpt2")  # Replace "gpt2" with any advanced model

# Title of the application
st.title("Interactive Data Analysis and Visualization App with LLM")

# Sidebar for uploading dataset
st.sidebar.title("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file for analysis", type=["csv"])

if uploaded_file:
    # Load dataset
    dataset = uploaded_file.read()
    df = pd.read_csv(io.StringIO(dataset.decode("utf-8")))
    st.sidebar.success("Dataset uploaded successfully!")
    st.write("## Dataset Preview")
    st.dataframe(df)
else:
    st.info("Please upload a dataset to begin.")

# Keywords to detect graph type or query intent
keywords = {
    "bar chart": ["categories", "comparison", "quantities","bar chart"],
    "line chart": ["time series", "trend", "continuous data","line chart"],
    "pie chart": ["percentages", "parts of a whole", "segments","pie chart"],
    "scatter plot": ["correlation", "data points", "x and y axes","scatter plot"],
    "histogram": ["frequency distribution", "bins", "ranges","histogram"],
}

# User query input
st.write("## Ask Your Query")
user_input = st.text_input(
    "Describe your question or the graph you want to generate (e.g., 'Show sales trend over time')."
)

def determine_graph_type(user_query):
    for graph, keys in keywords.items():
        for key in keys:
            if key in user_query.lower():
                return graph
    return None

if user_input and uploaded_file:
    dataset_columns = df.columns.tolist()

    # Step 1: Use LLM to interpret the query
    prompt = f"Interpret the following query and suggest the appropriate graph, calculation, or operation. Dataset columns: {dataset_columns}. Query: {user_input}"
    llm_response = nlp(prompt, max_new_tokens=100, num_return_sequences=1)[0]["generated_text"]
    st.write("### LLM Interpretation:")
    st.write(llm_response)

    # Step 2: Determine graph type using keywords or LLM interpretation
    graph_type = determine_graph_type(llm_response) or determine_graph_type(user_input)

    # Step 3: Handle advanced queries (highest, lowest, top/bottom N)
    if "highest" in user_input or "lowest" in user_input:
        column = [col for col in dataset_columns if col.lower() in user_input.lower()]
        if column:
            column = column[0]
            if "highest" in user_input:
                value = df[column].max()
                st.write(f"The highest value in column '{column}' is {value}.")
            elif "lowest" in user_input:
                value = df[column].min()
                st.write(f"The lowest value in column '{column}' is {value}.")
        else:
            st.write("Please specify a valid column for the highest/lowest value query.")

    elif "top" in user_input or "bottom" in user_input:
        match = re.search(r"top (\d+)|bottom (\d+)", user_input.lower())
        if match:
            n = int(match.group(1) or match.group(2))
            column = [col for col in dataset_columns if col.lower() in user_input.lower()]
            if column:
                column = column[0]
                if "top" in user_input:
                    result = df.nlargest(n, column)
                elif "bottom" in user_input:
                    result = df.nsmallest(n, column)
                st.write(f"Here are the {'top' if 'top' in user_input else 'bottom'} {n} values in column '{column}':")
                st.dataframe(result)
            else:
                st.write("Please specify a valid column for the top/bottom query.")

    # Step 4: Generate graphs based on the query
    if graph_type:
        st.write(f"### Generating a {graph_type} based on your query...")

        if graph_type == "pie chart":
            # Pie chart requires only one column
            pie_column = None
            for col in dataset_columns:
                if col.lower() in user_input.lower():
                    pie_column = col
                    break
            if pie_column:
                st.write(f"Generating a Pie Chart for column: {pie_column}")
                pie_data = df[pie_column].value_counts()
                fig, ax = plt.subplots(figsize=(8, 8))
                ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Ensures a circular pie chart
                st.pyplot(fig)
            else:
                st.write("Please specify a valid column for the pie chart.")
        else:
            # Select x and y columns for other graphs
            x_col, y_col = None, None
            for col in dataset_columns:
                if col.lower() in user_input.lower():
                    if not x_col:
                        x_col = col
                    elif not y_col:
                        y_col = col
                        break
            if not x_col or not y_col:
                x_col = random.choice(dataset_columns)
                y_col = random.choice([col for col in dataset_columns if col != x_col])

            plt.figure(figsize=(12, 6))
            if graph_type == "line chart":
                plt.plot(df[x_col], df[y_col], marker="o")
            elif graph_type == "bar chart":
                plt.bar(df[x_col], df[y_col])
            elif graph_type == "scatter plot":
                plt.scatter(df[x_col], df[y_col])
            elif graph_type == "histogram":
                plt.hist(df[x_col], bins=10)

            plt.title(f"{graph_type.capitalize()} of {y_col} vs {x_col}", fontsize=16)
            plt.xlabel(x_col, fontsize=14)
            plt.ylabel(y_col, fontsize=14)
            plt.xticks(fontsize=12, rotation=45)
            plt.yticks(fontsize=12)
            st.pyplot(plt)
    else:
        st.write("Unable to determine the graph type from the query. Please specify a valid graph type or check your query.")