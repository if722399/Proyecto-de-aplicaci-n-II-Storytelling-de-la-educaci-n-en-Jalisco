from re import X
import streamlit as st
import main as mn
import visualizations as vs
import plotly.express as px
import functions as fn


# Disable warning 
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Aplication project II - Jalisco education storytelling')

st.markdown('## 1. Property')
st.markdown('### Main variable to analize')

principal_radio = st.radio(
        '',
         ['AULAS_EXISTENTES','AULAS_USO','BENEFICIARIOS_ALIMENTOS_DIF_2014_digit','CONECTIVIDAD_mbs']
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

    show_map = st.checkbox('Show Map')
    if show_map:
        st.pyplot(vs.map_viz(principal_radio))


    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    show_dax = st.checkbox('Show Double Y Axis Plot')
    if show_dax:
        st.plotly_chart(vs.dax_viz(principal_radio,numeric_box))



        #st.plotly_chart(vs.double_ax_plot(mn.df.MUNICIPIO,mn.df[principal_radio],mn.df[numeric_box]))


    # Categoric pendiente

if v_type == 'Categoric':
    categoric_box = st.selectbox(
        'Choose a numeric variable',
        mn.categoric_performers.columns
    )

    st.markdown('#### Descriptive statistics')
    st.text(f'Columns: {principal_radio}')
    st.text(f'Rows: {categoric_box}')
    st.write(mn.df[[categoric_box]+[principal_radio]].groupby(categoric_box)[principal_radio].agg(['sum','describe']))
