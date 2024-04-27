import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.markdown("# Graph Plotter 📈")

data_file = st.file_uploader("Upload you csv file")

fig, ax = plt.subplots()

plt.figure(facecolor='yellow')
ax.set_facecolor("#495057")

def twoParameterPlot(plottype):
    x_axis = st.selectbox(
        "Select the X axis, the Column should be integer or flote values",
            dataset.columns.values
        )
    st.write('You selected:', x_axis)
    y_axis = st.selectbox(
        "Select the Y axis, the Column should be integer or flote values",
            dataset.columns.values
        )
    st.write('You selected:', y_axis)

    if st.button('plot the chart'):
        x_value = dataset[x_axis]
        y_value = dataset[y_axis]

        st.write("plotting the graph...")

        if(plottype == "line"):
            ax.plot(x_value, y_value)
            st.pyplot(fig)

        elif(plottype == "scatter"):
            ax.scatter(x_value, y_value)
            st.pyplot(fig)

        elif(plottype == "bar"):
            ax.bar(x_value, y_value)
            st.pyplot(fig)

        elif(plottype == "hbar"):
            ax.barh(x_value, y_value)
            st.pyplot(fig)
        
        st.write("Graph ploted successfully")


def oneParameterPlot(plottype):
    x_axis = st.selectbox(
        "Select column",
            dataset.columns.values
        )
     
    if(plottype == "hist"):
        bin_size = st.number_input("Enter bin size", 10)

    elif plottype == "box":
        st.write("Do you want to select a second parameter?")
        
        # Initialize box_parameter in session state if it doesn't exist
        if 'box_parameter' not in st.session_state:
            st.session_state.box_parameter = None

        choice = st.radio("Select option", ("Yes", "No"))

        if choice == "Yes":
            st.session_state.box_parameter = st.selectbox(
                "Select second parameter, the Column should be integer or flote values",
                dataset.columns.values
            )
        else:
            st.session_state.box_parameter = None

        st.write("Second parameter is ", st.session_state.box_parameter)


    if st.button('plot the chart'):
        x_value = np.array(dataset[x_axis])

        st.write("plotting the graph...")
        if(plottype == "hist"):
            ax.hist(x_value, bins = bin_size)
            st.pyplot(fig)

        elif(plottype == "box"):
            if st.session_state.box_parameter:
                box_parameter_value = dataset[st.session_state.box_parameter]
                # try:
                if (box_parameter_value.dtype == float or int):
                    arr = np.array([x_value, box_parameter_value])
                    ax.boxplot(arr)
                    st.pyplot(fig)
                    st.write(box_parameter_value.dtype)
                else:
                # except ValueError:
                    st.error("Please select a column with numerical values.")
            else:
                ax.boxplot(x_value)
                st.pyplot(fig)

        elif(plottype == "violin"):
            if (x_value.dtype == float or int):
                ax.violinplot(x_value)
                st.error("Please select a column with numerical values.")
            
        elif(plottype == "pie"):
            if (x_value.dtype == float or int):
                ax.pie(x_value)
                st.pyplot(fig)
            else:
                st.error("Please select a column with numerical values.")
        
        st.write("Graph ploted successfully")


if(data_file):
    dataset = pd.read_csv(data_file)
    data_load_state = st.text('Loading data...')
    st.table(dataset.head(10))
    data_load_state.text('Loading data...done!')

    option = st.selectbox(
     'Select the graph you want to plot',
    ('Line Chart', 'Scatter Chart', 'Bar Chart', 'Horizontal Bar Chart', 'Histogram', 'Boxplot', 'Violinplot', 'Pie Chart'))
    st.write('You selected:', option)

    if(option == "Line Chart"):
        twoParameterPlot("line")

    elif(option == "Scatter Chart"):
        twoParameterPlot("scatter")

    elif(option == "Bar Chart"):
        twoParameterPlot("bar")

    elif(option == "Horizontal Bar Chart"):
        twoParameterPlot("hbar")

    elif(option == "Histogram"):
        oneParameterPlot("hist")

    elif(option == "Boxplot"):
        oneParameterPlot("box")

    elif(option == "Violinplot"):
        oneParameterPlot("violin")

    elif(option == "Pie Chart"):
        oneParameterPlot("pie")