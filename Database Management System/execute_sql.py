"""
Database Management System - Interactive SQL Script Execution & Management Utility
Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
Course: 25ITT31 - Database Management Systems
Department of Information Technology, Velalar College of Engineering and Technology
"""

import os
import sys
import sqlite3
import datetime

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "gym_management.db")
DB_FILE = os.path.abspath(DB_FILE)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sql_queries_output.txt")

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def print_table(cursor, title, file_handle=None):
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    col_widths = [len(c) for c in columns]
    for row in rows:
        for idx, val in enumerate(row):
            col_widths[idx] = max(col_widths[idx], len(str(val) if val is not None else "NULL"))
    
    header_line = "+" + "+".join(["-" * (w + 2) for w in col_widths]) + "+"
    title_banner = f"\n=== {title} ==="
    
    def emit(text):
        print(text)
        if file_handle:
            file_handle.write(text + "\n")
            
    emit(title_banner)
    emit(header_line)
    header_str = "|" + "|".join([f" {columns[i].center(col_widths[i])} " for i in range(len(columns))]) + "|"
    emit(header_str)
    emit(header_line)
    for row in rows:
        row_str = "|" + "|".join([f" {str(row[i] if row[i] is not None else 'NULL').ljust(col_widths[i])} " for i in range(len(columns))]) + "|"
        emit(row_str)
    emit(header_line)
    emit(f"Total Rows: {len(rows)}\n")

