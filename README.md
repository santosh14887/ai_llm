# ai_llm
AI LLM (need to be project folder)
#create .env file and set key as we generated
GEMINI_API_KEY=******
# Create Python virtual environment
python -m venv venv
#Activate it
venv\Scripts\activate
#Install dependencies
pip install -r requirements.txt
#generate/update the file from your working environment with
pip freeze > requirements.txt
# Test database connection
python database.py
#Insert initial document
python insert_document.py
#Insert chunks
python insert_chunks.py
#Generate embeddings
python generate_embeddings.py
#Test reading chunks + embeddings
python search_chunks.py
#Test question embedding
python question_embedding.py
#Test cosine similarity
python similarity.py
#Run actual RAG retrieval
python rag_search.py
#Current RAG generation
#We also tested passing retrieved content to Gemini:
Question
   ↓
Embedding
   ↓
Similarity
   ↓
Relevant chunks
   ↓
Prompt
   ↓
Gemini
   ↓
Answer
#FastAPI
uvicorn fast_api:app --reload


