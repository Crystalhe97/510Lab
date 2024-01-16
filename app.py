import streamlit as st

st.set_page_config(
    page_title="Yuwei He - Student",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://raw.githubusercontent.com/Crystalhe97/510Lab/main/WechatIMG5371.jpg)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://raw.githubusercontent.com/Crystalhe97/510Lab/main/WechatIMG5371.jpg')
with col2:
    st.markdown(
        """
    # Yuwei He (She/Her)
                
    - Student at University of Washington
        """
    )

st.markdown(
    """
# Education

- [B.A. Communication at University of Washington](https://www.washington.edu)
- [B.A. Japanese at University of Washington](https://www.washington.edu)
- [M.A. Strategy Communication at Johns Hopkins University](https://www.jhu.edu)
"""
)

st.markdown(
    """
# Hobbies and Interests
- Love cats
- Love eating and exploring restaurants
""")
col1, col2, col3 = st.columns(3)

# Photos want to share
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://github.com/Crystalhe97/510Lab/blob/main/WechatIMG5325.jpg?raw=true)
        </div>
        """,
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns(3)

# Photos want to share
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://github.com/Crystalhe97/510Lab/blob/main/WechatIMG5321.jpg?raw=true)
        </div>
        """,
        unsafe_allow_html=True,
    )


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