def create_database(interactive=False):
    print("\n" + "=" * 75)
    print("  DBMS: CREATE DATABASE & SCHEMA TABLES (gym_db)")
    print("=" * 75)
    
    if interactive:
        confirm = input("This will reset all tables in gym_management.db. Proceed? (Y/N) [Y]: ").strip().upper()
        if confirm == 'N':
            print("Operation aborted by user.")
            return

    conn = get_connection()
    cursor = conn.cursor()

    drop_tables = [
        "reports", "attendance", "trainer_assignments", 
        "memberships", "trainers", "membership_plans", "members"
    ]
    for table in drop_tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

    cursor.execute("""
    CREATE TABLE members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL CHECK (age >= 14),
        contact_no TEXT NOT NULL,
        email TEXT UNIQUE,
        registration_date DATE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE membership_plans (
        plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plan_name TEXT NOT NULL UNIQUE,
        duration INTEGER NOT NULL CHECK (duration > 0),
        fee REAL NOT NULL CHECK (fee >= 0.0),
        facilities TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE memberships (
        membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        plan_id INTEGER NOT NULL,
        start_date DATE NOT NULL,
        expiry_date DATE NOT NULL,
        status TEXT NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Expired', 'Expiring Soon')),
        FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
        FOREIGN KEY (plan_id) REFERENCES membership_plans(plan_id) ON DELETE RESTRICT
    );
    """)

    cursor.execute("""
    CREATE TABLE trainers (
        trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        contact_no TEXT NOT NULL,
        email TEXT UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE trainer_assignments (
        assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        trainer_id INTEGER NOT NULL,
        assignment_date DATE NOT NULL,
        status TEXT NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'Transferred')),
        FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
        FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id) ON DELETE RESTRICT
    );
    """)

    cursor.execute("""
    CREATE TABLE attendance (
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        attendance_date DATE NOT NULL,
        check_in_time TEXT NOT NULL,
        check_out_time TEXT,
        duration_minutes INTEGER DEFAULT 0,
        FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE reports (
        report_id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_type TEXT NOT NULL,
        generated_date TEXT DEFAULT (datetime('now','localtime')),
        details TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print("[SUCCESS] All 7 relational tables created successfully with PK, FK, and CHECK constraints.")
    print(f"[INFO] Database location: {DB_FILE}\n")

def insert_default_records():
    conn = get_connection()
    cursor = conn.cursor()

    plans = [
        (1, 'Basic Fitness', 1, 1500.00, 'Cardio Machines, Locker Room, General Gym Floor'),
        (2, 'Standard Strength', 3, 3800.00, 'Free Weights, Resistance Machines, Locker Room, Shower'),
        (3, 'Pro Athlete', 6, 7000.00, 'All Standard + Crossfit Zone, Steam Bath, Nutrition Consultation'),
        (4, 'Elite Annual VIP', 12, 12500.00, 'All Pro + Personal Locker, Sauna, Swimming Pool, 5 Guest Passes')
    ]
    cursor.executemany("INSERT OR REPLACE INTO membership_plans VALUES (?, ?, ?, ?, ?);", plans)

    trainers = [
        (1, 'Vikram Rathore', 'Strength & Bodybuilding', '9876501234', 'vikram.trainer@gym.com'),
        (2, 'Ananya Sharma', 'Yoga & Flexibility', '9876502345', 'ananya.yoga@gym.com'),
        (3, 'Karthik Raja', 'CrossFit & Functional HIIT', '9876503456', 'karthik.hiit@gym.com'),
        (4, 'Divya Menon', 'Weight Loss & Aerobics', '9876504567', 'divya.aerobics@gym.com'),
        (5, 'Rahul Varma', 'Rehabilitation & Conditioning', '9876505678', 'rahul.rehab@gym.com')
    ]
    cursor.executemany("INSERT OR REPLACE INTO trainers VALUES (?, ?, ?, ?, ?);", trainers)

    members = [
        (1, 'Aarav Patel', 24, '9840112345', 'aarav.patel@email.com', '2026-01-05'),
        (2, 'Sneha Reddy', 28, '9840223456', 'sneha.reddy@email.com', '2026-01-12'),
        (3, 'Rohan Verma', 32, '9840334567', 'rohan.verma@email.com', '2026-01-20'),
        (4, 'Priya Krishnan', 22, '9840445678', 'priya.k@email.com', '2026-02-02'),
        (5, 'Aditya Joshi', 45, '9840556789', 'aditya.joshi@email.com', '2026-02-15'),
        (6, 'Meera Nair', 30, '9840667890', 'meera.nair@email.com', '2026-03-01'),
        (7, 'Siddharth Sen', 27, '9840778901', 'siddharth.sen@email.com', '2026-03-10'),
        (8, 'Kavita Das', 35, '9840889012', 'kavita.das@email.com', '2026-04-05'),
        (9, 'Varun Dhawan', 21, '9840990123', 'varun.dhawan@email.com', '2026-04-18'),
        (10, 'Ishita Roy', 26, '9841001234', 'ishita.roy@email.com', '2026-05-02'),
        (11, 'Manoj Kumar', 38, '9841112345', 'manoj.kumar@email.com', '2026-05-20'),
        (12, 'Tanvi Bansal', 29, '9841223456', 'tanvi.b@email.com', '2026-06-11'),
        (13, 'Gaurav Gupta', 33, '9841334567', 'gaurav.gupta@email.com', '2026-07-04'),
        (14, 'Deepika Pillai', 25, '9841445678', 'deepika.p@email.com', '2026-08-15'),
        (15, 'Harish Balan', 41, '9841556789', 'harish.balan@email.com', '2026-09-01')
    ]
    cursor.executemany("INSERT OR REPLACE INTO members VALUES (?, ?, ?, ?, ?, ?);", members)

    memberships = [
        (1, 1, 4, '2026-01-05', '2027-01-05', 'Active'),
        (2, 2, 2, '2026-01-12', '2026-04-12', 'Expired'),
        (3, 3, 3, '2026-01-20', '2026-07-20', 'Expired'),
        (4, 4, 3, '2026-02-02', '2026-08-02', 'Expired'),
        (5, 5, 4, '2026-02-15', '2027-02-15', 'Active'),
        (6, 6, 2, '2026-03-01', '2026-06-01', 'Expired'),
        (7, 7, 3, '2026-05-20', '2026-11-20', 'Expiring Soon'),
        (8, 8, 1, '2026-10-22', '2026-11-22', 'Expiring Soon'),
        (9, 9, 3, '2026-06-01', '2026-12-01', 'Active'),
        (10, 10, 2, '2026-05-02', '2026-08-02', 'Expired'),
        (11, 11, 4, '2026-05-20', '2027-05-20', 'Active'),
        (12, 12, 3, '2026-06-11', '2026-12-11', 'Active'),
        (13, 13, 2, '2026-07-04', '2026-10-04', 'Expired'),
        (14, 14, 4, '2026-08-15', '2027-08-15', 'Active'),
        (15, 15, 3, '2026-09-01', '2027-03-01', 'Active')
    ]
    cursor.executemany("INSERT OR REPLACE INTO memberships VALUES (?, ?, ?, ?, ?, ?);", memberships)

    assignments = [
        (1, 1, 1, '2026-01-06', 'Active'),
        (2, 2, 2, '2026-01-15', 'Completed'),
        (3, 3, 3, '2026-01-22', 'Completed'),
        (4, 4, 4, '2026-02-05', 'Completed'),
        (5, 5, 5, '2026-02-18', 'Active'),
        (6, 6, 2, '2026-03-05', 'Completed'),
        (7, 7, 1, '2026-05-22', 'Active'),
        (8, 8, 4, '2026-10-23', 'Active'),
        (9, 9, 3, '2026-06-05', 'Active'),
        (10, 10, 2, '2026-05-05', 'Completed'),
        (11, 11, 1, '2026-05-25', 'Active'),
        (12, 12, 3, '2026-06-15', 'Active'),
        (13, 13, 1, '2026-07-06', 'Completed'),
        (14, 14, 2, '2026-08-18', 'Active'),
        (15, 15, 5, '2026-09-05', 'Active')
    ]
    cursor.executemany("INSERT OR REPLACE INTO trainer_assignments VALUES (?, ?, ?, ?, ?);", assignments)

    attendance_records = [
        (1, '2026-01-10', '06:15:00', '07:30:00', 75),
        (2, '2026-01-10', '07:00:00', '08:00:00', 60),
        (3, '2026-01-10', '18:00:00', '19:15:00', 75),
        (1, '2026-01-12', '06:20:00', '07:45:00', 85),
        (2, '2026-01-12', '07:10:00', '08:10:00', 60),
        (3, '2026-01-13', '18:15:00', '19:30:00', 75),
        (1, '2026-01-15', '06:30:00', '07:40:00', 70),
        (2, '2026-01-16', '07:05:00', '08:20:00', 75),
        (3, '2026-01-25', '18:00:00', '19:00:00', 60),
        (1, '2026-02-05', '06:15:00', '07:30:00', 75),
        (4, '2026-02-05', '08:00:00', '09:00:00', 60),
        (5, '2026-02-18', '17:30:00', '18:45:00', 75),
        (1, '2026-02-19', '06:20:00', '07:30:00', 70),
        (4, '2026-02-20', '08:15:00', '09:15:00', 60),
        (5, '2026-02-22', '18:00:00', '19:15:00', 75),
        (1, '2026-03-05', '06:10:00', '07:25:00', 75),
        (6, '2026-03-05', '07:00:00', '08:00:00', 60),
        (7, '2026-03-12', '18:30:00', '19:45:00', 75),
        (5, '2026-03-15', '17:45:00', '19:00:00', 75),
        (6, '2026-03-18', '07:15:00', '08:15:00', 60),
        (7, '2026-03-25', '18:00:00', '19:10:00', 70),
        (1, '2026-04-08', '06:30:00', '07:45:00', 75),
        (8, '2026-04-10', '07:30:00', '08:30:00', 60),
        (5, '2026-04-12', '18:00:00', '19:15:00', 75),
        (9, '2026-04-20', '19:00:00', '20:15:00', 75),
        (8, '2026-04-22', '07:45:00', '08:45:00', 60),
        (9, '2026-04-28', '18:30:00', '19:50:00', 80),
        (1, '2026-05-04', '06:15:00', '07:30:00', 75),
        (10, '2026-05-05', '08:00:00', '09:00:00', 60),
        (11, '2026-05-22', '06:45:00', '08:00:00', 75),
        (7, '2026-05-24', '18:15:00', '19:30:00', 75),
        (9, '2026-05-25', '19:00:00', '20:15:00', 75),
        (10, '2026-05-28', '08:10:00', '09:10:00', 60),
        (1, '2026-06-05', '06:30:00', '07:45:00', 75),
        (11, '2026-06-08', '06:45:00', '07:55:00', 70),
        (12, '2026-06-15', '17:30:00', '18:45:00', 75),
        (7, '2026-06-18', '18:00:00', '19:15:00', 75),
        (9, '2026-06-20', '18:45:00', '20:00:00', 75),
        (12, '2026-06-25', '17:40:00', '18:50:00', 70),
        (1, '2026-07-08', '06:15:00', '07:35:00', 80),
        (11, '2026-07-10', '06:30:00', '07:45:00', 75),
        (13, '2026-07-12', '18:00:00', '19:15:00', 75),
        (7, '2026-07-15', '18:15:00', '19:30:00', 75),
        (12, '2026-07-20', '17:30:00', '18:45:00', 75),
        (13, '2026-07-26', '18:10:00', '19:10:00', 60),
        (1, '2026-08-04', '06:20:00', '07:30:00', 70),
        (11, '2026-08-10', '06:30:00', '07:45:00', 75),
        (14, '2026-08-18', '07:00:00', '08:15:00', 75),
        (9, '2026-08-20', '19:00:00', '20:15:00', 75),
        (12, '2026-08-22', '17:30:00', '18:45:00', 75),
        (14, '2026-08-28', '07:15:00', '08:30:00', 75),
        (1, '2026-09-02', '06:15:00', '07:30:00', 75),
        (15, '2026-09-05', '06:30:00', '07:45:00', 75),
        (11, '2026-09-10', '06:45:00', '08:00:00', 75),
        (14, '2026-09-15', '07:00:00', '08:15:00', 75),
        (15, '2026-09-20', '06:30:00', '07:40:00', 70),
        (9, '2026-09-25', '18:30:00', '19:45:00', 75),
        (1, '2026-10-05', '06:30:00', '07:45:00', 75),
        (11, '2026-10-08', '06:40:00', '07:50:00', 70),
        (14, '2026-10-12', '07:15:00', '08:25:00', 70),
        (15, '2026-10-18', '06:30:00', '07:45:00', 75),
        (8, '2026-10-25', '07:30:00', '08:30:00', 60),
        (12, '2026-10-28', '17:30:00', '18:45:00', 75),
        (1, '2026-11-02', '06:15:00', '07:30:00', 75),
        (11, '2026-11-04', '06:30:00', '07:45:00', 75),
        (14, '2026-11-06', '07:00:00', '08:15:00', 75),
        (15, '2026-11-08', '06:30:00', '07:45:00', 75),
        (8, '2026-11-10', '07:30:00', '08:30:00', 60),
        (9, '2026-11-12', '18:45:00', '20:00:00', 75),
        (12, '2026-11-14', '17:30:00', '18:45:00', 75),
        (1, '2026-11-16', '06:20:00', '07:35:00', 75),
        (15, '2026-11-17', '06:30:00', '07:50:00', 80)
    ]
    cursor.executemany("""
    INSERT INTO attendance (member_id, attendance_date, check_in_time, check_out_time, duration_minutes)
    VALUES (?, ?, ?, ?, ?);
    """, attendance_records)

    conn.commit()
    conn.close()
    print("[SUCCESS] Default sample records populated into database.")

def manual_add_member():
    print("\n--- [MANUAL INPUT] REGISTER NEW MEMBER ---")
    try:
        name = input("Enter Member Full Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        age = int(input("Enter Member Age (>= 14): ").strip())
        if age < 14:
            print("Validation Error: Member must be at least 14 years old.")
            return
        phone = input("Enter 10-Digit Contact Number: ").strip()
        if len(phone) < 10:
            print("Validation Error: Phone must be at least 10 digits.")
            return
        email = input("Enter Email Address: ").strip()
        reg_date = datetime.date.today().isoformat()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO members (name, age, contact_no, email, registration_date) VALUES (?, ?, ?, ?, ?)",
                    (name, age, phone, email, reg_date))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        print(f"[SUCCESS] Member '{name}' registered successfully with ID: {new_id}!")
    except Exception as e:
        print(f"Error adding member: {e}")

def manual_add_plan():
    print("\n--- [MANUAL INPUT] CREATE NEW MEMBERSHIP PLAN ---")
    try:
        name = input("Enter Plan Name: ").strip()
        duration = int(input("Enter Duration in Months: ").strip())
        fee = float(input("Enter Plan Fee (INR): ").strip())
        facilities = input("Enter Facilities Offered (e.g. Cardio, Sauna, Pool): ").strip()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO membership_plans (plan_name, duration, fee, facilities) VALUES (?, ?, ?, ?)",
                    (name, duration, fee, facilities))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        print(f"[SUCCESS] Membership Plan '{name}' added with Plan ID: {new_id}!")
    except Exception as e:
        print(f"Error adding plan: {e}")

def manual_add_trainer():
    print("\n--- [MANUAL INPUT] ADD NEW TRAINER ---")
    try:
        name = input("Enter Trainer Name: ").strip()
        spec = input("Enter Specialization (Strength, Yoga, HIIT, Cardio): ").strip()
        phone = input("Enter Contact Number: ").strip()
        email = input("Enter Email Address: ").strip()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO trainers (name, specialization, contact_no, email) VALUES (?, ?, ?, ?)",
                    (name, spec, phone, email))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        print(f"[SUCCESS] Trainer '{name}' added successfully with Trainer ID: {new_id}!")
    except Exception as e:
        print(f"Error adding trainer: {e}")

def interactive_insert_menu():
    while True:
        print("\n" + "=" * 70)
        print("  DBMS: INSERT RECORDS MENU (KEYBOARD / SAMPLE)")
        print("=" * 70)
        print(" 1. Insert Default Sample Records (15 Members, 4 Plans, 72 Footfalls)")
        print(" 2. Manually Add New Member via Keyboard")
        print(" 3. Manually Add New Membership Plan via Keyboard")
        print(" 4. Manually Add New Trainer via Keyboard")
        print(" 5. View Current Members Table")
        print(" 0. Back / Exit")
        print("=" * 70)
        choice = input("Enter choice (0-5): ").strip()

        if choice == '1':
            insert_default_records()
        elif choice == '2':
            manual_add_member()
        elif choice == '3':
            manual_add_plan()
        elif choice == '4':
            manual_add_trainer()
        elif choice == '5':
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT member_id, name, age, contact_no, registration_date FROM members LIMIT 15;")
            print_table(cur, "Current Members")
            conn.close()
        elif choice == '0':
            break
        else:
            print("Invalid selection. Please choose 0 to 5.")

def interactive_reports_menu():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        print("\n" + "=" * 75)
        print("  DBMS: SQL QUERIES & REPORT GENERATOR (STEP-BY-STEP)")
        print("=" * 75)
        print(" 1. Registered Members Roster")
        print(" 2. Active Memberships with Plan Details (INNER JOIN)")
        print(" 3. Membership Revenue Report by Plan (SUM & GROUP BY)")
        print(" 4. Grand Total Revenue Summary")
        print(" 5. Membership Status Distribution (Active / Expired / Expiring Soon)")
        print(" 6. Membership Renewal Alert Roster")
        print(" 7. Trainer Workload Distribution")
        print(" 8. Monthly Attendance Footfall Summary")
        print(" 9. Execute Custom SQL Query from Keyboard")
        print(" 10. Run All Reports & Save to outputs/sql_queries_output.txt")
        print(" 0. Exit")
        print("=" * 75)
        choice = input("Enter choice (0-10): ").strip()

        if choice == '1':
            cursor.execute("SELECT member_id, name, age, contact_no, email, registration_date FROM members;")
            print_table(cursor, "REGISTERED MEMBERS ROSTER")
        elif choice == '2':
            cursor.execute("""
            SELECT m.member_id, m.name, p.plan_name, p.fee, ms.start_date, ms.expiry_date, ms.status
            FROM members m
            JOIN memberships ms ON m.member_id = ms.member_id
            JOIN membership_plans p ON ms.plan_id = p.plan_id
            WHERE ms.status = 'Active';
            """)
            print_table(cursor, "ACTIVE MEMBERSHIPS WITH PLAN DETAILS")
        elif choice == '3':
            cursor.execute("""
            SELECT p.plan_id, p.plan_name, p.fee AS plan_fee, 
                   COUNT(ms.membership_id) AS total_subscribers, 
                   SUM(p.fee) AS total_revenue
            FROM membership_plans p
            LEFT JOIN memberships ms ON p.plan_id = ms.plan_id
            GROUP BY p.plan_id, p.plan_name, p.fee
            ORDER BY total_revenue DESC;
            """)
            print_table(cursor, "MEMBERSHIP REVENUE REPORT BY PLAN")
        elif choice == '4':
            cursor.execute("""
            SELECT SUM(p.fee) AS grand_total_revenue, 
                   ROUND(AVG(p.fee), 2) AS avg_revenue_per_plan, 
                   COUNT(ms.membership_id) AS total_memberships_sold
            FROM memberships ms
            JOIN membership_plans p ON ms.plan_id = p.plan_id;
            """)
            print_table(cursor, "GRAND TOTAL REVENUE SUMMARY")
        elif choice == '5':
            cursor.execute("""
            SELECT ms.status, COUNT(*) AS count, 
                   ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM memberships)), 1) AS percentage
            FROM memberships ms
            GROUP BY ms.status;
            """)
            print_table(cursor, "MEMBERSHIP STATUS DISTRIBUTION")
        elif choice == '6':
            cursor.execute("""
            SELECT m.member_id, m.name AS member_name, m.contact_no, p.plan_name, ms.expiry_date, ms.status
            FROM members m
            JOIN memberships ms ON m.member_id = ms.member_id
            JOIN membership_plans p ON ms.plan_id = p.plan_id
            WHERE ms.status IN ('Expired', 'Expiring Soon')
            ORDER BY ms.expiry_date ASC;
            """)
            print_table(cursor, "MEMBERSHIP RENEWAL ALERT ROSTER")
        elif choice == '7':
            cursor.execute("""
            SELECT t.trainer_id, t.name AS trainer_name, t.specialization,
                   COUNT(CASE WHEN ta.status = 'Active' THEN 1 END) AS active_clients,
                   COUNT(ta.assignment_id) AS total_assigned_all_time
            FROM trainers t
            LEFT JOIN trainer_assignments ta ON t.trainer_id = ta.trainer_id
            GROUP BY t.trainer_id, t.name, t.specialization
            ORDER BY active_clients DESC;
            """)
            print_table(cursor, "TRAINER WORKLOAD DISTRIBUTION")
        elif choice == '8':
            cursor.execute("""
            SELECT strftime('%Y-%m', attendance_date) AS workout_month,
                   COUNT(attendance_id) AS total_visits,
                   COUNT(DISTINCT member_id) AS unique_members,
                   ROUND(AVG(duration_minutes), 1) AS avg_session_mins
            FROM attendance
            GROUP BY strftime('%Y-%m', attendance_date)
            ORDER BY workout_month ASC;
            """)
            print_table(cursor, "MONTHLY ATTENDANCE FOOTFALL & DURATION SUMMARY")
        elif choice == '9':
            custom_q = input("\nEnter SQL Query (e.g. SELECT * FROM members WHERE age > 25;):\n> ").strip()
            if custom_q:
                try:
                    cursor.execute(custom_q)
                    if custom_q.strip().upper().startswith("SELECT"):
                        print_table(cursor, "CUSTOM QUERY RESULTS")
                    else:
                        conn.commit()
                        print(f"[SUCCESS] Query executed successfully. Rows affected: {cursor.rowcount}")
                except Exception as e:
                    print(f"SQL Error: {e}")
        elif choice == '10':
            generate_all_reports_to_file()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

    conn.close()

def generate_all_reports_to_file():
    conn = get_connection()
    cursor = conn.cursor()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("=" * 80 + "\n")
        out.write("GYM MEMBERSHIP MANAGEMENT - SQL QUERY EXECUTION OUTPUT\n")
        out.write(f"Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write("=" * 80 + "\n\n")

        cursor.execute("SELECT member_id, name, age, contact_no, email, registration_date FROM members;")
        print_table(cursor, "1. REGISTERED MEMBERS ROSTER", out)

        cursor.execute("""
        SELECT m.member_id, m.name, p.plan_name, p.fee, ms.start_date, ms.expiry_date, ms.status
        FROM members m
        JOIN memberships ms ON m.member_id = ms.member_id
        JOIN membership_plans p ON ms.plan_id = p.plan_id
        WHERE ms.status = 'Active';
        """)
        print_table(cursor, "2. ACTIVE MEMBERSHIPS WITH PLAN DETAILS", out)

        cursor.execute("""
        SELECT p.plan_id, p.plan_name, p.fee AS plan_fee, 
               COUNT(ms.membership_id) AS total_subscribers, 
               SUM(p.fee) AS total_revenue
        FROM membership_plans p
        LEFT JOIN memberships ms ON p.plan_id = ms.plan_id
        GROUP BY p.plan_id, p.plan_name, p.fee
        ORDER BY total_revenue DESC;
        """)
        print_table(cursor, "3. MEMBERSHIP REVENUE REPORT BY PLAN", out)

        cursor.execute("""
        SELECT SUM(p.fee) AS grand_total_revenue, 
               ROUND(AVG(p.fee), 2) AS avg_revenue_per_plan, 
               COUNT(ms.membership_id) AS total_memberships_sold
        FROM memberships ms
        JOIN membership_plans p ON ms.plan_id = p.plan_id;
        """)
        print_table(cursor, "4. GRAND TOTAL REVENUE SUMMARY", out)

        cursor.execute("""
        SELECT ms.status, COUNT(*) AS count, 
               ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM memberships)), 1) AS percentage
        FROM memberships ms
        GROUP BY ms.status;
        """)
        print_table(cursor, "5. MEMBERSHIP STATUS DISTRIBUTION", out)

        cursor.execute("""
        SELECT m.member_id, m.name AS member_name, m.contact_no, p.plan_name, ms.expiry_date, ms.status
        FROM members m
        JOIN memberships ms ON m.member_id = ms.member_id
        JOIN membership_plans p ON ms.plan_id = p.plan_id
        WHERE ms.status IN ('Expired', 'Expiring Soon')
        ORDER BY ms.expiry_date ASC;
        """)
        print_table(cursor, "6. MEMBERSHIP RENEWAL ALERT ROSTER", out)

        cursor.execute("""
        SELECT t.trainer_id, t.name AS trainer_name, t.specialization,
               COUNT(CASE WHEN ta.status = 'Active' THEN 1 END) AS active_clients,
               COUNT(ta.assignment_id) AS total_assigned_all_time
        FROM trainers t
        LEFT JOIN trainer_assignments ta ON t.trainer_id = ta.trainer_id
        GROUP BY t.trainer_id, t.name, t.specialization
        ORDER BY active_clients DESC;
        """)
        print_table(cursor, "7. TRAINER WORKLOAD DISTRIBUTION", out)

        cursor.execute("""
        SELECT strftime('%Y-%m', attendance_date) AS workout_month,
               COUNT(attendance_id) AS total_visits,
               COUNT(DISTINCT member_id) AS unique_members,
               ROUND(AVG(duration_minutes), 1) AS avg_session_mins
        FROM attendance
        GROUP BY strftime('%Y-%m', attendance_date)
        ORDER BY workout_month ASC;
        """)
        print_table(cursor, "8. MONTHLY ATTENDANCE FOOTFALL & DURATION SUMMARY", out)
    conn.close()
    print(f"\n[SUCCESS] Reports exported to: {OUTPUT_FILE}")

if __name__ == "__main__":
    action = sys.argv[1].lower() if len(sys.argv) > 1 else "interactive"
    if action == "create":
        create_database(interactive=True)
    elif action == "insert":
        interactive_insert_menu()
    elif action == "reports":
        interactive_reports_menu()
    elif action == "all":
        create_database(interactive=False)
        insert_default_records()
        generate_all_reports_to_file()
    else:
        print("\nGym Management DBMS Controller")
        print("Choose: [create | insert | reports | all]")
