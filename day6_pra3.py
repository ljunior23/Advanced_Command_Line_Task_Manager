# Write a program to log messages with timestamps into a file
import datetime

def log_message(file_path, message):
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f" {timestamp} - {message}\n")
        print(f"Message logged: {message}")
    except Exception as e:
        print(f"Error logging message: {e}")

# Example usage
log_message("data.txt", "This is a test log message.")