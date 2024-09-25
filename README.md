

# AI Researcher

The **AI Researcher** is a Streamlit application designed to help you explore top stories and users on HackerNews. Leveraging a team of specialized AI assistants powered by GPT-4, this app allows you to generate insightful content based on your research queries.

# Its a play area for me to try out multi-agents

## Features

- **Comprehensive Research**: Investigate top stories and users on HackerNews effortlessly.
- **AI-Driven Assistance**: Utilize a team of AI assistants, each focused on specific research tasks.
- **Content Generation**: Create blog posts, reports, and social media content from your research findings.

## Getting Started

### 1. Clone the Repository

To get started, clone the GitHub repository:

```bash
git clone https://github.com/happyahluwalia/multiagent.git
```

### 2. Install Dependencies

Navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Obtain Your OpenAI API Key

- Sign up for an OpenAI account (or another LLM provider of your choice) to obtain your API key.

### 4. Run the Streamlit App

Launch the application with the following command:

```bash
streamlit run agent.py
```

### 5. Deployment
I will focus on deploying using Kamal or another method on my DigitalOcean server. My goal is to find an 'automatic' deployment provider that only requires access to a specific repository rather than full access to my entire GitHub account. (I really appreciate DigitalOcean for their commitment to doing things right! :-))

## How It Works

1. **API Key Input**: When you run the app, you will be prompted to enter your OpenAI API key. This key authenticates your access to the OpenAI language models.

2. **Assistant Instances Creation**:
    - **`story_researcher`**: Specializes in researching HackerNews stories.
    - **`user_researcher`**: Focuses on researching HackerNews users and reading articles from URLs.
    - **`hn_assistant`**: Serves as a team assistant coordinating the research efforts of both the story and user researchers.

3. **Research Query**: Input your research query in the provided text field. This could be a topic, keyword, or specific question related to HackerNews stories or users.

4. **Research Coordination**: The `hn_assistant` orchestrates the research process, delegating tasks to the `story_researcher` and `user_researcher` based on your query.

5. **Information Gathering**: The AI assistants gather relevant information from HackerNews using their respective tools.

6. **Content Generation**: The gathered information is processed using the GPT-4 language model to create a comprehensive response.

7. **Review Generated Content**: The generated content, which may include a blog post, report, or social media post, will be displayed in the app for you to review and utilize.
