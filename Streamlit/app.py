# Streamlit
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Title and Introduction
st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey")
st.write(
    "This web app is designed to help you develop a **growth mindset** by embracing challenges, learning from failures, "
    "and staying motivated. 🌱🚀\n\n"
    "Explore daily challenges, get inspired by motivational quotes, and track your progress as you cultivate resilience and "
    "continuous improvement."
)

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.success("**“Success is not an accident, success is a choice.”** – Stephen Curry")

# Challenge Input
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_area("Describe a challenge you are facing:")

if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward toward your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: **{reflection}**")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievement Section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: **{achievement}**")
else:
    st.info("Big or small, every achievement counts! Share one now 😊")

# Footer
st.write("---")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**©️ Created by Faria Usman**")
