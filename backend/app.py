from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

from src import create_app

app = create_app()
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
