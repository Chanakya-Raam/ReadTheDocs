Installation
============

Follow these steps to set up the FastAPI project with Keycloak:

1. **Clone the Repository**

   Clone the project repository from GitHub:
   
   .. code-block:: bash
   
      git clone https://github.com/yourusername/yourproject.git
      cd yourproject

2. **Create a Virtual Environment**

   Set up a Python virtual environment:
   
   .. code-block:: bash
   
      python3 -m venv venv
      source venv/bin/activate

3. **Install Dependencies**

   Install the required dependencies listed in the `requirements.txt` file:
   
   .. code-block:: bash
   
      pip install -r requirements.txt

4. **Run the FastAPI App**

   Start the FastAPI application:
   
   .. code-block:: bash
   
      uvicorn app.main:app --reload

   By default, the application will run at `http://127.0.0.1:8000`.

5. **Keycloak Setup**

   You'll need a Keycloak server running. Follow the instructions from the official Keycloak documentation to set up a Keycloak instance: https://www.keycloak.org/documentation.
