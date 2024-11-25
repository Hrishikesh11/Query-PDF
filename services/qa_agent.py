from services.model_wrapper import ModelWrapper
from services.chroma_client import ChromaClient

class QAAgent:
    def __init__(self):
        self.model = ModelWrapper()
        self.chroma_client = ChromaClient()

    def answer_questions(self, questions: list):
        """Processes questions by querying Chroma and generating answers."""
        # # Pre-process document and index chunks
        # chunks = self._chunk_document(document)
        # chunk_embeddings = [self.embedding_service.compute_embedding(chunk) for chunk in chunks]
        # self.chroma_client.store_chunks(chunks, chunk_embeddings, metadata=[{"source": "pdf"}] * len(chunks))

        # Answer questions
        try:
            results = {}
            context=""
            for question in questions:
                # query_embedding = self.embedding_service.compute_embedding(question)
                # print("questionquestionquestion",question)
                similar_chunks = self.chroma_client.query_similar_chunks(question, top_k=3)
                # print("similar_chunkssimilar_chunkssimilar_chunks",similar_chunks)
                context =" ".join(similar_chunks[0]) 
                answer = self.model.query(question, context)
                results[question]=answer
        except Exception:
            results[question] = "Data Not Available"
        return results

    