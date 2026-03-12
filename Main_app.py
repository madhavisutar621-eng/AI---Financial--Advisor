import streamlit as st

st.title("AI Financial Advisor")

income = st.number_input("Enter your monthly income")

expenses = st.number_input("Enter your monthly expenses")

if st.button("Calculate"):
    savings = income - expenses
    st.write("Your savings:", savings)

    if savings > 5000:
        st.success("Great! You can invest in mutual funds or SIP.")
    elif savings > 0:
        st.info("Try to save more and start small investments.")
    else:
        st.error("Your expenses are higher than income.")
