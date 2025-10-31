"""
Retrival-Augmented Generation (RAG) with the Google Vertex AI Vector Search

__author__ = "vci"
__copyright__ = "Copyright 2025, vci"
__license__ = "MIT"
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "modernui.app@gmail.com"
__status__ = "development"
__reference__ = "vci"

"""

from vertexai.language_models import TextEmbeddingModel, TextGenerationModel, ChatModel
from vertexai.generative_models import GenerativeModel
# from vertexai.preview.vector_search import VectorSearchIndex, VectorSearchEndpoint
from google.cloud import aiplatform #, aiplatform_v1
import fitz
import json


class VertexAiVectorSearch:
    """
    A class to handle Retrieval-Augmented Generation (RAG) through vector search using Google Vertex AI RAG pipelines.
    """

    def __init__(self, project_name: str, location: str, api_key_file: str) -> None:
        self.api_key = api_key_file
        self.aiplatform = aiplatform
        self.aiplatform.init(project=project_name,location=location, api_key=self.api_key)

    def extract_text_from_pdf(self, pdf_path: str, max_page: int = 3):
        """
        Extract text from a PDF file using PyMuPDF (fitz)
        """
        lines = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                if len(page.get_text()) == 0:
                    continue
                lines.extend(page.get_text().splitlines())
        return lines

    def embed_texts(self, texts: list) -> list:
        """
        Embed texts using Vertex AI Embedding Model
        """
        embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
        embeddings = [embedding_model.get_embeddings([text])[0].values for text in texts]
        return embeddings
    
    def create_vector_search(self, embeddings: list, ids: list, index_id: str, endpoint_id: str, deployed_index_id: str, export_file: str):
        """
        Upload embeddings to Vertex AI Vector Search
        """
        # gen datapoints
        datapoints = [ {"datapoint_id": id, "feature_vector": embedding} for id, embedding in zip(ids, embeddings) ]
        # export to file
        with open(export_file, "w") as f:
            for dp in datapoints:
                f.write(json.dumps(dp) + "\n")
        # create index
        index = self.aiplatform.MatchingEngineIndex.create_tree_ah_index(
            display_name=index_id,
            dimensions=768,
            approximate_neighbors_count=10,
            index_update_method="STREAM_UPDATE",
            description="Vector search index for RAG"
        )
        # create endpoint
        index_endpoint = self.aiplatform.MatchingEngineIndexEndpoint.create(
            display_name=endpoint_id,
            public_endpoint_enabled=True,
            description="Vector search endpoint for RAG"
        )
        # deploy index to endpoint
        index_endpoint.deploy_index(
            index=index,
            deployed_index_id=deployed_index_id
        )
        # upsert datapoints
        index.upsert_datapoints( datapoints=datapoints )
        return index
    
    def upload_datapoints(self, embeddings: list, ids: list, texts: list, index_id: str):
        """
        Upload embeddings to Vertex AI Vector Search
        """
        index = self.aiplatform.MatchingEngineIndex(index_name=index_id)
        datapoints = [ {"datapoint_id": text, "feature_vector": embedding} for text, embedding in zip(texts, embeddings) ]
        # datapoints = [ {"datapoint_id": id, "feature_vector": embedding, "crowding_tag": CrowdingTag(crowding_attribute="raw", value=f"{id} {text}")} for id, embedding, text in zip(ids, embeddings, texts)]
        # datapoints = [ {"datapoint_id": id, "feature_vector": embedding} for id, embedding in zip(ids, embeddings) ]
        index.upsert_datapoints( datapoints=datapoints )
        return index

    def retrieve_similar_texts(self, query: str, endpoint_id: str, deployed_index_id: str, top_k: int = 3) -> list:
        """
        Retrieve similar texts using Vertex AI Vector Search
        """
        retrieved_texts = []
        embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-005")
        query_embedding = embedding_model.get_embeddings([query])[0].values
      
        endpoint = self.aiplatform.MatchingEngineIndexEndpoint(endpoint_id)
        response = endpoint.find_neighbors(queries=[query_embedding], deployed_index_id=deployed_index_id, num_neighbors=top_k)
        # get retrieved texts
        for neighbor in response[0]:
            raw_text = neighbor.id
            retrieved_texts.append(raw_text)

        print(f"retrieved_texts: {retrieved_texts}")
        return retrieved_texts

    def generate_response(self, query: str, retrieved_texts: list, model: str = "gemini-2.5-flash") -> str:
        """
        Generate response using Vertex AI Language Model
        """ 
        context = "\n".join([text for text in retrieved_texts])
        full_prompt = f"""
                        You are an expert assistant. Answer the question **only using the context provided below**.
                        If the answer is not in the context, say "I don't know based on the provided information."

                        Context:
                        {context}

                        Question:
                        {query}

                        Answer:
                        """
        chat_model = GenerativeModel(model)
        chat = chat_model.start_chat()
        response = chat.send_message(full_prompt)
        return response.text
