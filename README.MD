# Terminal AI Chat Application & Python Automation Scripts

## Terminal AI Chat Application

A Python-based terminal application that enables interactive conversations with an AI assistant, powered by OpenAI's GPT models. The app supports saving, listing, and managing conversation history using PostgreSQL as the database backend.

### Features

- **Interactive Conversations**:
  - Start a new conversation or continue a previous one.
  - Seamless interaction with GPT-4 for dynamic and meaningful responses.
- **Conversation Management**:
  - Save conversations to a PostgreSQL database.
  - List all saved conversations for review.
  - Continue from a saved conversation.
  - Delete specific conversations by ID.
- **Error Handling**:
  - Robust handling of API and database errors to ensure smooth user experience.

### Setup Instructions

#### Prerequisites

- Python 3.8 or later
- PostgreSQL database
- API key from OpenAI
- `dotenv` package for environment variables

#### Installation

1. Clone the repository:
   ```
   git clone https://github.com/BohBOhTN/terminal_ai.git
   cd terminal_ai
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the environment:
   - Create a `.env` file in the project directory with the following:
     ```
     OPENAI_API_KEY=your_openai_api_key
     DATABASE_URL=postgresql://username:password@hostname:port/dbname
     ```

4. Set up your PostgreSQL database:
   - Ensure your database has a conversations table:
     ```
     CREATE TABLE conversations (
         conversation_id SERIAL PRIMARY KEY,
         user_message TEXT NOT NULL,
         ai_response TEXT
     );
     ```

#### Developer Notes

##### Recent Updates

- Fixed infinite input loop in conversation mode.
- Improved error handling for API and database interactions.
- Enhanced save conversation functionality to include user-AI message pairs.

##### Future Improvements

- Add support for exporting conversations to a file.
- Implement a graphical user interface (GUI).
- Optimize conversation storage for large datasets.

#### Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

#### License

This project is licensed under the MIT License. See the LICENSE file for details.

#### Author

Developed by BohBOhTN.

## Python Automation Scripts

This project contains various Python scripts to automate tasks and handle operations for different use cases. One key feature is the `convert_to_one_line.py` script, designed to convert multiline Python code into a single line suitable for CMD environments.

### `convert_to_one_line.py` Script

#### Purpose

Some command-line interfaces (CMD) do not accept multiline code and automatically break it into separate lines, causing errors. The `convert_to_one_line.py` script converts multiline code into a single line for CMD.

#### How it works

The script takes a `.txt` file as input and returns its contents as a single line, replacing newline characters with spaces.

#### Usage

1. Place the `convert_to_one_line.py` script in your project directory.
2. Prepare a `.txt` file (e.g., `input.txt`) containing multiline code.
3. Run the script:
   ```
   python convert_to_one_line.py input.txt
   ```

#### Benefits

- Converts multiline Python scripts into one-line commands for compatibility with CMD environments.

By combining the Terminal AI Chat Application with Python Automation Scripts, users can experience seamless interactions with an AI assistant and efficiently automate tasks with Python scripts. Contributions to both projects are welcome.