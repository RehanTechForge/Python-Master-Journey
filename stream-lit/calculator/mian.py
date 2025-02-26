import streamlit as st

first_value = st.number_input("Enter No :",key="first_value")
second_value = st.number_input("Enter No :",key="second_value")
result = None

if st.button("Addition"):
  result = int(first_value) + int(second_value)

if st.button("Subtraction"):
  result = int(first_value) - int(second_value)

if st.button("Multiplication"):
  result = int(first_value) * int(second_value)

if st.button("Division"):
  result = int(first_value) / int(second_value)

if result is not None:
  st.write("Result:",result)


# import streamlit as st

# # Number input fields (default 0 rakha hai)
# first_value = st.number_input("Enter First Number:", key="first_value", value=0)
# second_value = st.number_input("Enter Second Number:", key="second_value", value=0)

# result = None  # Store result

# # Single button click handling
# operation = None
# if st.button("Addition"):
#     operation = "add"
# elif st.button("Subtraction"):
#     operation = "subtract"
# elif st.button("Multiplication"):
#     operation = "multiply"
# elif st.button("Division"):
#     operation = "divide"

# # Perform the selected operation
# if operation:
#     if operation == "add":
#         result = first_value + second_value
#     elif operation == "subtract":
#         result = first_value - second_value
#     elif operation == "multiply":
#         result = first_value * second_value
#     elif operation == "divide":
#         if second_value == 0:
#             st.error("Division by zero is not allowed!")
#         else:
#             result = first_value / second_value

# # Display the result
# if result is not None:
#     st.success(f"Result: {result}")
