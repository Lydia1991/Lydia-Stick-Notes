# 💜 Sticky Notes Task Manager

A stylish, Django-based productivity application designed to manage tasks as **3x3 inch sticky notes**. This project features a modern purple interface, a responsive horizontal grid, and full search functionality.

---

## 📊 System Architecture
The following flowchart illustrates the request-response cycle and how the application handles user interactions with the dashboard:

```mermaid
graph TD
    A[User Browser] -->|URL Request| B(Django URL Resolver)
    B -->|View Logic| C{NoteListView}
    C -->|Query DB| D[(SQLite Database)]
    D -->|Return Data| C
    C -->|Render HTML| E[3x3 Sticky Note Grid]


🏗️ Class Diagram
This diagram defines the data model structure used to store and categorize sticky notes:
mermaid
classDiagram
    class Note {
        +String title
        +String content
        +String color
        +Boolean is_completed
        +DateTime updated_at
        +__str__()
    }


✨ Key Features
3x3 Inch Grid: Notes are locked in a square format to prevent stretching, maintaining a consistent "Post-it" feel.
Full CRUD Support: Users can Create, Read (List & Detail), Update (Edit), and Delete notes.
Interactive Search: A floating search bar in the purple header allows for instant note filtering.
Custom Categorization: Choose from four distinct colors (Yellow, Pink, Green, Blue) to organize tasks.
Automated Testing: Includes 4 unit tests covering core model and view logic.
Clean Documentation: Fully compliant with PEP 8 and PEP 257 standards.
🚀 Implementation & Setup
To implement this project on your local machine, follow these steps:
Create a Virtual Environment:
bash
python -m venv venv

Activate the Environment:
Windows: .\venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install Dependencies:
bash
pip install -r requirements.txt

Initialize Database:
bash
python manage.py migrate

Run Automated Tests:
bash
python manage.py test

Start the Application:
bash
python manage.py runserver

Access the dashboard at http://127.0.0.1.
Tools & Libraries
•	Django web framework
•	Bootstrap
Author
•	Lydia 
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you.
