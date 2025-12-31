import streamlit as st
import time
from textblob import TextBlob

st.title("Sentiment Analysis")

st.divider()

st.header("Enter a sentence to analyze its sentiment.")

user_input = st.text_input("")

if st.button("Analyse Sentiments") and user_input:
    blob = TextBlob(user_input)
    sentimentp = blob.sentiment.polarity          #negative(-1) -> neutral(0) -> positive(1)
    sentiments = blob.sentiment.subjectivity      #fact(0) -> opinion(1)

    if sentimentp > 0.5:
        st.subheader("Strongly Positive 😄 ")

    elif sentimentp > 0.1:
        st.subheader("Positive 🙂 ")

    elif sentimentp >= -0.1:
        st.subheader("Neutral 😐 ") 

    elif sentimentp > -0.5:
        st.subheader("Negative 😕 ")       

    else:
        st.subheader("Super Negative 😡 ")

    st.write(f"**Sentiment/Polarity Score: {sentimentp}** ")            

    st.progress((sentimentp + 1) / 2)

    #col1, col2, col3, col4, col5 = st.columns(5)
    #col1.markdown("-1")
    #col3.markdown("0")
    #col5.markdown("1")

    st.markdown("""<div style="display: flex; justify-content: space-between; font-weight: bold;">
                <span>-1</span>
                <span style="text-align:center;">0</span>
                <span>1</span>
                </div>""",
                unsafe_allow_html=True)
    
    time.sleep(1)
    st.divider()
    time.sleep(1)

    if sentiments > 0.5:
        st.subheader("This is mostly an Opinion")
    elif sentiments == 0.5:
        st.subheader("This is Mixed: opinion and fact") 
    else:
        st.subheader("This is mostly a Fact")       

    st.write(f"**Subjectivity Score: {sentiments}** ")

    st.progress((sentiments + 1) / 2)

    #col1, col2, col3, col4, col5 = st.columns(5)
    #col1.markdown("-1")
    #col3.markdown("0")
    #col5.markdown("1")

    st.markdown("""<div style="display: flex; justify-content: space-between; font-weight: bold;">
                <span>0</span>
                <span>1</span>
                </div>""",
                unsafe_allow_html=True)
    
    time.sleep(1)
    st.divider()

    st.subheader("Thank you! All Done.")

else:
    st.write("For Analysing Sentiments please type in statement.")    