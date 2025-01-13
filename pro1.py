import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Heart Data Visualization App")

# Load the uploaded CSV file
uploaded_file = "heart.csv"  # The uploaded file path

try:
    # Load the data
    data = pd.read_csv(uploaded_file)

    # Display the raw data
    st.subheader("Preview of Heart Data")
    st.dataframe(data)

    # Display data summary
    st.subheader("Heart Data Summary")
    st.write(data.describe())

    # Sidebar for user options
    st.sidebar.title("Visualization Options")

    # Select columns for visualization
    columns = data.columns.tolist()
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Select", "Line Chart", "Bar Chart", "Scatter Plot", "Histogram", "Correlation Heatmap"])

    if chart_type != "Select":
        if chart_type == "Line Chart":
            x_axis = st.sidebar.selectbox("Select X-axis", columns)
            y_axis = st.sidebar.selectbox("Select Y-axis", columns)
            st.subheader(f"Line Chart: {x_axis} vs {y_axis}")
            fig, ax = plt.subplots()
            sns.lineplot(data=data, x=x_axis, y=y_axis, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Bar Chart":
            x_axis = st.sidebar.selectbox("Select X-axis", columns)
            y_axis = st.sidebar.selectbox("Select Y-axis", columns)
            st.subheader(f"Bar Chart: {x_axis} vs {y_axis}")
            fig, ax = plt.subplots()
            sns.barplot(data=data, x=x_axis, y=y_axis, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Scatter Plot":
            x_axis = st.sidebar.selectbox("Select X-axis", columns)
            y_axis = st.sidebar.selectbox("Select Y-axis", columns)
            st.subheader(f"Scatter Plot: {x_axis} vs {y_axis}")
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Histogram":
            column = st.sidebar.selectbox("Select Column", columns)
            bins = st.sidebar.slider("Number of Bins", min_value=5, max_value=50, value=10)
            st.subheader(f"Histogram: {column}")
            fig, ax = plt.subplots()
            sns.histplot(data[column], bins=bins, kde=True, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Correlation Heatmap":
            st.subheader("Correlation Heatmap")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

except FileNotFoundError:
    st.error("The file 'heart.csv' was not found. Please ensure the file is located in the working directory.")
except Exception as e:
    st.error(f"An error occurred: {e}")
