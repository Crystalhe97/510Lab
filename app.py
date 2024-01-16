import streamlit as st

# Set up the title for your website
st.title("My Personal Website")

# Profile Picture
st.header("Profile Picture")
# Assuming you have a profile picture named 'profile_pic.jpg' in the same directory
st.image("profile_pic.jpg", caption='YuweiHe')

# About
st.header("About")
st.write("Yuwei He - Student")

# Education
st.header("Education")
st.write("B.A. Communication @UW")
st.write("B.A. Japanese @UW")
st.write("M.A. Strategy Communication @JHU")

# Hobbies and Interests
st.header("Hobbies")
st.write("Love eating foods and exploring restaurant")
# To run the app, save this script as 'app.py' and in the terminal run 'streamlit run app.py'