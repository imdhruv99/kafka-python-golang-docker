import random
import time

def generate_log():
    log_levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    messages = [
        "System started successfully.",
        "Error encountered while connecting to database.",
        "Debugging the user login issue.",
        "Warning: Disk space running low."
    ]
    log_level = random.choice(log_levels)
    message = random.choice(messages)
    return f"{log_level}: {message}"

if __name__ == "__main__":
    while True:
        log = generate_log()
        print(log)
        time.sleep(1)