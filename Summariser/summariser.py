# Import necessary libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain.chains import load_summarize_chain

llm = Ollama(model="llama3")


# Define the PDF summarization function
def summarize_pdf(pdf_file_path):
    """This function uses LLM to summarise the PDF file. It uses load_summarise_chain to summarise the documents"""
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke(docs)
    return summary


def summarize_txt(file_path):
    """This function uses LLM to summarise the text. This function uses normal LLM capabilities and does not use
    load_summarize_chain for the same."""
    return llm.invoke("Summarise this text file: \n" + open(file_path).read())


def main(file_path=None):
    if file_path.endswith(".pdf"):  # If it is a .pdf file, summarise it
        print(summarize_pdf(file_path)['output_text'])
    elif file_path.endswith(".txt"):  # If it is a .txt file, summarise it
        print(summarize_txt(file_path))


# Run the main function to launch the application
if __name__ == "__main__":
    # Example on how to use it.
    main(file_path="/Users/gr/Desktop/Elsa/test.txt")
