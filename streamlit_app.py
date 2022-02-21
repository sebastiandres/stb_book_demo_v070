import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Streamlit Book", page_icon="📖",)

# Streamit book properties
save_answers = True
stb.set_library_config(menu_title="",
                       options=[
                                "Intro",   
                                "Multitest", 
                                "To Do list", 
                                "True or False", 
                                "Multiple Choice", 
                                "Single Choice",
                                "Demo Day",
                                "End",   
                                ], 
                       paths=[
                              "pages/streamlit_book_examples/Intro.py", 
                              "pages/streamlit_book_examples/00 Multitest", 
                              "pages/streamlit_book_examples/01 To do Lists", 
                              "pages/streamlit_book_examples/02 True or False",
                              "pages/streamlit_book_examples/03 Multiple choice",
                              "pages/streamlit_book_examples/04 Single choice",
                              "pages/streamlit_book_examples/DemoDay",                             
                              "pages/streamlit_book_examples/End.md", 
                              ],
                       icons=["tree", 
                              "code", 
                              "robot", 
                              "moon", 
                              "alarm", 
                              "activity", 
                              "apple",
                              "tree",
                              ],
                       save_answers=save_answers,
                       )