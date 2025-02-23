# CodeNova
# test

## Overview
The AI-Powered Software Engineer is an advanced tool designed for developers, integrating IBM's Granite LLMs to enhance software development workflows. This project was built for the IBM x LabLab.ai Hackathon and provides business-valued solutions by automating various software engineering tasks.

## Features
The application includes six main tools:
1. **Code Generation** - Automatically generate code based on user input.
2. **Code Debugging** - Identify and fix issues in the provided code.
3. **Code Explainer** - Provide detailed explanations of code functionality.
4. **Code Refactoring** - Improve code structure and efficiency.
5. **Automated Documentation** - Generate structured documentation in TXT, DOCX, and PDF formats.
6. **Pair Programming** - Assist developers in real-time coding collaborations.

Additionally, it supports audio explanations (.mp3) to enhance accessibility and ease of use.

## Technologies Used
- **Python** (Flask for backend)
- **React** (Frontend UI)
- **IBM Granite LLMs** (AI model for software engineering tasks)
- **OpenAI Whisper** (for audio generation, if applicable)
- **Docker** (for containerized deployment)

## Installation and Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AI-Powered-Software-Engineer.git
   cd AI-Powered-Software-Engineer
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python app.py
   ```
   The app will be available at `http://localhost:5000`

## How to Use
1. Navigate through the sidebar to select a tool.
2. Input your code or query and click 'Generate'.
3. View, copy, or download the output.
4. Use the documentation generator for structured reports.

## Deployment (Docker)
1. Build the Docker image:
   ```sh
   docker build -t ai-powered-se .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 ai-powered-se
   ```

## .gitignore Configuration
To avoid committing unnecessary files, create a `.gitignore` file and add:
```
# Virtual environment
venv/

# Logs and cache
*.log
cache/

# Python bytecode
__pycache__/
*.pyc

# Environment variables
.env
```
This ensures sensitive and temporary files are not uploaded to GitHub.

## Business Value
- **Efficiency:** Reduces software development time with AI-powered assistance.
- **Accuracy:** Enhances code quality with debugging and refactoring tools.
- **Accessibility:** Provides multiple output formats, including audio explanations.
- **Scalability:** Easily deployable via Docker and cloud platforms.

## Future Enhancements
- Integration with IDE plugins.
- Support for additional programming languages.
- Advanced AI-driven pair programming.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit changes and push to GitHub.
4. Open a Pull Request.

## License
This project is licensed under the MIT License.

---

**Developed for IBM x LabLab.ai Hackathon**

