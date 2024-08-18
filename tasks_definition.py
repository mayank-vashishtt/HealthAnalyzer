from crewai import Task
# from tools_setup import OpenAIWrapper
from agents_setup import health_metrics_interpreter, medical_content_explorer, personalized_health_consultant
from PyPDF2 import PdfReader

# Read the blood test report from the PDF
pdf_path = './blood_report.pdf'
raw_text = ""

with open(pdf_path, 'rb') as file:
    reader = PdfReader(file)
    for page in reader.pages:
        raw_text += page.extract_text()

# Task for analyzing blood test report
analyze_blood_test_task = Task(
    description=f'''
    You are tasked with interpreting the following blood test report:
    "{raw_text}"

    Guidelines:
    1. Identify and list all the tests performed, along with their results and reference ranges.
    2. Analyze the results by comparing them with the reference ranges:
        - If a result falls within the reference range, confirm it as normal.
        - If a result deviates from the reference range, mark it as abnormal and explain the potential health implications.
    3. Provide a clear, concise summary of the overall health picture, with emphasis on any significant abnormalities.
    4. Suggest any immediate actions or further tests that may be required to better understand the patient's condition.

    Your analysis should be both technically accurate and easy to understand for someone without medical training.
    ''',
    expected_output='A detailed interpretation of the blood test results, highlighting any abnormalities and explaining their potential health impact.',
    agent=health_metrics_interpreter
)

# Task for finding relevant articles
find_articles_task = Task(
    description='''Following the analysis of the blood test report, perform the following tasks:
    1. Identify key health concerns or issues highlighted by the abnormal values in the blood test report.
    2. Search the web for 3-5 recent, high-quality medical articles that are directly related to each identified health concern.
    3. For each selected article, provide:
        - The full title and author(s) of the article.
        - A concise summary (2-3 sentences) of the main findings or recommendations.
        - A clear explanation of how the article's findings relate to the blood test results.
    ''',
    expected_output='A list of articles with summaries and explanations of their relevance to the health concerns.',
    agent=medical_content_explorer
)

# Task for providing recommendations based on the analysis and articles
provide_recommendations_task = Task(
    description='''Based on the detailed analysis of the blood test report and the relevant articles, provide comprehensive health recommendations:
    1. Summarize the key findings from the blood test report and articles.
    2. Identify the main health concerns highlighted by the test results and articles.
    3. Recommend any additional tests or follow-ups that may be necessary for further evaluation.
    4. Offer actionable lifestyle advice aimed at improving overall health, considering the specific findings of the blood test.
    5. Include links to the referenced articles or additional trusted resources for further reading.
    ''',
    expected_output='A set of prioritized health recommendations, including a summary of the blood test findings, additional test suggestions, lifestyle advice, and relevant resources.',
    agent=personalized_health_consultant
)
