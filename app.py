import streamlit as st

# Title
st.title(" ABDULLAH AL SHAKHEE \n--------------------------\n - Made This BMI Calculator \n - Copyright researved \n--------------------------")

# Sidebar Title
st.sidebar.title("User Information")

# Sidebar Input: Name
name = st.sidebar.text_input("Enter your name:", "")
if name:
    st.sidebar.success(f"Hello, {name}! Let's calculate your BMI.")

# Sidebar Input: Age
age = st.sidebar.slider("Select your age (in Years)", 0, 100, 25)
st.sidebar.write(f"Your selected age: {age} Years")

# Sidebar Input: Weight
weight = st.sidebar.slider("Select your weight (in KG)", 0, 200, 25)
st.sidebar.write(f"Your selected weight: {weight} KG")

# Sidebar Input: Height (Feet & Inches)
st.sidebar.write("Select your height:")
feet = st.sidebar.number_input("Feet", min_value=0, max_value=7, value=5, step=1)
inches = st.sidebar.number_input("Inches", min_value=0, max_value=11, value=7, step=1)

# Convert height to meters
height_meters = (feet * 0.3048) + (inches * 0.0254)
st.sidebar.write(f"Your height: {feet} feet {inches} inches ({height_meters:.2f} meters)")

# BMI Calculation
if height_meters > 0:
    BMI = float(weight / (height_meters ** 2))
    st.write(f"### Welcome, {name}! Your Age is {age} \n And \n ### BMI is **{BMI:.2f} Kg/m²**.")
    
    # BMI Categories
    if BMI < 18.5:
        st.warning("You are **Underweight**.")
    elif 18.5 <= BMI < 24.9:
        st.success("You have a **Normal weight**. ✅")
    elif 25 <= BMI < 29.9:
        st.warning("You are **Overweight**.")
    else:
        st.error("You are in the **Obese** category. ⚠️")

else:
    st.error("Invalid height! Please enter a valid height to calculate BMI.")
