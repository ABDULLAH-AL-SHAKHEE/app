import streamlit as st

# Title
st.title(" BMI Calculator ")
st.write(f" MADE BY ABDULLAH AL SHAKHE \n - Copyright researved")

# Sidebar Title
st.sidebar.title("User Information")

# Sidebar Input: Name
name = st.sidebar.text_input("Enter your name:", "")
if name:
    st.sidebar.success(f"Hello, {name}! Let's calculate your BMI.")

# Sidebar Input: Age
st.sidebar.write("Select your AGE:")
age = st.sidebar.number_input("AGE IN YEAR ", min_value=0, max_value=500, value=5, step=1)
st.sidebar.write()


# Sidebar Input: Weight
st.sidebar.write("Select your Weight:")
kg = st.sidebar.number_input("Kilo Gram", min_value=0, max_value=500, value=5, step=1)
g = st.sidebar.number_input("Gram", min_value=0, max_value=999, value=7, step=1)
st.sidebar.write()



# Sidebar Input: Height (Feet & Inches)
st.sidebar.write("Select your height:")
feet = st.sidebar.number_input("Feet", min_value=0, max_value=7, value=5, step=1)
inches = st.sidebar.number_input("Inches", min_value=0, max_value=11, value=7, step=1)


# Convert height to meters
weight = (kg) + (g / 1000)
height_meters = (feet * 0.3048) + (inches * 0.0254)



# BMI Calculation
if height_meters > 0:
    BMI = float(weight / (height_meters ** 2))
    st.write(f" Welcome, {name}!! Your Are {age} Years Old")
    st.write(f" Your are {feet} feet {inches} inches ({height_meters:.2f} meters) tall")
    st.write(f" ### BMI is **{BMI:.2f} Kg/m²**.")
    
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
