# Code Snippets API

Example on how to serialize and deserialize data using Django REST Framework.

## Quick Start (MacOS)

1. Setup Python environment:
```

# Install pyenv
brew install pyenv

# Install and set Python version
pyenv install 3.8.10
pyenv local 3.8.10

# Create and activate virtual environment
python -m venv env
source env/bin/activate
```

2. Install and run:
```

# Install dependencies
pip install -r requirements.txt

# Setup database and run server
python manage.py migrate
python manage.py runserver
```

3. Use the API:
- Open http://localhost:8000/snippets/ in your browser
- Or use curl: `curl http://localhost:8000/snippets/` # serializer-and-deserializer
