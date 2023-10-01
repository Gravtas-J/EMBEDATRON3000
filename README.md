# EMBEDATRON3000

## Description

EMBEDATRON3000 is a Streamlit application that allows you to upload PDF files, processes the text within them, splits the text into manageable chunks, embeds those chunks using OpenAI's embeddings, and then stores these embeddings in a FAISS vector store. The generated vector store is then serialized and saved to disk for future use.

## Dependencies

- streamlit
- pypdf
- python-dotenv
- langchain
- faiss-cpu or faiss-gpu

Install the required libraries using pip:


pip install streamlit pypdf python-dotenv langchain faiss-cpu


Note: If you have a CUDA-compatible GPU, you might want to install `faiss-gpu` instead of `faiss-cpu` for better performance.

## Setup

1. Clone this repository.
2. Set up a `.env` file in the project root with necessary configurations (if any).
3. Navigate to the project directory in the terminal.
4. Run the following command to start the Streamlit app:


streamlit run app.py


Now, navigate to `http://localhost:8501` in your web browser to access the EMBEDATRON3000 interface. Upload a PDF file through the interface, and the app will process the text, generate embeddings, and save the vector store to a pickle file on your machine.

## Usage

1. Upon launching, you'll be greeted with a page titled "EMBEDATRON3000" and a prompt to upload your PDF file.
2. Click on the "upload here" button to select and upload your PDF file.
3. The application will process the text within the PDF, split it into chunks, generate embeddings for each chunk using OpenAI's embeddings, and store these embeddings in a FAISS vector store.
4. The generated vector store will then be serialized and saved to a pickle file in the same directory with a name derived from the original PDF file name.

## Contributing

Feel free to fork the repository, create a new branch, and submit a Pull Request if you'd like to contribute to this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
