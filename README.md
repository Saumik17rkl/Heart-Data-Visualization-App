# Heart-Data-Visualization-App
A Streamlit app for interactive data visualization of `heart.csv`, featuring data preview, summary, and visualizations (line, bar, scatter, histogram, heatmap) with user-friendly sidebar controls.
The Heart Data Visualization App is a data analysis and visualization application designed to provide insights into heart disease datasets. Built using Streamlit, this app allows users to explore various attributes related to heart health and their correlation with the likelihood of heart disease. The app includes interactive visualizations and statistical insights to aid in understanding patterns and trends in heart disease data.

Key Features:
Interactive Visualizations:

Users can visualize key metrics such as age, cholesterol levels, blood pressure, and more through interactive charts and graphs.
Correlation Analysis:

The app visualizes the relationships between different features of the dataset (e.g., age vs. cholesterol level) using correlation heatmaps and scatter plots.
Heart Disease Prediction:

Based on user input (age, cholesterol, etc.), the app can predict the likelihood of heart disease using a trained machine learning model (e.g., Logistic Regression, Decision Tree).
Model Evaluation:

The app shows various evaluation metrics for the trained model, such as accuracy, precision, recall, and confusion matrix.
Dataset Overview:

Users can explore the dataset to understand the distribution of features and target variables.
Technologies Used:
Streamlit: For building the interactive web application.
Pandas: For data manipulation and analysis.
Matplotlib & Seaborn: For visualizing the data and correlations.
Scikit-learn: For implementing machine learning models (e.g., Logistic Regression) to predict heart disease.
Numpy: For numerical operations and calculations.
Dataset:
The app uses a Heart Disease dataset that contains medical information about individuals, such as:

Age
Sex
Blood pressure
Cholesterol
Max heart rate achieved
Exercise induced angina
Target variable: Whether or not the individual has heart disease (binary classification).
Machine Learning Model:
The app utilizes a Logistic Regression model (or any classifier of your choice) to predict the likelihood of heart disease based on input features. The model is trained and evaluated on the heart disease dataset, and its performance is displayed in terms of metrics like accuracy, precision, and recall.

How to Run:
Clone the repository:
bash
Copy
Edit
git clone https://github.com/Saumik17rkl/Heart-Data-Visualization-App.git
Install the required libraries:
bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy
Edit
streamlit run app.py
Screenshots:
Home Page: Interactive input and visualizations of heart disease-related features.
Data Visualization Page: A variety of plots showing correlations and distributions of the dataset.
Prediction Results: Displays the heart disease prediction based on user inputs.
Contributions:
Feel free to fork the repository and submit pull requests with improvements. If you encounter any issues or have suggestions, please submit an issue or a pull request.
