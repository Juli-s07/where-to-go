## How to run the project

1. Clone the project and open it

   ```bash
   git clone <repository-url> 
   cd where-to-go
   ```

2. Create and activate a virtual environment 

   (Linux/macOS):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   (Windows):
   ```bash
   python -m venv .venv 
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Apply migrations to create the local SQLite database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Endpoints
With the server running at `http://127.0.0.1:8000`:

| URL                                | Behavior                                |
|------------------------------------|-----------------------------------------|
| http://127.0.0.1:8000/             | Home page. Generate a random place.     |
| http://127.0.0.1:8000/places/      | List of all places.                     |
| http://127.0.0.1:8000/add/         | Add a new place.                        |
| http://127.0.0.1:8000/place/{id}/  | See the full descriptionn of the place. |

## Use of AI

Chat GPT and Claude were used to fully generate the .css file, partly .html structure, descriptions for places and the place_image.png image.
These tools also helped to understand the structure of the website and how its parts work together. (e.g. how and where to generate a random place when the button is pressed)
