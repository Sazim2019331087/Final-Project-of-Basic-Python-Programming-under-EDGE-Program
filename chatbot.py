# Project title: Customer Support Chatbot Simulation
# Developer: Md. Sazim Mahmudur Rahman
# Basic Programming with Python Batch 03 under EDGE Program

import json
import time
from datetime import datetime

def load_responses():
    try:
        with open("responses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "Support":"Contact sazimmahmud2020@gmail.com"
        }

def log_query(query, category, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "query": query,
        "category": category,
        "response": response
    }
    with open("query_logs.json", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

def categorize_query(query, responses):
    for category in responses:
        if category.lower() in query.lower():
            return category, responses[category]
    return None, "Sorry, I couldn't understand that. Please try again."

def view_logs():
    try:
        with open("query_logs.json", "r") as log_file:
            logs = [json.loads(line) for line in log_file]
            
            print("\nView Logs")
            print("1. View all logs")
            print("2. Filter by category")
            print("3. Filter by date (YYYY-MM-DD)")
            choice = input("Enter your choice: ")

            if choice == "2":
                category = input("Enter category to filter by: ")
                logs = [log for log in logs if log["category"].lower() == category.lower()]
            elif choice == "3":
                date = input("Enter date to filter by (YYYY-MM-DD): ")
                logs = [log for log in logs if log["timestamp"].startswith(date)]

            for log in logs:
                print(log)
    except FileNotFoundError:
        print("No logs found.")

def start_chat(responses):
    print("\nChat Session: Type 'exit' to end the chat.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        category, response = categorize_query(query, responses)
        print(f"Chatbot: {response}\n")
        log_query(query, category, response)

def main():
    responses = load_responses()

    while True:
        print("\nBanglalink Customer Support Chatbot")
        print("1. Start Chat Session")
        print("2. View Logs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_chat(responses)
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
