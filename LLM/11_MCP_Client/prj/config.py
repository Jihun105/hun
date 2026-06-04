'''설정 관리'''
import os
from dotenv import load_dotenv
load_dotenv(override=True)

class Config:
    '''시스템 설정'''
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL')
    LLM_MODEL = os.getenv('LLM_MODEL')
    LLM_TEMPERATURE = os.getenv('LLM_TEMPERATURE')
    RETRIEVE_TOP_K = int(os.getenv('RETRIEVE_TOP_K'))
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE'))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP'))
    DOCUMENT_PATH = os.getenv('DOCUMENT_PATH', './data/internal_docs')
    CHROMA_PERSIST_DIRECTORY = os.getenv('CHROMA_PERSIST_DIRECTORY')
    CHROMA_COLLECTION_NAME = os.getenv('CHROMA_COLLECTION_NAME')

    @classmethod
    def validate(cls):
        '''필수 설정검증'''
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required")
        if not os.path.exists(cls.DOCUMENT_PATH):
            os.makedirs(cls.DOCUMENT_PATH, exist_ok=True)
            print(f"Created document path: {cls.DOCUMENT_PATH}")

config = Config()
    
    