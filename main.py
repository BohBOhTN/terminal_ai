from openai import OpenAI
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

# Function to create a new conversation or continue an old one
def interact_with_ai(conversation_id=None):
    # Initialize conversation history
    conversation = []

    if conversation_id:
        # Fetch the previous conversation from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_message, ai_response FROM conversations WHERE conversation_id = %s", (conversation_id,))
        rows = cursor.fetchall()
        for row in rows:
            conversation.append({"role": "user", "content": row[0]})
            conversation.append({"role": "assistant", "content": row[1]})
        cursor.close()
        conn.close()

    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            print("Ending the conversation.")
            break

        # Add user message to conversation history
        conversation.append({"role": "user", "content": prompt})

        try:
            # Call the OpenAI API to get a response
            response = client.chat.completions.create(
                model="gpt-4",  # Ensure correct model name
                messages=conversation,  # Pass the conversation history here
                temperature=1,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Extract the AI's response from the response object
            ai_response = response.choices[0].message.content.strip()
            print(f"AI: {ai_response}")

            # Add AI response to conversation history
            conversation.append({"role": "assistant", "content": ai_response})

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        # Ask user if they want to save the conversation
        save = input("Do you want to save this conversation? (y/n): ")
        if save.lower() == "y":
            save_conversation(conversation)

# Function to save conversation to the database
def save_conversation(conversation):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for i in range(0, len(conversation), 2):  # Save user and AI messages as pairs
            user_message = conversation[i]['content']
            ai_response = conversation[i + 1]['content'] if i + 1 < len(conversation) else None
            cursor.execute(
                "INSERT INTO conversations (user_message, ai_response) VALUES (%s, %s)",
                (user_message, ai_response)
            )
        conn.commit()
        print("Conversation saved successfully.")
    except Exception as e:
        print(f"Failed to save conversation: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to list saved conversations
def list_conversations():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT conversation_id, user_message FROM conversations")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]} - User: {row[1]}")
    except Exception as e:
        print(f"Failed to list conversations: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to delete a conversation
def delete_conversation(conversation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM conversations WHERE conversation_id = %s", (conversation_id,))
        conn.commit()
        print(f"Conversation with ID {conversation_id} deleted.")
    except Exception as e:
        print(f"Failed to delete conversation: {e}")
    finally:
        cursor.close()
        conn.close()

# Main function
def main():
    while True:
        print("\nOptions:")
        print("1. Start a new conversation")
        print("2. List previous conversations")
        print("3. Continue a previous conversation")
        print("4. Delete a conversation")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            interact_with_ai()
        elif option == "2":
            list_conversations()
        elif option == "3":
            conversation_id = input("Enter conversation ID to continue: ")
            interact_with_ai(conversation_id=int(conversation_id))
        elif option == "4":
            conversation_id = input("Enter conversation ID to delete: ")
            delete_conversation(conversation_id=int(conversation_id))
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
