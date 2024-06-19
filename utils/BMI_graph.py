import streamlit as st
import plotly.graph_objs as go

def BMI_Value(height,weight):
    height = height/100
    bmi = weight / (height ** 2)


    color = "black"
    if bmi <= 18.5:
        bmi_class = 'Thin'
        color = "blue"
    elif bmi <  24.0:
        bmi_class = 'Ideal'
        color = "green"
    elif bmi < 28.0:
        bmi_class = 'Fat'
        color = "yellow"
    else:
        bmi_class = 'Obesity'
        color = "red"
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = bmi,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "BMI"},
        number = {'font': {'color': color},'suffix': f"<br>({bmi_class})"},  # Change number color based on value
        gauge = {'axis': {'range': [None, 60]},
                 'bar': {'color': "white",'thickness': 0},
                 'steps' : [
                     {'range': [0, 18.5], 'color': "blue"},
                     {'range': [18.5, 24.0], 'color': "green"},
                     {'range': [24.0, 28.0], 'color': "yellow"},
                     {'range': [28.0, 60], 'color': "red"}],
                 'threshold' : {'line': {'color': "black", 'width': 7}, 'thickness': 1, 'value': bmi}}))

    fig.add_trace(go.Scatter(
        x=[0],
        y=[0],
        #marker=dict(color="red", size=12),
        showlegend=False,
        name="BMI",
    ))

    

    fig.update_layout(width=400, height=300, plot_bgcolor='rgba(0,0,0,0)', showlegend=False, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
    
    fig.update_traces(x=[bmi], selector=dict(name="BMI"))

    return fig


if __name__ == "__main__":
    BMI_Value()