import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats

st.title("Data Analysis and Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Data Preview:", df.head())
    
    # Ensure a numeric column
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_cols:
        selected_column = st.selectbox("Select a numeric column", numeric_cols)
        
        if st.button("Calculate Statistics"):
            if df.empty:
                st.error("DataFrame is empty!")
            else:
                mean = df[selected_column].mean()
                median = df[selected_column].median()

                
                mode_values = df[selected_column].mode()
                mode_counts = df[selected_column].value_counts()
               
                if not mode_values.empty and mode_counts[mode_values[0]] > 1:
                    mode = ', '.join(map(str, mode_values)) # Convert all mode values to a comma-separated string
                else:
                    mode = "No mode"

                variance = df[selected_column].var()
                std_dev = df[selected_column].std()
                data_range = df[selected_column].max() - df[selected_column].min()


                st.write(f"Moyenne: {mean}")
                st.write(f"Median: {median}")
                st.write(f"Mode: {mode}")
                st.write(f"Variance: {variance}")
                st.write(f"ECART-Type: {std_dev}")
                st.write(f"Etendu: {data_range}")
    else:
        st.error("No numeric columns available in the uploaded file.")

    # Visualization Section
    st.subheader("Data Visualization")

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    visualization_type = st.selectbox("Select Visualization Type", 
                                  ["Line Plot", "Scatter Plot", "Box Plot", "Histogram", "KDE Plot", "Violin Plot"])

    selected_column = st.selectbox("Select a numeric column for visualization", numeric_cols)

    if visualization_type == "Scatter Plot" and len(numeric_cols) > 1:
        scatter_column = st.selectbox("Select a column to plot against", [col for col in numeric_cols if col != selected_column])


    if st.button("Show Visualization"):
        if df.empty:
            st.error("DataFrame is empty!")
        elif selected_column: # see if the column is selected
            fig, ax = plt.subplots(figsize=(8, 6))

            if visualization_type == "Line Plot":
                sns.lineplot(data=df, x=df.index, y=selected_column, ax=ax)
                ax.set_title(f'Line Plot of {selected_column}')

            elif visualization_type == "Scatter Plot":
                sns.scatterplot(data=df, x=selected_column, y=scatter_column, ax=ax)
                ax.set_title(f'Scatter Plot between {selected_column} and {scatter_column}')

            elif visualization_type == "Box Plot":
                sns.boxplot(data=df, y=selected_column, ax=ax)
                ax.set_title(f'Box Plot of {selected_column}')

            elif visualization_type == "Histogram":
                sns.histplot(data=df, x=selected_column, bins=20, ax=ax)
                ax.set_title(f'Histogram of {selected_column}')
        
            elif visualization_type == "KDE Plot":
                sns.kdeplot(data=df, x=selected_column, ax=ax)
                ax.set_title(f'KDE Plot of {selected_column}')
        
            elif visualization_type == "Violin Plot":
                sns.violinplot(data=df, y=selected_column, ax=ax)
                ax.set_title(f'Violin Plot of {selected_column}')

            st.pyplot(fig)



