import streamlit as st
# Import the backend function we just wrote
from project_static import get_researcher_info

st.title("Researcher Information Form")
st.write("Ask anything about the researcher and get the answer in seconds.")

# 1. Create the form container
with st.form(key="user_info_form"):
    # 2. Add input field inside the form block
    name = st.text_input(label="Enter researcher name or question:")
    
    # 3. Every form MUST have a submit button
    submit_button = st.form_submit_button(label="Submit Details")

# 4. Handle logic after button click
if submit_button:
    if name.strip() == "":
        st.warning("Please enter a name or question first!")
    else:
        # Show loading spinner while calling our split backend function
        with st.spinner("Searching for researcher information..."):
            answer = get_researcher_info(name)
            
            st.subheader("Answer:")
            st.write(answer)