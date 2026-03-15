import os
from DocumentCopilot import DocumentCopilot
from api import app, init_api

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") 

documentCopilot = DocumentCopilot("gemini-2.5-flash", GEMINI_API_KEY)

init_api(documentCopilot)

if __name__ == "__main__":
    app.run()
