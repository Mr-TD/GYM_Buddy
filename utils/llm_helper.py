import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def Gym(name,age,weight,height,gender,selected_options):
    if gender == 'Male':
        gender_suffix = 'He'
    elif gender == 'Female':
        gender_suffix = 'She'

    if len(selected_options) == 1:
        selected_options = selected_options[0]
    else:
        selected_options = additioal_info = ' and '.join(selected_options)
        
    with open("Prompts/Gym.prompt", "r") as f:
        template = f.read()
    
    template = PromptTemplate(template=template,input_variables=["name","age","height","weight","gender","gender_suffix","fitness_goal"])
    formatted_input = template.format_prompt(
        name = name,
        age = age,
        height = weight,
        weight = height,
        gender = gender,
        gender_suffix = gender_suffix,
        fitness_goal = selected_options
    )

    response = model.generate_content(formatted_input.to_string())

    final_response = response.text

    return final_response

def Home(name,age,weight,height,gender,selected_options):
    if gender == 'Male':
        gender_suffix = 'He'
    elif gender == 'Female':
        gender_suffix = 'She'
    
    if len(selected_options) == 1:
        selected_options = selected_options[0]
    else:
        selected_options = additioal_info = ' and '.join(selected_options)
        
    with open("Prompts/Home.prompt", "r") as f:
        template = f.read()
    
    template = PromptTemplate(template=template,input_variables=["name","age","height","weight","gender","gender_suffix","fitness_goal"])
    formatted_input = template.format_prompt(
        name = name,
        age = age,
        height = weight,
        weight = height,
        gender = gender,
        gender_suffix = gender_suffix,
        fitness_goal=selected_options,
    )

    response = model.generate_content(formatted_input.to_string())

    final_response = response.text

    return final_response

def Gym_Home(name,age,weight,height,gender,selected_options,flexibility,gym,home):
    if gender == 'Male':
        gender_suffix = 'He'
    elif gender == 'Female':
        gender_suffix = 'She'

    if flexibility == 'Specify a day':
        additioal_info = str(gym) + " day Gym and " + str(home) + ' day home.' 
    else:
        additioal_info = ' and '.join(flexibility)
    
    if len(selected_options) == 1:
        selected_options = selected_options[0]
    else:
        selected_options = additioal_info = ' and '.join(selected_options)
        
    with open("Prompts/Gym_home.prompt", "r") as f:
        template = f.read()
    
    template = PromptTemplate(template=template,input_variables=["name","age","height","weight","gender","gender_suffix","additioal_info","fitness_goal"])
    formatted_input = template.format_prompt(
        name = name,
        age = age,
        height = weight,
        weight = height,
        gender = gender,
        gender_suffix = gender_suffix,
        additioal_info = additioal_info,
        fitness_goal=selected_options
    )

    response = model.generate_content(formatted_input.to_string())

    final_response = response.text

    return final_response

def main(form_name,form_age,form_weight,form_height,form_gender,form_access,form_flexibility,form_gym,form_home,form_selected_options):
    if len(form_access) == 1:
        if form_access[0] == 'Gym':
           final_response =  Gym(name = form_name,age = form_age,weight = form_weight,height = form_height,gender = form_gender,selected_options = form_selected_options)
        elif form_access[0] == 'Home':
            final_response =  Home(name = form_name,age = form_age,weight = form_weight,height = form_height,gender = form_gender,selected_options = form_selected_options)
        else:
            final_response = 'Something went wrong'
    elif form_access == ['Gym','Home']:
        final_response =  Gym_Home(name = form_name,age = form_age,weight = form_weight,height = form_height,gender = form_gender,selected_options = form_selected_options,flexibility=form_flexibility,gym=form_gym,home=form_home)
    else:    
        final_response = 'Something went wrong'

    return final_response


if __name__ == "__main__":
    print(main(
        name = 'Dharmik',
        age = 25,
        height = 178,
        weight = 97.7,
        gender = 'Male'
    ))