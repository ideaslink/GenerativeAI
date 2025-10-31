"""
Retrival-Augmented Generation (RAG) with the Google Vertex AI Cloud

__author__ = "vci"
__copyright__ = "Copyright 2025, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

"""

from vertexai.language_models import TextEmbeddingModel, ChatModel
# from vertaxai.preview.vector_search import VectorSearchIndex, VectorSearchEndpoint
from google.cloud import aiplatform, aiplatform_v1
import fitz


class VertexAiRAG:
    """
    A class to handle Retrieval-Augmented Generation (RAG) using Google Vertex AI RAG pipelines.
    """

    def __init__(self, project_name: str, location: str, api_key_file: str) -> None:
        # self.api_key = api_key
        
        self.aiplatform = aiplatform
        self.aiplatform.init(project=project_name,location=location, api_key=api_key_file)

    def extract_text_from_pdf(self, pdf_path: str, max_page: int = 3):
        """
        Extract text from a PDF file using PyMuPDF (fitz)
        """
        with fitz.open(pdf_path) as doc:
            texts = [doc[i].get_text() for i in range(min(len(doc), max_page))]
        return texts
    
    def embed_texts(self, texts: list):
        """
        Embed texts using Vertex AI Embedding Model
        """
        embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
        # embedding_model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001") #  ("text-embedding-005") # 
        embeddings = [embedding_model.get_embeddings([text])[0].values for text in texts]
        return embeddings
    
    def uploadto_vector_search(self, embeddings: list, ids: list, index_id: str):
        """
        Upload embeddings to Vertex AI Vector Search
        """
        index = self.aiplatform.MatchingEngineIndex(index_id)
        index.upsert_datapoints( datapoints=[{"datapoint_id": id, "feature_vector": embedding} for id, embedding in zip(ids, embeddings)] )
        # index.upsert( items=[{"id": id, "embeddings": embedding} for id, embedding in zip(ids, embeddings)] )
        return index
    
    def retrieve_similar_texts(self, query: str, endpoint_id: str, deployed_index_id: str, top_k: int = 3) -> list:
        """
        Retrieve similar texts using Vertex AI Vector Search
        """
        query_embedding = self.embed_texts([query])[0]
        print(f"query_embedding: {query_embedding}")
        endpoint = self.aiplatform.MatchingEngineIndexEndpoint(endpoint_id)
        # test: to make query_embedding iterable
        query_embedding = [query_embedding]
        response = endpoint.find_neighbors(queries=query_embedding, deployed_index_id=deployed_index_id)
        print(f"vector search response: {response}")
        return ([doc["neighbor"]["id"] for doc in response]) # #response

    def generate_response(self, query: str, retrieved_texts: list, model: str = "gemini-2.5-flash") -> str:
        """
        Generate response using Vertex AI Language Model
        """ 
        context = "\n".join([text for text in retrieved_texts])
        full_prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
        chat_model = ChatModel.from_pretrained(model)
        chat = chat_model.start_chat()
        response = chat.send_message(full_prompt)
        return response.text
