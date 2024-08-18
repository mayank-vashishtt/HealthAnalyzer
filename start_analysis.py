from agents_setup import health_metrics_interpreter, medical_content_explorer, personalized_health_consultant
from crewai import Crew
from tasks_definition import analyze_blood_test_task, find_articles_task, provide_recommendations_task

# Create a Crew and execute tasks
crew = Crew(
    agents=[health_metrics_interpreter, medical_content_explorer, personalized_health_consultant],
    tasks=[analyze_blood_test_task, find_articles_task, provide_recommendations_task],
    verbose=True
)

results = crew.kickoff()

# Convert results to a string
results_str = str(results)

# Define the file name
output_file = "results.md"

# Write the results to the file
with open(output_file, "w") as file:
    file.write("# Analysis Results\n\n")
    file.write(results_str)

print(f"Results have been written to {output_file}")