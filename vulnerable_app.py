import sqlite3
import os
import pickle
import subprocess
import hashlib

# ----------------------------------------------------------------
# Vulnerable Python Web Application — For Security Review Purposes
# ----------------------------------------------------------------

# VULNERABILITY 1: Hardcoded credentials
DB_PASSWORD = "admin123"
SECRET_KEY  = "mysecretkey"
ADMIN_USER  = "admin"
ADMIN_PASS  = "password"

def get_db_connection():
    # VULNERABILITY 2: No parameterized queries — SQL Injection
    conn = sqlite3.connect("users.db")
    return conn

def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    # VULNERABILITY 2: SQL Injection — user input directly in query
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def get_user_file(filename):
    # VULNERABILITY 3: Path Traversal — no sanitization of filename
    base_dir = "/var/www/files/"
    filepath = base_dir + filename
    with open(filepath, "r") as f:
        return f.read()

def hash_password(password):
    # VULNERABILITY 4: Weak hashing — MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

def run_command(user_input):
    # VULNERABILITY 5: Command Injection — unsanitized input passed to shell
    output = subprocess.check_output("ping -c 1 " + user_input, shell=True)
    return output

def load_user_session(session_data):
    # VULNERABILITY 6: Insecure Deserialization — pickle with untrusted data
    user = pickle.loads(session_data)
    return user

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    # VULNERABILITY 7: Password stored in plaintext
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def debug_info():
    # VULNERABILITY 8: Sensitive data exposure — exposes env vars and internals
    print("DB_PASSWORD:", DB_PASSWORD)
    print("SECRET_KEY:", SECRET_KEY)
    print("Environment:", os.environ)
    print("CWD:", os.getcwd())

def read_config(config_file="config.txt"):
    # VULNERABILITY 9: No input validation — any file can be read
    with open(config_file, "r") as f:
        return f.read()

# VULNERABILITY 10: Debug mode left enabled, overly broad exception handling
DEBUG = True

def process_request(data):
    try:
        result = login(data["username"], data["password"])
        return result
    except:
        # Catches ALL exceptions — hides real errors, bad practice
        if DEBUG:
            import traceback
            traceback.print_exc()
        return None