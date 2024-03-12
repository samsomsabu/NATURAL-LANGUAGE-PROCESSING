import streamlit as st
import pandas as pd

# Load the IPC data from the CSV file
ipc_data = pd.read_csv("C:/Users/samso/OneDrive/Desktop/ipc_sections.csv")  # Replace 'ipc_data.csv' with the actual filename
# Create a dictionary to store IPC section details
ipc_dict = {}
for index, row in ipc_data.iterrows():
    section_number = row['Section']
    ipc_dict[section_number] = {
        'Description': row['Description'],
        'Offense': row['Offense'],
        'Punishment': row['Punishment']
    }

# Streamlit app
def main():
    st.title('Indian Penal Code Chatbot')

    user_input = st.text_input('Enter IPC Section Number:')
    if user_input:
        user_input = user_input.upper()  # Convert input to uppercase for consistency
        if user_input in ipc_dict:
            st.subheader(f'IPC Section {user_input}')
            st.markdown(f'**Description:** {ipc_dict[user_input]["Description"]}')
            st.markdown(f'**Offense:** {ipc_dict[user_input]["Offense"]}')
            st.markdown(f'**Punishment:** {ipc_dict[user_input]["Punishment"]}')
        else:
            st.error('Invalid IPC Section Number. Please enter a valid section number.')

if __name__ == '__main__':
    main()