# Import necessary libraries
from langchain.document_loaders import PyPDFLoader
from langchain.llms import Ollama
from langchain.chains import load_summarize_chain

# Define the PDF summarization function
def summarize_pdf(pdf_file_path, custom_prompt=""):
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    llm = Ollama(model="llama3")  # Replace "your_ollama_model" with your actual model name
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke(docs)
    return summary

# Define the main function to set up Gradio interface
def main():
    pdf_path = "/Users/gr/Desktop/Elsa/CC 2640R2.pdf"
    print(summarize_pdf(pdf_path)['output_text'])


# Run the main function to launch the application
if __name__ == "__main__":
    main()
