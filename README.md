# CodeNova


## Overview
**CodeNova** is an AI-powered code assistant designed to streamline software development by automating code generation, debugging, documentation, and code explanations. It integrates multiple AI models to provide a seamless and intelligent coding experience.integrating IBM's Granite LLMs to enhance software development workflows. This project was built for the **Generative AI Hackathon with IBM GRANITE** and provides business-valued solutions by automating various software engineering tasks.

## Features
The application includes six main tools:
1. **Code Wizard** - Automatically generate code based on user input prompt.
2. **Fix-it** - Identify and fix issues in the provided code.
3. **Code Whisperer** - Provide detailed text & voice-based explanations of code functionality.
4. **Code Optimizer** - Improve code structure and efficiency.
5. **DocuBot** - Generate structured documentation in TXT and DOCX formats.
6. **AI Pair Coder** - Assist developers in real-time coding collaborations.

## Technology Used
CodeNova leverages IBM Granite AI models for core functionalities, ensuring high-performance AI-driven code assistance. Specific features are powered by industry-leading AI services:

- **Python**
- **Streamlit** - Used for Front-End UI and deployment
- **IBM Granite-34B-Code-Instruct:** – Used for code generation, debugging, optimization, and pair programming.
- **IBM Granite-20B-Code-Instruct:** - Powers text-based code explanations.
- **Google Gemini Pro** – Enables comprehensive document generation to streamline documentation tasks.
- **Google Text-to-Speech** – Provides text and voice-based code explanations, enhancing developer understanding.

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
- **Accelerated Development:** AI-driven code generation and refactoring reduce development time.
- **Enhanced Code Quality:** Intelligent debugging and optimization ensure clean, maintainable code.
- **Accessibility:** Provides multiple output formats, including audio explanations.
- **AI-Powered Collaboration:** Acts as a virtual pair programmer, improving productivity and reducing bottlenecks in software development.

## Future Enhancements
- Enhanced AI Models
- Integration with IDE plugins.
- Advanced AI-driven pair programming.
- Enterprise Adoption
- Global Developer Reach

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit changes and push to GitHub.
4. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
- Nidhish Balasubramanya - [nidhishbalasubramaya@gmail.com](nidhishbalasubramanya@gmail.com)
- Nathania Rachael - [nathaniarachael@gmail.com](nathaniarachael@gmail.com)
- Allen Reji - [allenreji@gmail.com](allenreji@gmail.com)
---

*Developed for Generative AI Hackathon with IBM GRANITE*

