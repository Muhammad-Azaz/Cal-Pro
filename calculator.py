import streamlit as st

def main():
    st.title("Simple Calculator")

    # Get user input
    number1 = st.number_input("Enter first number")
    number2 = st.number_input("Enter second number")
    
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform the operation
    if operation == "Add":
        result = number1 + number2
    elif operation == "Subtract":
        result = number1 - number2
    elif operation == "Multiply":
        result = number1 * number2
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error! Division by zero."
    
    # Display the result
    st.write("Result:", result)

if __name__ == "__main__":
    main()
