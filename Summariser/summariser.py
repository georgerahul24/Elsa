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


def summarize_txt(file_path, custom_prompt=""):
    llm = Ollama(model="llama3")  # Replace "your_ollama_model" with your actual model name
    return llm.invoke("Summarise this text file: \n" + open(file_path).read())


def main():
    file_path = "/Users/gr/Desktop/Elsa/test.txt"
    if file_path.endswith(".pdf"):
        print(summarize_pdf(file_path)['output_text'])
    elif file_path.endswith(".txt"):
        print(summarize_txt(file_path))


# Run the main function to launch the application
if __name__ == "__main__":
    main()
