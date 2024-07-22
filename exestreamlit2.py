import streamlit as st

st.title('Temperature Converter')

temper = st.number_input('Enter temperature value')

option = st.selectbox('Select unit', 
             ['Celsius to Fahrenheit', 'Fahrenheit to Celsius'])

button_convert = st.button('Convert')

if button_convert == True:
    if option == 'Celsius to Fahrenheit':
        temper = (temper * 9/5) + 32
    elif option == 'Fahrenheit to Celsius':
        temper = (temper - 32) * 5/9

    st.write(f'Converted temperature: {temper:.2f}')
