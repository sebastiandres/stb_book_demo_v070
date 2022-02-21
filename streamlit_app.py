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
                              "pages/Intro.py", 
                              "pages/00 Multitest", 
                              "pages/01 To do Lists", 
                              "pages/02 True or False",
                              "pages/03 Multiple choice",
                              "pages/04 Single choice",
                              "pages/DemoDay",                             
                              "pages/End.md", 
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