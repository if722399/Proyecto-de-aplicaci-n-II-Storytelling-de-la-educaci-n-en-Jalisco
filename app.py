from re import X
import streamlit as st
import main as mn
import visualizations as vs
import plotly.express as px
import functions as fn
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Disable warning 
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Aplication project II - Jalisco education storytelling')

st.markdown('## Choose dataset to analyse')
database_radio = st.radio(
        '',
         ['PROPERTY','INVESTMENT','PERFORMANCE','PERSONAL']
    )

if database_radio=='PROPERTY':
    st.markdown('### Main variable to analyze')
    principal_radio = st.radio(
            '',
            mn.property
        )
elif database_radio=='INVESTMENT':
    st.markdown('### Main variable to analyze')
    principal_radio = st.radio(
            '',
            mn.investment
        )
elif database_radio=='PERFORMANCE':
    st.markdown('### Main variable to analyze')
    principal_radio = st.radio(
            '',
            mn.performance
        )
elif database_radio=='PERSONAL':
    st.markdown('### Main variable to analyze')
    principal_radio = st.radio(
            '',
            mn.personal
        )





st.markdown('### Chose the type of the second variable')

v_type = st.radio(
        '',
         ['Numeric','Categoric']
    )


if v_type == 'Numeric':
    numeric_box = st.selectbox(
        'Choose a numeric variable',
        mn.numeric_performers.columns
    )
    st.markdown('#### Correlation')
    st.markdown(fn.get_corr(principal_radio,numeric_box,mn.numeric_performers))

    st.markdown('#### Scatter plot')
    f = px.scatter(mn.df,principal_radio, y = numeric_box, color = numeric_box)
    st.plotly_chart(f)

    st.markdown('#### Descriptive statistics')
    st.text(f'Columns: {numeric_box}')
    st.text(f'Rows: {principal_radio}')
    st.write(mn.df[[principal_radio]+[numeric_box]].groupby(principal_radio)[numeric_box].agg(['sum','describe']))


    categoric_box = st.selectbox(
        'Choose a categoric variable',
        mn.categoric_performers.columns
    )

    st.markdown(f'#### Contrasting variables grouping by {categoric_box}')
    st.plotly_chart(vs.dax_viz(principal_radio,numeric_box,categoric_box))
    
    show_map = st.checkbox('Show Map')
    if show_map:
        st.text('Mean by municipality')
        st.pyplot(vs.map_viz(principal_radio))


    # Categoric pendiente

if v_type == 'Categoric':
    categoric_box = st.selectbox(
        'Choose a categoric variable',
        mn.categoric_performers.columns
    )

    st.markdown('#### Descriptive statistics')
    st.text(f'Columns: {principal_radio}')
    st.text(f'Rows: {categoric_box}')
    st.write(mn.df[[categoric_box]+[principal_radio]].groupby(categoric_box)[principal_radio].agg(['sum','describe']))

    
    c_min,c_max = fn.categoric_grouped(mn.df,categoric_box,principal_radio,mn.total_variables)

    st.markdown(f'Information of the min value of the variable: {principal_radio}')
    st.dataframe(c_min)

    st.markdown(f'Information of the max value of the variable: {principal_radio}')
    st.dataframe(c_max)


