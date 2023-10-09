# chatbot-share-service

**Description**  
Sends emails with product information using OpenAI language models.

**Dependencies**  
- Python 3.10
- OpenAI Python package
- LangChain
- AWS Lambda Python Runtime

**Installation**  
1. Install required Python packages.
2. Deploy to AWS Lambda.

**API**  
- Trigger via HTTP POST with JSON payload containing:
  - `email`
  - `productPanelContent`
