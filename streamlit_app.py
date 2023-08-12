import streamlit
import pandas

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatemeanl ')
streamlit.text('🥗 Kale , spinach & Rocket smoothies')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocodo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
