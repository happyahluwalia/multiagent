
import streamlit as st
from phi.assistant import Assistant
from phi.tools.hackernews import HackerNews
from phi.llm.openai import OpenAIChat

# Set up the Streamlit app title and description
st.title("AI Researcher 🔍🤖")
st.caption("Research stories from hacker news to generate additional content "
           "like social media posts, reports, blogs, tweets")

# Prompt user for OpenAI API key securely (password type input)
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Error container for displaying API errors or input issues
error_container = st.empty()

# Check if API key is provided before proceeding
# we are going to create 2 agents with different roles, a researcher and a reader
if openai_api_key:
    try:
        # Create a HackerNews story researcher agent
        story_researcher = Assistant(
            name="HN Researcher",
            role="Finds interesting top stories and users on HackerNews.",
            tools=[HackerNews()], 
        )

        # Create a HackerNews user researcher agent
        user_researcher = Assistant(
            name="Researcher",
            role="Reads articles and user information from URLs on HN",
            tools=[HackerNews()],  # Same tool as story_researcher, but different role
        )

        # Combine researchers & reader into a team and configure the OpenAI LLM with GPT-4 model
        hn_assistant = Assistant(
            name="Research Team",
            team=[story_researcher, user_researcher],  # Grouping agents into a team
            llm=OpenAIChat(  # Using OpenAI's GPT-4 model
                model="gpt-4",  # Ensure correct model version
                max_tokens=1024,  # Limit token usage
                temperature=0.5,  # Set temperature for response creativity
                api_key=openai_api_key  # Securely pass the API key
            )
        )

        # Input field for the user to enter a research query
        query = st.text_input("Enter your research question:")

        # Check if a query is provided
        if query:
            try:
                # Run the query using the assistant and display the result
                response = hn_assistant.run(query, stream=False)  # Execute query without streaming
                st.write(response)  # Display the assistant's response to the user
            except Exception as e:
                # Handle errors during query execution
                st.error(f"An error occurred while processing the query: {e}")
    except Exception as e:
        # Handle errors related to the Assistant or API initialization
        error_container.error(f"Failed to initialize the assistant: {e}")
else:
    # Display a message prompting the user to enter the API key
    st.warning("Please enter your OpenAI API Key to continue.")
