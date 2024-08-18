# Health Analyzer

This project is a **Medical Report Analysis** tool that extracts and analyzes health metrics from a blood report PDF, conducts web research on relevant health topics, and provides personalized health recommendations. The tool is implemented using the **Gemini API**, **Streamlit** for UI, and **Python**.

## Features

- **Health Metrics Extraction**: Extracts specific data points from a provided blood report PDF.
- **Condition Analysis**: Analyzes the extracted health data to identify potential health conditions.
- **Web Research**: Searches the web for relevant articles based on the analysis.
- **Personalized Recommendations**: Generates health recommendations and provides relevant resources.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mayank-vashishtt/HealthAnalyzer.git
    cd HealthAnalyzer
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory of the project and add the following:

    ```env
    GEMINI_API_KEY=your-gemini-api-key
    OPENAI_API_KEY=your-openai-api-key
    OPENAI_MODEL_NAME=gpt-4
    OPENAI_API_BASE=https://api.openai.com/v1
    ```

## Usage

1. **Run the application**:

    ```bash
    streamlit run start_analysis.py
    ```

2. **Upload a PDF file**:
    - You will be prompted to upload a PDF file containing the blood report.

3. **Analyze the Report**:
    - Click the "Analyze Report" button to begin the analysis. The tool will extract text from the PDF, analyze health metrics, perform web research, and provide health recommendations.

4. **View the Results**:
    - The results will be displayed in the Streamlit app and written to a `results.md` file.

## Project Structure

- `agents_setup.py`: Contains the setup for agents like health metrics interpreter, medical content explorer, and personalized health consultant.
- `tasks_definition.py`: Defines the tasks such as analyzing blood tests, finding articles, and providing recommendations.
- `tools_setup.py`: Setup for tools used by the agents, such as those required for web research.
- `start_analysis.py`: The main script that runs the analysis by creating a crew and executing tasks.
- `requirements.txt`: Lists all Python dependencies required by the project.
- `blood_report.pdf`: Example PDF file used for testing.
- `results.md`: The markdown file where analysis results are stored.

## Results

The results of the analysis will include:

- A summary of the extracted health metrics.
- An analysis of the health conditions.
- Relevant articles and resources found through web research.
- Personalized health recommendations.

## License

This project is licensed under the MIT License.
