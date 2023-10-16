# BespokeCV
Discover "Bespoke CV": your tool for tailored job applications. Match your CV to job descriptions, generate cover letters, get ATS scores, and prep with top 10 interview questions plus tailored answers. Analyze CV strengths and weaknesses against job roles and receive recommendations to enhance your application.

## Features

- Job Description Summarization: Summarizes job descriptions into job nature, responsibilities, and requirements.
- CV Rating: Rates the compatibility of the CV with the job description, providing strengths, weaknesses, and recommendations to strengthen the CV.

## Setup and Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:

```bash
pip install gradio openai
```

Create a file named config.py in the project directory with the following content, replacing your_openai_api_key_here with your actual OpenAI API key:
```python
OPENAI_API_KEY = "your_openai_api_key_here"
```
##Usage

Run the application by executing the following command in the project directory:
```bash
python app.py
```
# Assuming your script is saved as app.py
The Gradio interface will launch in your web browser. You can also access the interface at http://127.0.0.1:7860/.
In the "Job Description Summarizer" tab, paste a job description into the text box and click "Submit" to get a summarized version of the job description.
In the "CV ATS Rating" tab, paste the CV data into the text box and click "Submit" to get a rating and feedback based on the job description summary.
Customization

You can customize the behavior of the application by modifying the process_jd and cv_rating functions in the script.

##License

This project is open source and available under the MIT License.

