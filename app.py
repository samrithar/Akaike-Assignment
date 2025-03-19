import gradio as gr
import requests

def fetch_summary(company):
    response = requests.get(f"http://127.0.0.1:5000/fetch-news?company={company}")
    data = response.json()
    
    return data["articles"], data["comparative_analysis"], data["audio"]

ui = gr.Interface(
    fn=fetch_summary,
    inputs=gr.Textbox(label="Enter Company Name"),
    outputs=[gr.Textbox(label="Articles"), gr.Textbox(label="Comparative Analysis"), gr.Audio(label="Hindi TTS Output")]
)

ui.launch()

