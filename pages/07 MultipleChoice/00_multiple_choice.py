import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Multiple Choice Question")

# Default
st.header("Question with minimal arguments")
c1, c2 = st.columns([5,5])
with c1:
    st.code("""
    stb.multiple_choice(
                        "What are 1 ...", # required argument
                        {"a":True, "b":False, "c":False} # required argument
                        )
    """)
with c2:
    stb.multiple_choice(
                        "What are 1...", # required argument
                        {"a":True, "b":False, "c":False} # required argument
                        )
# Default
st.header("Question with all optional arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
        stb.true_or_false("Are you a cyborg?", False, 
                            success='Pfiuuuuu!!!', 
                            error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                            button='Check MY answer')
        """)
with c2:
    stb.multiple_choice(
                        "What are 2...", # required argument
                        {"a":True, "B":False, "c":False}, # required argument
                        success='Pfiuuuuu!!!', 
                        error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                        button='Check MY answer')

# Custom question
st.header("Question with custom behavior")
c1, c2 = st.columns([4,3])
with c1:
    st.code("""
adsad
        """)
with c2:
    checked_answer, correct_answer = stb.multiple_choice("What are 3...", # required argument
                                                        {"A":True, "B":False, "C":False}, # required argument
                                                        success="",
                                                        error="",
                                                        button='Check THE answer')
    if checked_answer:
        if correct_answer:
            st.info("Welcome fellow human!")            
            st.balloons()
        else:
            st.info("Welcome fellow human!")            
            st.balloons()
    else:
        st.write("You need to check the answer")