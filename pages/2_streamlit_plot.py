import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# Streamlit Graph plot 📊")

datafile = st.file_uploader("Upload your csv file here")

def graphPlot(plottype):

    x_axis = st.selectbox(
        "Select X axis",
        dataframe.columns.values
    )

    y_axis = st.selectbox(
        "Select Y axis",
        dataframe.columns.values
    )

    if (st.button("plot the chart")):
        if (plottype == "area"):

            if (dataframe[y_axis].dtype == int or dataframe[y_axis].dtype == float):
                chart_data = pd.DataFrame(
                {
                    "col1": dataframe[x_axis],
                    "col2": dataframe[y_axis],
                    "col3": np.random.choice(["A", "B", "C"], len(np.array(dataframe[x_axis]))),
                }
                )
                st.area_chart(chart_data, x="col1", y="col2", color="col3")
                
            else:
                st.error("Plese select the non string value column")

        elif(plottype == "bar"):
            chart_d = pd.DataFrame(
                {
                    "col1": dataframe[x_axis],
                    "col2": dataframe[y_axis],
                }
            )   

            st.bar_chart(chart_d, x="col1", y="col2")


        
    


if datafile :
    data = pd.read_csv(datafile)

    dataframe = pd.DataFrame(data)

    st.write("10 Rows of Your CSV file")
    st.table(dataframe.head(10))

    graphtype = st.selectbox(
        "select the graph",
        ["Area Plot", "Bar Plot"]
    )

    if(graphtype == "Area Plot"):
        graphPlot("area")

    elif(graphtype == "Bar Plot"):
        graphPlot("bar")