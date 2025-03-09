import streamlit as st
import pandas as pd 

st.set_page_config(page_title="Growth MIndset Project",page_icon="⭐")
st.title("Growth Mindset Challenge:Web App with Streamlit")

st.header("Welcome to the Growth Mindset Challenge")
st.write("Embrace challenges, learn from mistakes, and unlock yuor full potentential")

#quote section
st.header("today Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:it is the courage to continue that counts")

st.header("what's your challene today?")
user_input=st.text_input("Describe a challenge you'r facing")

#condition
if user_input:
    st.success(f"you're facing:{user_input} keep pushing fprward yoyr goal!")
else:
    st.warning("Tell us about your challenge!")

    #reflection

    st.header("Reflection on your learning")
    reflection=st.text_area("write your reflection here")

    if reflection:
        st.success(f"Great Insight! Your reflection:{reflection}")
    else:
        st.info("Reflecting on past experience help your goal share your difficulties")

        #acchievement

        st.header("Celebrate your win")
        achievement=st.text_input("Share something you have recentaly acompalished")
        if achievement:
            st.success(f"🌠Amazing! You achieved{achievement}")
        else:
            st.info("Big or small , every achievement counts! Share one now😍")

            #footer
            st.write("----")
            st.write("Keep believing in yourself. Growth is a journey, not a destination!🌟")
            st.write("***✏ Created By M.Tahir***")
