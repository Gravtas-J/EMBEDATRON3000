import streamlit as st
import os
import re
import pypdf 
import pickle

from pypdf import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def main():
    load_dotenv()
    st.set_page_config(page_title="EMBEDATRON3000")
    st.header("Upload the file you wish to embed")

    # uploading
    pdf = st.file_uploader("upload here", type="pdf")

    # Check if it has stuff in it and extract it
    if pdf is not None:
        # Get the file name, replace non-alphanumeric characters with underscores
        file_name = re.sub(r'\W+', '_', pdf.name)
        # Remove the .pdf extension, if present
        file_name = re.sub(r'\.pdf$', '', file_name, flags=re.IGNORECASE)
        pickle_file_name = f'{file_name}.pkl'

        pdf_Reader = PdfReader(pdf)
        text = ""
        # loop through pages
        for page in pdf_Reader.pages:
            # concatinate is a funny word
            text += page.extract_text()

        # split into chunks 
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        # create a thing to hold the chunks in an array
        chunks = text_splitter.split_text(text)

        # Embedding the data
        embeddings = OpenAIEmbeddings()
        KB = FAISS.from_texts(chunks, embeddings)

        # New code to save embeddings...
        with open(pickle_file_name, 'wb') as f:
            pickle.dump(KB, f)

if __name__ == '__main__':
    main()
