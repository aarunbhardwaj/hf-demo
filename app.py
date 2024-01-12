from transformers import pipeline
import gradio as gr


model= pipeline('summarization')



def predict():
    summary = model(prompt)[0]["summary_text"]
    return summary


with gr.Blocks() as demo:
    textbox = gr.textBox(placeholder="Enter text to summarize" , lines = 4)
    gr.Interface(fn=predict, inputs = textbox , outputs = text)

demo.launch()