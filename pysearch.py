import streamlit as st
import resources.ai as ai
import itertools

# import pybites_search - this doesn't work?
# import search_content

from .search_content import search_for_content  # why dot? same directory?


def pysearch():
    with st.container():
        # Display Title
        st.title("PyBites Search")

        # Display Example Questions
        st.markdown("""
        Example questions:
        - "How can I build an API?"
        - "How can I verify a data structure?"
        - "How can I convert ISO time to human-readable time?"
        - "How do I scrape a webpage?"
        - "What should I use to handle SQL databases in Python?"
        - "How can I create a GUI for my Python application?"
        - "How can I parallelize tasks in Python?"
        - "How can I test my Python code?"
        - "What can I use to handle HTTP requests?"
        - "How do I work with machine learning in Python?"
        """)

        # Text input
        user_input = st.text_input("Please enter your question:")

        if st.button("Submit"):
            extracted_subject = ai.extract_subject(user_input)
            recommended_framework = ai.python_framework_recommendation(extracted_subject)
            string_response = f"It looks like you are interest in {extracted_subject}, I would recommend searching {recommended_framework}"
            st.write(ai.generate_nl(string_response))

            # Change extracted_subject from list to string
            # Method 1
            if isinstance(extracted_subject, list):
                extracted_subject = extracted_subject[0]

            # Method 2
            # if isinstance(extracted_subject, list):
            #     extracted_subject = ' '.join(extracted_subject)

            # Put extracted_subject into a key in session state
            st.session_state["subject"] = extracted_subject

            # Also add channel as a key in session state
            st.session_state["channel"] = "All"

            # if "subject" in st.session_state:
            #     extracted_subject = st.session_state["subject"]

            # Channel Functionality
            # channels = [
            #     "All Content",
            #     "Pybites Articles",
            #     "Pybites Bite Exercises",
            #     "Pybites Podcasts",
            #     "Pybites YouTube Videos",
            # ]
            # selected_channel = st.radio("Select Content:", channels, index=0)

            with st.spinner("Searching....."):
                # Do the Search
                results = search_for_content(extracted_subject)

                if results:
                    results.sort(key=lambda x: x.channel)

                    # if selected_channel != "All Content":
                    #     # Group
                    #     results = [r for r in results if r.channel == selected_channel]

                    if results:
                        grouped_results = itertools.groupby(results, key=lambda x: x.channel)
                        # Display
                        for channel, group in grouped_results:
                            group_list = list(group)
                            st.markdown(f"## {channel}")
                            for result in group_list:
                                st.markdown(f" - [{result.title}]({result.url})")
                    else:
                        st.write("No Results Found")
                else:
                    st.write("None")
