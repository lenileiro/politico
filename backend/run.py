"""Main application run file"""
import os

from app import create_app
config_name = os.getenv("FLASK_ENV", 'development')
runport = int(os.environ.get("PORT", 8050))

app = create_app(config_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=runport)
