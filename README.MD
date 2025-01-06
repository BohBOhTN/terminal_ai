# Terminal AI Chat Application

A Python-based terminal application that enables interactive conversations with an AI assistant, powered by OpenAI's GPT models. The app supports saving, listing, and managing conversation history using PostgreSQL as the database backend.

---

## Features

1. **Interactive Conversations**:
   - Start a new conversation or continue a previous one.
   - Seamless interaction with GPT-4 for dynamic and meaningful responses.

2. **Conversation Management**:
   - Save conversations to a PostgreSQL database.
   - List all saved conversations for review.
   - Continue from a saved conversation.
   - Delete specific conversations by ID.

3. **Error Handling**:
   - Robust handling of API and database errors to ensure smooth user experience.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- PostgreSQL database
- API key from OpenAI
- `dotenv` package for environment variables

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/BohBOhTN/terminal_ai.git
   cd terminal_ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the environment:
   - Create a `.env` file in the project directory with the following:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     DATABASE_URL=postgresql://username:password@hostname:port/dbname
     ```

4. Set up your PostgreSQL database:
   - Ensure your database has a `conversations` table:
     ```sql
     CREATE TABLE conversations (
         conversation_id SERIAL PRIMARY KEY,
         user_message TEXT NOT NULL,
         ai_response TEXT
     );
     ```

---

## Usage

Run the application:
```bash
python main.py
```

### Menu Options:
1. **Start a new conversation**:
   - Interact with the AI from scratch.
   - Type "exit" to end the conversation.
   - Optionally save the conversation after finishing.

2. **List previous conversations**:
   - View saved conversations with their IDs and user messages.

3. **Continue a previous conversation**:
   - Resume interaction with the AI from a saved conversation.

4. **Delete a conversation**:
   - Remove a conversation by its ID.

5. **Exit**:
   - Close the application.

---

## Development Notes

### Recent Updates:
- Fixed infinite input loop in conversation mode.
- Improved error handling for API and database interactions.
- Enhanced save conversation functionality to include user-AI message pairs.

### Future Improvements:
- Add support for exporting conversations to a file.
- Implement a graphical user interface (GUI).
- Optimize conversation storage for large datasets.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Developed by BohBOhTN.
