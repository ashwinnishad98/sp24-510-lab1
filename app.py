import textwrap

import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🙋‍♂️ Hi this is Ashwin's Website! 🙋‍♂️")
    st.image("/Users/ashwinnishad/Downloads/UW/Spring24/510/sp24-510-lab1/pfp.jpeg")


st.header("About Me")
st.text(
    textwrap.fill(
        "Hi! My name is Ashwin and I'm a graduate student at UW! I spent most of my life growing up in Abu Dhabi and I moved to Dallas to pursue my bachelors degree. After graduating, I worked as a Software Engineer for 3 years at a Marketing Technology company.",
        width=150,
    )
)
st.divider()

st.header("Education")
st.text(
    textwrap.fill(
        "I have completed my Bachelors in Computer Science from the University of Texas at Dallas. I'm currently pursuing my Masters in Technology Innovation at the University of Washington.",
        width=150,
    )
)
st.divider()

st.header("Work Experience")
st.text(
    textwrap.fill(
        "I have worked as a Software Engineer at Epsilon for 3 years. I was primarily involved as a solutions architect, working on automating infrastructure in AWS, defining data engineering pipelines to perform ETL operations, and developing a microservice architecture from the ground up.",
        width=150,
    )
)
st.divider()

st.header("Hobbies and Interests")
st.text(
    textwrap.fill(
        "I'm interested in a lot of different things but my current interests that I try to keep up with are Formula 1, reading non-fiction books (currently reading The Gene by Siddhartha Mukherjee), and exploring Seattle when I can! My hobbies include cooking and digital art to draw my own tattoos!",
        width=150,
    )
)
st.divider()

st.header("Projects")
st.text(
    "I have worked on a lot of different projects but I will list some notable ones: "
)
st.subheader("1. AR Shopping Assistant POC")
st.text(
    textwrap.fill(
        "An AR application that allows shoppers to scan items in store, to view pricing, information and reviews through an AR interface. It leveraged computer vision to identify products and we overlayed information on top of the product.",
        width=150,
    )
)
st.subheader("2. Twitter Sentiment Analysis")
st.text(
    textwrap.fill(
        "To get more experience with full stack development using Javascript, I created a web application deployed on Heroku that allows the user to enter a topic, and tweets related to that topic are streamed in realtime and analyzed for the sentiment. They are then displayed on the screen as a pie chart, labeled as positive, negative or neutral.",
        width=150,
    )
)
st.subheader("3. Speech Assisstant for Stroke Patients")
st.text(
    textwrap.fill(
        "I worked on a project that involved creating a speech assistant for stroke patients. The application leveraged AI to detect stutters or other impediments in speech, and based on the context of the conversation, it would provide suggestions to the patient to help them communicate. The project qualified for the Microsoft Imagine Cup and we also made it to the final of the Hollomon Health Innovation Challenge hosted by the Foster school at UW.",
        width=150,
    )
)
