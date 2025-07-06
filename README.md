# Agentic_AI_Workshop

## Intro
Welcome to the **Agentic_AI_Workshop** repository! This collection of mini projects is designed to introduce and explore the concepts of Agentic AI, where intelligent agents autonomously perform tasks and make decisions. The workshop aims to provide hands-on experience in building AI agents for various applications, such as task automation, decision-making, and interaction with environments. Each mini project demonstrates practical implementations of Agentic AI principles, offering insights into designing and deploying autonomous systems.

**Target Audience**: AI enthusiasts, developers, and beginners with a basic understanding of programming and AI concepts.  
**Prerequisites**: Familiarity with Python programming, basic knowledge of machine learning, and experience with Git for version control.

## Features
The repository includes several mini projects, each focusing on a specific aspect of Agentic AI:

- **Project 1: Task Automation Agent**  
  - Builds an AI agent that automates repetitive tasks, such as file organization or data processing.  
  - Demonstrates agent planning, environment interaction, and decision-making.  
  - Learning Outcome: Understand how to design agents that execute tasks autonomously.

- **Project 2: Conversational AI Agent**  
  - Implements a chatbot-like agent that responds to user inputs with context-aware decisions.  
  - Showcases natural language processing (NLP) and dialogue management.  
  - Learning Outcome: Learn to integrate NLP with agentic behavior for dynamic interactions.

- **Project 3: Game-Playing Agent**  
  - Creates an AI agent that plays a simple game (e.g., Tic-Tac-Toe) using reinforcement learning.  
  - Highlights decision-making under uncertainty and reward-based learning.  
  - Learning Outcome: Explore reinforcement learning techniques for agentic systems.

## Tech Stack
The mini projects utilize the following technologies:

- **Backend**:  
  - Python 3.8+  
  - Libraries: `numpy`, `pandas`, `scikit-learn`, `transformers` (Hugging Face), `gym` (for reinforcement learning)  
- **Frontend**:  
  - HTML, CSS, JavaScript (for interactive demos in Project 2)  
  - Flask (for serving web-based interfaces)  
- **Database**:  
  - SQLite (for storing conversation logs in Project 2)  
  - Chosen for its lightweight nature and ease of setup.

Each project may use a subset of these technologies. Refer to individual project READMEs for specific details.

## Project Structure
The repository is organized as follows:

```
Agentic_AI_Workshop/
├── project1_task_automation/
│   ├── README.md
│   ├── main.py
│   └── requirements.txt
├── project2_conversational_agent/
│   ├── README.md
│   ├── app.py
│   ├── templates/
│   └── requirements.txt
├── project3_game_playing/
│   ├── README.md
│   ├── game.py
│   └── requirements.txt
├── shared/
│   └── utils.py
├── LICENSE
└── README.md
```

- Each project has its own folder with a dedicated `README.md` for detailed instructions.  
- The `shared/` folder contains common utilities used across projects.  
- Individual `requirements.txt` files list project-specific dependencies.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)
- Optional: Virtualenv for isolated environments
- For Project 2: Node.js 14+ (for frontend development, if applicable)

### Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Sanjai-SNS/Agentic_AI_Workshop.git
   cd Agentic_AI_Workshop
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies for a specific project (e.g., for Project 1):
   ```bash
   cd project1_task_automation
   pip install -r requirements.txt
   ```

### Backend Setup
- For Project 1 and Project 3, run the main script:
  ```bash
  python main.py  # or game.py for Project 3
  ```
- For Project 2, start the Flask server:
  ```bash
  cd project2_conversational_agent
  python app.py
  ```

### Frontend Setup
- For Project 2 (if using the web interface):
  ```bash
  cd project2_conversational_agent
  npm install  # If frontend dependencies are required
  npm start
  ```
- Access the interface at `http://localhost:5000`.

## API Endpoints
For Project 2 (Conversational AI Agent), the following RESTful API endpoints are available:

- **GET /api/converse**  
  - Description: Retrieves the current conversation history.  
  - Example Request: `curl http://localhost:5000/api/converse`  
  - Example Response: `{"history": ["User: Hello", "Agent: Hi! How can I assist you?"]}`  

- **POST /api/converse**  
  - Description: Sends a user message to the conversational agent and returns its response.  
  - Example Request: `curl -X POST -H "Content-Type: application/json" -d '{"message": "Tell me about Agentic AI"}' http://localhost:5000/api/converse`  
  - Example Response: `{"response": "Agentic AI involves autonomous systems that..."}`

Refer to `project2_conversational_agent/README.md` for additional endpoints and details.

## Usage
Each mini project can be run independently:

- **Project 1: Task Automation Agent**  
  Run `python main.py` to execute the automation script. Example: Automate sorting files in a directory based on file type.  
  ```bash
  python main.py --input-dir ./data --output-dir ./sorted
  ```

- **Project 2: Conversational AI Agent**  
  Start the Flask server (`python app.py`) and access the web interface at `http://localhost:5000`. Alternatively, use the API to interact programmatically.  
  Example: Send a message via the API to get a response from the agent.

- **Project 3: Game-Playing Agent**  
  Run `python game.py` to start the game. The agent will play against itself or a human player.  
  Example: `python game.py --mode human` to play interactively.

## Development
To contribute to the repository:

1. Fork the repository and create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Follow the coding standards outlined in `CONTRIBUTING.md`.  
3. Run tests (if applicable):  
   ```bash
   pytest project1_task_automation/tests/
   ```
4. Submit a pull request with a clear description of your changes.

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support
For help or to report issues, please:  
- Open an issue on the [GitHub Issues page](https://github.com/Sanjai-SNS/Agentic_AI_Workshop/issues).  
- Contact the maintainer at sanjai.sns@example.com (replace with your actual email).