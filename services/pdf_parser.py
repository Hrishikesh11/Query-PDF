import fitz  # PyMuPDF for PDF processing
from langchain.text_splitter import RecursiveCharacterTextSplitter
from services.chroma_client import ChromaClient

class PDFParser:
    def __init__(self):
        self.chroma_client = ChromaClient()
    def extractandstoretext(self, file: str) -> str:
        """Extracts and returns the text content of a PDF."""
        try:

            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            full_text = ""  # String to hold the concatenated text from all pages
            
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)  # Load each page
                full_text += page.get_text() + "\n"  # Append text from the page with a newline
            
            pdf_document.close()
             # Pre-process document and index chunks
            chunks = self._chunk_document(full_text)
            self.chroma_client.store_chunks(chunks, metadata=[{"source": "pdf"}] * len(chunks))
            return True
        except Exception as e:
            raise RuntimeError(f"Error processing PDF: {e}")
    def _chunk_document(self, document: str, chunk_size=1000, chunk_overlap=200):
        """Splits the document into smaller chunks using RecursiveCharacterTextSplitter."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        chunks = text_splitter.split_text(document)
        return chunks
