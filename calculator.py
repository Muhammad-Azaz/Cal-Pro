import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")

# Dropdown for selecting the operation
operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Initialize result variable
result = None

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = number1 + number2
    elif operation == "Subtraction":
        result = number1 - number2
    elif operation == "Multiplication":
        result = number1 * number2
    elif operation == "Division":
        if number2 != 0:
            result = number1 / number2
        else:
            st.error("Division by zero is not allowed.")
    
    # Display the result
    if result is not None:
        st.success(f"The result of {operation} is: {result}")
