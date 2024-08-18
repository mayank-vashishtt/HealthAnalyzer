from crewai import Agent
# from tools_setup import OpenAIWrapper
from dotenv import load_dotenv
from tools_setup import get_language_model

# Initialize the OpenAIWrapper
# openai_wrapper = OpenAIWrapper()
load_dotenv()
llm = get_language_model()

# Define agents with new roles and goals using OpenAI
health_metrics_interpreter = Agent(
    role='Health Metrics Interpreter',
    goal='Thoroughly interpret the blood test results and generate a patient-friendly summary that highlights key health indicators.',
    backstory='A data-driven medical analyst with a deep understanding of health metrics and a talent for making complex data accessible to all.',
    verbose=True,
    allow_delegation=False,
    # llm=openai_wrapper
    llm=llm
)

medical_content_explorer = Agent(
    role='Medical Content Explorer',
    goal='Search for and extract high-quality, evidence-based medical articles that align with the blood test analysis.',
    backstory='A medical librarian with extensive experience in curating reliable and relevant health information from diverse sources.',
    verbose=True,
    allow_delegation=False,
    # llm=openai_wrapper
    llm=llm
)

personalized_health_consultant = Agent(
    role='Personalized Health Consultant',
    goal='Synthesize health metrics and research findings to offer tailored health advice that considers both medical data and lifestyle factors.',
    backstory='A holistic health consultant with a strong background in preventative care and personalized wellness strategies.',
    verbose=True,
    allow_delegation=False,
    llm=llm
    # llm=openai_wrapper
)