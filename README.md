# Junior Python Developer Test Task

## Setup

1. Clone the repo.
   ```
   git clone https://github.com/Temskyi/FastAPI-Text-Summarizer.git
   cd FastAPI-Text-Summarizer
   ```

2. Create a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Test the endpoint:
   - Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized.