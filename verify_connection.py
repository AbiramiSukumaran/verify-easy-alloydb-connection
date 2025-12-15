import os
import psycopg2 # pip install psycopg2-binary
from datetime import datetime

# CONFIGURATION
# Replace this with the Private IP of your AlloyDB Instance
DB_HOST = <<>> 
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
# Replace this with your actual AlloyDB password    
DB_PASS = <<>>

def test_connection() -> str:
    print(f"🔌 Attempting to connect to AlloyDB at {DB_HOST}...")
    response = ""
    try:
        # 1. Establish Connection
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.autocommit = True
        cursor = conn.cursor()
        print("✅ Connection Successful!")

        # 2. Run a Test Query (Version Check)
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"📊 Database Version: {db_version[0]}")

        # 3. Create a Dummy Table & Insert Data
        print("🛠  Creating test table...")
        cursor.execute("CREATE TABLE IF NOT EXISTS quick_test (id SERIAL PRIMARY KEY, info TEXT, created_at TIMESTAMP);")
        
        current_time = datetime.now()
        cursor.execute("INSERT INTO quick_test (info, created_at) VALUES (%s, %s)", ("Hello AlloyDB", current_time))
        print(f"📝 Inserted row with timestamp: {current_time}")

        # 4. Read it back
        cursor.execute("SELECT * FROM quick_test ORDER BY id DESC LIMIT 1;")
        row = cursor.fetchone()
        print(f"🔎 Read back row: ID={row[0]}, Info='{row[1]}'")

        # Clean up
        cursor.close()
        conn.close()
        response = "🎉 SUCCESS: Your AlloyDB instance is fully operational and ready for your AI Agent!"
        print("\n🎉 SUCCESS: Your AlloyDB instance is fully operational and ready for your AI Agent! Check databse for data")

    except Exception as e:
        print(f"\n❌ ERROR: Could not connect to AlloyDB.")
        print(f"Details: {e}")
        print("\nTroubleshooting Tips:")
        print("1. Are you running this from a resource (VM/Cloud Run) inside 'easy-alloydb-vpc'?")
        print("2. Did you enable 'VPC Egress' if using Cloud Run?")
        print("3. Is the DB_HOST correct? Check the AlloyDB console for the Private IP.")
        response = f"Details: {e}"
    return response