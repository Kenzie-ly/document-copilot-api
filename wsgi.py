import os
from DocumentCopilot import DocumentCopilot
from api import app, init_api

# 1. Grab the API key securely from the server's environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") 

# 2. Initialize your class
documentCopilot = DocumentCopilot("gemini-2.5-flash", GEMINI_API_KEY)

# 3. Attach the model to your Flask routes
init_api(documentCopilot)

# Gunicorn will look at this file and grab the 'app' variable to run it!
if __name__ == "__main__":
    app.run()