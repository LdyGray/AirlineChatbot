import streamlit as st
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI

st.title("Airline Feedback")

prompt = st.text_input("Share with us your experience of your latest trip.", "My last trip was")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# Function to determine the response based on user feedback
def analyze_feedback(feedback):
    # Prompt to analyze feedback
    prompt = f"""
    Analyze the following user feedback and classify it:
    - Identify if the experience was positive or negative.
    - If negative, determine the cause of dissatisfaction.
    - Possible causes include: 
      1. Airline's fault (e.g., lost luggage).
      2. Beyond airline's control (e.g., weather-related delays).
    
    Feedback: "{feedback}"
    """

    # Create a chain with the prompt
    chain = LLMChain(llm=llm, prompt=PromptTemplate(template=prompt))
    response = chain.run()
    return response

# Button to process feedback
if st.button("Submit Feedback"):
    if user_input:
        result = analyze_feedback(user_input)
        
        # Determine the response based on analysis
        if "positive" in result.lower():
            st.success("Thank you for your feedback and for choosing to fly with us!")
        elif "airline's fault" in result.lower():
            st.warning("We're sorry to hear about your experience. Our customer service will contact you soon to resolve the issue or provide compensation.")
        elif "beyond airline's control" in result.lower():
            st.info("We understand your frustration, but please note that the airline is not liable in situations beyond our control.")
        else:
            st.error("Could not determine the nature of your feedback. Please try again.")
    else:
        st.warning("Please enter your feedback before submitting.")
