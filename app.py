import streamlit as st
from PIL import Image
import utils.llm_helper as helper
import utils.BMI_graph as plot

def main():
    # Page icon
    icon = Image.open('Resource/td-logo.png')

    # Page config
    st.set_page_config(page_title="GYM",
                       page_icon=icon,
                       layout="wide"
                       )

    company_logo_path = 'Resource/td-logo.png'
    st.sidebar.image(company_logo_path, width=50)

    name = st.sidebar.text_input("Name")

    # Non-negative Integer Field for Age
    age = st.sidebar.number_input("Age", min_value=0, step=1)

    # Non-negative Float Field for Weight
    weight = st.sidebar.number_input("Weight (kg)", min_value=0.0, step=0.1)

    # Non-negative Float Field for Height
    height = st.sidebar.number_input("Height (cm)", min_value=0.0, step=0.1)

    # Long Text Field for Medical Conditions
    medical_conditions = st.sidebar.text_area("Medical Conditions")

    # Radio Button for Gender
    gender_options = ["Male", "Female"]
    gender = st.sidebar.radio("Gender", gender_options,horizontal=True)

    # Checkbox for Fitness Goals
    st.sidebar.write("Accessability")
    access_options = ["Gym", "Home"]
    accessability = st.sidebar.multiselect("Select options:", access_options)
    if accessability == [] or len(accessability) == 1:
        flexibility = ''
        gym = 0
        home = 0
        gym_home = gym + home
    else:
        flexibility_option = ["Gym & Home everyday", "Gym & Home on alternate day","Specify a day"]
        flexibility = st.sidebar.radio("Flexibility", flexibility_option,horizontal=True)
        if flexibility_option == 'Gym & Home everyday':
            flexibility_option = 'Provide a workout plane each day Gym workout and home workout so same day both workout plane should be there (e.g. Day 1 : Monday Gym,Home Day 2 : Tuesday Gym,Home till Day 7 : Sunday Gym,Home)'
        elif flexibility == 'Specify a day':
            gym = st.sidebar.number_input("Gym day", min_value=1, step=1)
            home = st.sidebar.number_input("Home day", min_value=1, step=1)
            gym_home = gym + home
        else:
            gym = 0
            home = 0
            gym_home = gym + home
        


    # Checkbox for Fitness Goals
    st.sidebar.write("Fitness Goals")
    fitness_goals_options = ["Weight Loss", "Stay Fit", "Muscle Building"]
    selected_options = st.sidebar.multiselect("Select options:", fitness_goals_options)

    if st.sidebar.button("Submit"):
        if age == 0:
            st.error("Age is a mandatory field.")
        elif weight == 0:
            st.error("weight is a mandatory field.")
        elif height == 0:
            st.error("height is a mandatory field.")
        elif len(access_options) == 0:
            st.error("Select atleast one option.")
        elif gym_home >=8:
            st.error("Gym day and Home day as per week please check value addition of both values should be 7 or less")
        elif len(selected_options) == 0:
            st.error("Select atleast one fitness goal.")
        else:
            with st.spinner('Generating Workout Plan...'):
                #with st.container(border=True):
                if name != '':
                    st.title(f"***Hello {name}***")
                else:
                    st.title(f"***Hello There***")

                fig = plot.BMI_Value(height=height, weight=weight)
                #fig.update_traces(x=[value], selector=dict(name="Value"))
                #fig.update_traces(x=[max_value], selector=dict(name="Forward Arrow"))
                st.plotly_chart(fig)
                #st.write(name,age,weight,height,gender,accessability,flexibility,gym,home,selected_options)
                response = helper.main(name,age,weight,height,gender,accessability,flexibility,gym,home,selected_options)
                st.write(response)





if __name__ == '__main__':
    main()