import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Single Choice Question")

# Required arguments
st.header("Question with minimal arguments")
c1, c2 = st.columns([5,5])
with c1:
    st.code("""
    stb.single_choice(
                    "What is the current streamlit version?", # required argument
                    ["0.4.0", "0.5.0", "1.5.0"], # required argument
                    2 # required argument
                    )
        """)
with c2:
    stb.single_choice(
                    "What is the current streamlit_book version?", # required argument
                    ["0.4.0", "0.5.0", "0.7.0"], # required argument
                    2 # required argument
                    )

# All arguments
st.header("Question with all optional arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
    stb.single_choice(
                    "What is the current streamlit_book version?", # required argument
                    ["0.4.0", "0.5.0", "0.7.0"], # required argument
                    2, # required argument
                    success='Pfiuuuuu!!!', 
                    error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                    button='Check MY answer'
                    )
        """)
with c2:
    stb.single_choice(
                    "What is the next streamlit_book version?", # required argument
                    ["0.4.0", "0.7.0", "0.8.0"], # required argument
                    2, # required argument
                    success='Pfiuuuuu!!!', 
                    error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                    button='Check MY answer'
                    )

# Custom question
st.header("Question with custom behavior")
c1, c2 = st.columns([4,3])
with c1:
    st.code("""
    checked_answer, correct_answer = stb.true_or_false("Are you a cyborg robot?", 
                                                False, 
                                                success="",
                                                error="",
                                                button='Check THIS answer')
    if checked_answer:
        if correct_answer:
            st.info("Welcome fellow human!")            
            st.balloons()
        else:
            N = 10.0
            pb = st.progress(0.0)
            ph = st.empty()
            robot_message = ""
            for i in range(1, int(N+1)):
                pb.progress(i/N)
                robot_message += random.choice(["Bip ", "bip ", "Bop ", "bop "])
                ph.code(robot_message)
                time.sleep(.5)
    else:
        st.write("You need to check the answer")
        """)
with c2:
    checked_answer, correct_answer = stb.single_choice(
                    "What is the next streamlit_book version?", # required argument
                    ["0.4.0", "0.5.0", "0.7.0"], # required argument
                    2, # required argument
                    success='Pfiuuuuu!!!', 
                    error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                    button='Check THE answer'
                    )

    if checked_answer:
        if correct_answer:
            st.info("Welcome fellow human!")            
            st.balloons()
        else:
            N = 10.0
            pb = st.progress(0.0)
            ph = st.empty()
            robot_message = ""
            for i in range(1, int(N+1)):
                pb.progress(i/N)
                robot_message += random.choice(["BIP ", "bip ", "BOP ", "bop "])
                ph.code(robot_message)
                time.sleep(.5)
    else:
        st.write("You need to check the answer")