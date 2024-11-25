import streamlit as st
from services.pdf_parser import PDFParser
from services.qa_agent import QAAgent
qa_agent = QAAgent()
# Utility Functions
def validate_file_upload(pdf_docs):
    """Validate uploaded PDF files."""
    if not pdf_docs:
        raise ValueError("No files uploaded. Please upload at least one PDF to proceed.")

def process_pdfs(pdf_docs):
    """Placeholder for processing uploaded PDFs."""
    try:
        text = ""
        pdf_parser = PDFParser()
        for pdf in pdf_docs:
            document_text = pdf_parser.extractandstoretext(pdf)
        st.session_state.files_uploaded = True
        return "PDFs processed successfully!"
    except Exception as e:
        raise RuntimeError(f"Error processing PDFs: {str(e)}")

def generate_ai_response(user_questions):
    """Generate AI responses (replace with actual LLM logic)."""
    try:
        # Replace with actual LLM API logic
        # responses = [f"Simulated response for: '{question.strip()}'" for question in user_questions if question.strip()]
        results = qa_agent.answer_questions(user_questions)
        return results
    except Exception as e:
        raise RuntimeError(f"Error generating response: {str(e)}")

# Streamlit App Functions
def handle_pdf_upload():
    """Handle the PDF upload process."""
    pdf_docs = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)
    if st.button("📤 Submit & Process"):
        try:
            validate_file_upload(pdf_docs)
            with st.spinner("Processing PDFs..."):
                success_message = process_pdfs(pdf_docs)
                st.success(success_message)
        except ValueError as ve:
            st.warning(str(ve))
        except RuntimeError as re:
            st.error(str(re))

def handle_bulk_questions():
    """Handle bulk question input and generate responses."""
    if not st.session_state.get("files_uploaded", False):
        st.error("Please upload and process PDF files to start querying.")
        return

    st.subheader("📋 Ask Questions in Bulk")
    questions = st.text_area(
        "Enter your questions (one per line):",
        placeholder="Type multiple questions, each on a new line.",
        help="You can enter multiple questions, one per line. Responses will be generated for each question.",
        key="bulk_questions",
    )

    if st.button("🚀 Submit Questions"):
        if questions.strip():
            user_questions = questions.split("\n")
            try:
                with st.spinner("Generating responses..."):
                    responses = generate_ai_response(user_questions)
                st.markdown("### 💡 Responses:")
                for question in  responses:
                    response=responses[question]
                    if question.strip():
                        st.markdown(f"**Q:** {question.strip()}")
                        st.markdown(f"**A:** {response}")
                        st.markdown("---")
            except RuntimeError as re:
                st.error(f"Error: {str(re)}")
        else:
            st.warning("Please enter at least one question.")

def setup_session_state():
    """Initialize session state variables."""
    if "files_uploaded" not in st.session_state:
        st.session_state.files_uploaded = False

# Main Function
def main():
    """Main application logic."""
    st.set_page_config(page_title="Bulk Questions on PDFs", layout="wide")

    setup_session_state()

    # App Header
    st.markdown(
        """
        <style>
        .main-header {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="main-header">Ask Multiple Questions on Your PDFs</div>', unsafe_allow_html=True)

    # Sidebar for PDF Upload
    with st.sidebar:
        st.title("📂 Upload PDFs")
        st.markdown(
            "Upload one or more PDF files and process them to enable bulk querying."
        )
        handle_pdf_upload()

    # Main Question Input and Response Section
    st.markdown(
        """
        <style>
        .bulk-question-container {
            padding: 15px;
            background-color: #F8F9FA;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="bulk-question-container">', unsafe_allow_html=True)
    handle_bulk_questions()
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 0.9em;'>Powered by OpenAI LLM & Streamlit</div>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
