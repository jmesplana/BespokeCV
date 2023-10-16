import gradio as gr
import config
import openai

# Set your OpenAI API key
openai.api_key = config.OPENAI_API_KEY

jd_summary_global = ""  # Global variable to store the job description summary

def process_jd(text):
    global jd_summary_global  # Declare the global variable
    if not text.strip():  # Check if the text is empty or contains only whitespace
        jd_summary_global = "No JD"  # Update the global variable
        return "No JD"
    
    try:
        # Structuring a prompt to ask GPT-3.5 to summarize the job description
        prompt = f"Summarize the following job description into its job nature, responsibilities, and requirements:\n\n{text}"
        
        # Uploading text to OpenAI 
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}])
        jd_summary = response['choices'][0]['message']['content'].strip()
        jd_summary_global = jd_summary  # Update the global variable
        return jd_summary
    except Exception as e:
        return str(e)

def cv_rating(cv_data):
    global jd_summary_global  # Declare the global variable
    if len(jd_summary_global) <= 1 or jd_summary_global == "No JD":  
        return "No JD in the previous tab."
    if len(cv_data) <= 1:
        return "No CV data"
    try:
        # Construct a prompt to ask GPT-3.5 to rate the CV based on the job description summary
        prompt = f"""
        Job Description Summary: {jd_summary_global}
        CV Data: {cv_data}
        
        Rate the compatibility of the CV with the job description and provide strengths, weaknesses, and recommendations to strengthen the CV.
        """
        # Uploading text to OpenAI 
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}])
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)
    
jd_sum = gr.Interface(
    fn=process_jd,  # function to process the text
    inputs=gr.Textbox(lines=30, label="Job Description"),
    outputs=gr.Textbox(lines=30, label="JD Summary", show_copy_button=True),
    live=False,
    title="Job Description Summarizer",
    description="An app to summarize job descriptions into job nature, responsibilities, and requirements.",
)

cv_rate_interface = gr.Interface(
    fn=cv_rating,
    inputs=gr.Textbox(lines=30, label="CV Data", placeholder="Paste the CV data here"),
    outputs=gr.Textbox(lines=30, label="ATS Rating System", show_copy_button=True),
    live=False,
    title="CV Rating",
    description="An app to rate CV compatibility with job description, providing strengths, weaknesses, and recommendations.",
)
bespokecv = gr.TabbedInterface([jd_sum, cv_rate_interface],tab_names=['Job Description Summarizer','CV ATS Rating'])

if __name__ == "__main__":
    bespokecv.launch(share=True)