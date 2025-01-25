# Customer Support Chatbot Simulation

This project, **Customer Support Chatbot Simulation**, is created as the final project for the course **"Basic Programming with Python (Batch 03) under EDGE Program"**. The chatbot simulates a customer support system for **Banglalink**, providing automated responses to common queries based on predefined categories.

## Features

1. **Query Categorization**:

   - Predefined categories for user queries include:

     | Recharge    | Internet       | Call Rate    | SIM Replace |
     | ----------- | -------------- | ------------ | ----------- |
     | New SIM     | Coverage       | Offers       | Balance     |
     | Caller Tune | Roaming        | Bill Payment | Problem     |
     | App         | Service Center |              |             |

   - Each category has a detailed response stored in a JSON file (`responses.json`).

2. **Chatbot Interface**:

   - A console-based chatbot where users can type their queries.
   - The chatbot matches queries to predefined categories and provides appropriate responses.
   - Default response for unmatched queries: `"Sorry, I couldn't understand that. Please try again."`

3. **Query Logging**:

   - Logs user queries, categories, and responses to a file (`query_logs.json`) for review.
   - Each log includes:
     - Timestamp
     - User query
     - Matched category
     - Response

4. **Log Viewer**:

   - Users can view and filter logs by category or date.

5. **Personalized Introduction**:

   - The chatbot introduces itself as Sazim from **"Basic Programming with Python Batch 03"**.

## File Structure

```
project-directory/
|-- chatbot.py             # Main Python script for the chatbot
|-- responses.json         # Predefined categories and responses
|-- query_logs.json        # Log file for storing user queries and responses
|-- README.md              # Project documentation
```

## How to Run the Project

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/Sazim2019331087/Final-Project-of-Basic-Python-Programming-under-EDGE-Program/
   cd Final-Project-of-Basic-Python-Programming-under-EDGE-Program
   ```

2. Ensure Python is installed on system (Python 3.6 or later).

3. Install any required dependencies (if applicable).

4. Run the chatbot:

   ```bash
   python chatbot.py
   ```

5. Interact with the chatbot through the console interface. Use the menu options to:

   - Start a chat session.
   - View or filter logs.

## Example Interaction

```
Customer Support Chatbot
1. Start Chat Session
2. View Logs
3. Exit

Enter your choice: 1

Chat Session: Type 'exit' to end the chat.
You: Balance
Chatbot: To check your balance, dial *124# from your Banglalink number.

You: exit
```

## Customization

- Add or modify categories and responses by editing the `responses.json` file.
- Logs are stored in `query_logs.json` and can be filtered by category or date through the menu interface.

## About

- **Project Title**: Customer Support Chatbot Simulation
- **Course**: Basic Programming with Python Batch 03 under EDGE Program
- **Developer**: Md. Sazim Mahmudur Rahman

---
