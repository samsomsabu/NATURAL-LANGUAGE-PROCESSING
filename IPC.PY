import streamlit as st
import pandas as pd

# Load the IPC data from the CSV file
ipc_data = pd.read_csv("C:/Users/samso/OneDrive/Desktop/ipc_sections.csv") 

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

    user_input = st.text_input('Enter the Offense:')
    user_input = user_input.lower()  # Convert input to lowercase for consistency

    matching_sections = []
    for section, details in ipc_dict.items():
        # Check if 'Offense' value is not NaN before converting to lowercase
        if pd.notna(details['Offense']) and user_input in details['Offense'].lower():
            matching_sections.append(section)

    if matching_sections:
        st.subheader(f'IPC Sections related to "{user_input}"')
        for section in matching_sections:
            st.markdown(f'**Section {section}**')
            st.markdown(f'**Description:** {ipc_dict[section]["Description"]}')
            st.markdown(f'**Punishment:** {ipc_dict[section]["Punishment"]}')
            st.markdown('---')
    else:
        st.error(f'No IPC Sections found related to "{user_input}".')

if __name__ == '__main__':
    main()