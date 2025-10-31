"""
unit tests for generative ai

__author__ = "vci"
__copyright__ = "Copyright 2025, vci
__license++ = "MIT
__version__ = "1.0.0.10"
__maintainer__ = "vci"
__email__ = "contact@hsharp.com"
__status__ = "development"
__reference__ = "vci"

"""

import unittest
import os
import sys
# Adjust the path to include the src directory to avoid import headache
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
from google_ai.generative_ai import GenerativeAI
from google_ai.vertexai_rag import VertexAiRAG
from google_ai.vertexai_vector_search import VertexAiVectorSearch
from shared.vars import GCP_VARS

class TestGenerativeAI(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skip("Skipping test that requires actual API call")
    def test_generative_ai(self):
        """
        test google generative ai - content generation
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        response = generative_ai.generate_text(prompt="what can you infer from ‘Shakespeare in AI’? (max: 300 words).", model="gemini-2.5-flash")

        print(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    @unittest.skip("Skipping test that requires actual API call")
    def test_generative_image(self):
        """
        test google generative ai - image generation
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        output_path = "../_assets/ai_gcp_image.png"
        response = generative_ai.generate_image(output_path=output_path, prompt="generate an image: a logo for AI Frontiers.", model="gemini-2.5-flash-image-preview")

        # print(response)
        self.assertTrue(os.path.exists(output_path))

    @unittest.skip("Skipping test that requires actual API call")
    def test_generative_image_edit(self):
        """
        test google generative ai - image editing
        """
        
        # print("calling gemini api")
        generative_ai = GenerativeAI(api_key = os.getenv( GCP_VARS.get("API_KEY", "") ) )
        input_path = "../_assets/ai_gcp_image_original.png" # 
        output_path = "../_assets/ai_gcp_image_edited.png"
        response = generative_ai.generate_image_edit(input_path=input_path, output_path=output_path, prompt="Add a tie to the cat and place it beside a swimming  pool lined with palm trees.", model="gemini-2.5-flash-image-preview")

        print(response)
        self.assertTrue(os.path.exists(output_path))

    @unittest.skip("Skipping test for vertex ai rag")
    def test_vertexai_rag(self):
        """
        test google vertex ai rag
        """
        apikeyfile = os.getenv( GCP_VARS.get("API_KEY_FILE", "") )
        vertexai_rag = VertexAiRAG(project_name="gcpapis-468721", location="us-central1", api_key_file=apikeyfile)
        pdf_path = "../_assets/Oscar 2025 winners.pdf"
        query = "Who is the Best Actor winner?"
        texts = vertexai_rag.extract_text_from_pdf(pdf_path=pdf_path, max_page=3)
        print(f"extracted texts: {texts}")
        ids = [f"page_{i}" for i in range(len(texts))]
        embeddings = vertexai_rag.embed_texts(texts=texts)
        print(f"embeddings: {embeddings}")
        index = vertexai_rag.uploadto_vector_search(embeddings=embeddings, ids=ids, index_id="7517081723151056896")
        retrieved_texts = vertexai_rag.retrieve_similar_texts(query=query, endpoint_id="projects/459024198485/locations/us-central1/indexEndpoints/2061577705010233344", deployed_index_id="gcp_sharp_deploy_stream_1761254986818", top_k=3)
        print(f"retrieved_texts: {retrieved_texts}")
        response = vertexai_rag.generate_response(query=query, retrieved_texts=retrieved_texts, model="gemini-2.5-flash")
        print(f"response: {response}")

        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


    @unittest.skip("Skipping test for vertex ai rag")
    def test_vertexai_rag_vs(self):
        """
        test google vertex ai rag
        """
        self.UID = "001"  # unique value for index/endpoint etc.
        self.index_id = f"gcp_sharp_index_{self.UID}"
        self.endpoint_id = f"gcp_sharp_endpoint_{self.UID}"
        self.deployed_index_id = f"gcp_sharp_deploy_{self.UID}"
        apikeyfile = os.getenv( GCP_VARS.get("VERTEXAI_KEY_FILE", "") )
        vertexai_rag = VertexAiVectorSearch(project_name="gcpapis-468721", location="us-central1", api_key_file=apikeyfile)
        pdf_path = "../_assets/Oscar 2025 winners.pdf"
        query = "Who is the Best Actor winner?"
        texts = vertexai_rag.extract_text_from_pdf(pdf_path=pdf_path, max_page=3)
        ids = [f"{i}" for i in range(len(texts))]
        embeddings = vertexai_rag.embed_texts(texts=texts)
        index = vertexai_rag.create_vector_search(embeddings=embeddings, ids=ids, index_id=self.index_id, endpoint_id=self.endpoint_id, deployed_index_id=self.deployed_index_id, export_file="../_assets/vector_datapoints.jsonl")    
        retrieved_texts = vertexai_rag.retrieve_similar_texts(query=query, endpoint_id=self.endpoint_id, deployed_index_id=self.deployed_index_id, top_k=3)
        print(f"retrieved_texts: {retrieved_texts}")
        response = vertexai_rag.generate_response(query=query, retrieved_texts=retrieved_texts, model="gemini-2.5-flash")
        print(f"response: {response}")

        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    @unittest.skip("Skipping test for upserting datapoints")
    def test_vertexai_rag_upsert(self):
        """
        test google vertex ai rag - upsert datapoints
        """
        self.UID = "001"  # unique value for index/endpoint etc.
        self.index_id = "9069979169663746048" # input your index id (note: it's not sensitive)
        self.endpoint_id = "3110634943210848256" # input your endpoint id (note: it's not sensitive)
        self.deployed_index_id = f"gcp_sharp_deploy_{self.UID}"
        project_id = "459024198485" # input your project id (note: it's not sensitive)
        project_name="gcpapis-468721"
        location="us-central1"
        apikeyfile = os.getenv( GCP_VARS.get("VERTEXAI_KEY_FILE", "") )
        vertexai_rag = VertexAiVectorSearch(project_name=project_name, location=location, api_key_file=apikeyfile)
        pdf_path = "../_assets/Oscar 2025 winners.pdf"
        query = "Who is the Best Actor winner?"
        # retrieve contents
        texts = vertexai_rag.extract_text_from_pdf(pdf_path=pdf_path, max_page=3)
        ids = [f"{i}" for i in range(len(texts))]
        # embed texts
        embeddings = vertexai_rag.embed_texts(texts=texts)
        # upsert datapoints
        index = vertexai_rag.upload_datapoints(embeddings=embeddings, ids=ids, texts=texts, index_id=f"projects/{project_id}/locations/{location}/indexes/{self.index_id}")
        # retrieve similar texts
        retrieved_texts = vertexai_rag.retrieve_similar_texts(query=query, endpoint_id=f"projects/{project_id}/locations/{location}/indexEndpoints/{self.endpoint_id}", deployed_index_id=self.deployed_index_id, top_k=3)
        print(f"retrieved_texts: {retrieved_texts}")        
        # generate response by GenAi
        response = vertexai_rag.generate_response(query=query, retrieved_texts=retrieved_texts, model="gemini-2.5-flash")
        print(f"response: {response}")

        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    @unittest.skip("Skipping test for querying about oscar winners")
    def test_vertexai_rag_query_movie_winners(self):
        """
        test google vertex ai rag - query movie winners
        """
        self.UID = "001"  # unique value for index/endpoint etc.
        self.index_id = "9069979169663746048" # input your index id (note: it's not sensitive)
        self.endpoint_id = "3110634943210848256" # input your endpoint id (note: it's not sensitive)
        self.deployed_index_id = f"gcp_sharp_deploy_{self.UID}"
        project_id = "459024198485" # input your project id (note: it's not sensitive)
        project_name="gcpapis-468721"
        location="us-central1"
        apikeyfile = os.getenv( GCP_VARS.get("VERTEXAI_KEY_FILE", "") )
        vertexai_rag = VertexAiVectorSearch(project_name=project_name, location=location, api_key_file=apikeyfile)
        query = input("\nQuery about Oscar 2025 winners: ") # query = "Who is the Best Actor winner?"
        # retrieve similar texts
        retrieved_texts = vertexai_rag.retrieve_similar_texts(query=query, endpoint_id=f"projects/{project_id}/locations/{location}/indexEndpoints/{self.endpoint_id}", deployed_index_id=self.deployed_index_id, top_k=3)
        # generate response by GenAi
        response = vertexai_rag.generate_response(query=query, retrieved_texts=retrieved_texts, model="gemini-2.5-flash")
        print(f"response: {response}")

        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()