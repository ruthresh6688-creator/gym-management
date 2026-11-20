# Gym Membership Management and Fitness Activity Analysis System
### Scenario 27 — Project-Based Assessment (Academic Year 2026 - 2027 ODD)
**Class:** 25IT3A&B | **Department:** Information Technology  
**Institution:** Velalar College of Engineering and Technology (Autonomous), Erode - 12  
**Affiliated Subjects:**
1. **25ITT33** – Software Engineering
2. **25ITT31** – Database Management Systems
3. **25ITT32** – Java Programming
4. **25ITC31** – Foundations of Data Science

---

## 1. Executive Summary & Problem Statement

Gyms and fitness centres face significant operational bottlenecks when relying on manual recordkeeping or disparate spreadsheets:
- **Member Tracking & Expiry Alerts:** Inability to proactively flag expiring memberships leads to lost subscription revenue and unmonitored facility access.
- **Attendance Logging Inaccuracies:** Manual paper logs fail to track check-in and check-out times, preventing calculation of workout durations, peak hour capacity, and member participation habits.
- **Trainer Overburdening:** Lack of workload visibility results in suboptimal trainer-to-member assignment ratios, diminishing instructional quality.
- **Absence of Business Intelligence:** Raw transactional records remain unanalyzed, leaving management without actionable insights into membership tier popularity, financial revenue trends, and member retention.

This project delivers a complete, enterprise-grade **Gym Membership Management and Fitness Activity Analysis System** utilizing a 3-tier architecture:
- **Software Engineering:** Formal SRS (IEEE 830), functional and non-functional requirements, complete UML and architectural diagrams, and comprehensive testing documentation.
- **DBMS:** 3NF normalized relational schema, primary/foreign key constraints, transactional DML, joins, aggregations, and business reporting queries.
- **Java Programming:** Object-oriented desktop console engine featuring inheritance, encapsulation, polymorphism, custom exception handling, and JDBC persistence.
- **Foundation of Data Science:** Python analytics engine (Pandas, Matplotlib, Seaborn) performing data extraction, cleaning, feature engineering, and high-resolution visual analytics.

---

## 2. System Architecture

```
+---------------------------------------------------------------------------------------+
|                                    USER INTERFACE                                     |
|             Gym Administrators  *  Fitness Trainers  *  Gym Members                   |
+------------------------------------------+--------------------------------------------+
                                           |
                                   (User Interaction)
                                           v
+---------------------------------------------------------------------------------------+
|                            APPLICATION LAYER (JAVA - JDK 17)                          |
|  * Member Management Module            * Attendance Check-In / Check-Out Tracking     |
|  * Membership Plans & Registration     * Trainer Assignment & Workload Management     |
|  * Dynamic Status & Renewal Engine     * Financial & Operational Reporting            |
|  * JDBC Layer (PreparedStatements, Transactions, Custom Exception Handling)           |
+------------------------------------+------------------+-------------------------------+
                                     |                  ^
                             (SQL Read / Write)         | (JDBC Query Result)
                                     v                  |
+-------------------------------------------------------+-------------------------------+
|                             DATA PERSISTENCE LAYER (DBMS)                             |
|  * Relational Schema (3NF Normalized)                 * Integrity Constraints (PK/FK) |
|  * Tables: members, membership_plans, memberships, trainers, assignments, attendance  |
|  * Storage Engine: MySQL 8.x / SQLite 3 Embedded (gym_management.db)                  |
+-------------------------------------------------------+-------------------------------+
                                                        |
                                                (Database Connector)
                                                        v
+---------------------------------------------------------------------------------------+
|                     DATA SCIENCE & ANALYTICS PIPELINE (PYTHON 3.12)                   |
|  * Data Ingestion & Preprocessing (data_loader.py)                                    |
|  * Attendance Trends & Participation Frequency (attendance_analysis.py)               |
|  * Membership Plan Popularity & Status Breakdown (membership_analysis.py)             |
|  * Trainer Workload Capacity & Balancing (trainer_analysis.py)                        |
|  * Master 6-Panel Executive Dashboard (comprehensive_eda.py)                          |
+---------------------------------------------------------------------------------------+
                                                        |
                                              (Visualizations & Reports)
                                                        v
+---------------------------------------------------------------------------------------+
|                                   DECISION DASHBOARDS                                 |
|  [Line Charts] [Bar Charts] [Pie Charts] [Histograms] [Donut Plots] [Execution Logs]  |
+---------------------------------------------------------------------------------------+
```

---

## 3. Four Subject-Wise Folder Organization

```
d:\gym management\
│
├── README.md                               <-- Root Project Documentation
├── gym_management.db                       <-- Relational Database File
│
├── Software Engineering\                   <-- FOLDER 1: SOFTWARE ENGINEERING (25ITT33)
│   ├── Software_Requirements_Specification.md  <-- Formal IEEE 830 SRS Document
│   ├── Functional_and_Non_Functional_Requirements.md
│   ├── Testing_Techniques_and_Test_Cases.md    <-- Verification & Validation (17 Test Cases)
│   └── diagrams\
│       ├── system_architecture_diagram.jpg
│       ├── use_case_diagram.jpg
│       ├── class_diagram.jpg
│       ├── dfd_level_0.jpg
│       ├── dfd_level_1.jpg
│       ├── sequence_diagram.jpg
│       ├── activity_diagram.jpg
│       ├── state_transition_diagram.png
│       ├── state_transition_diagram.md
│       └── README.md
│
├── Database Management System\             <-- FOLDER 2: DATABASE MANAGEMENT SYSTEMS (25ITT31)
│   ├── Relational_Schema.md                <-- Relational Schema & Data Dictionary
│   ├── Normalization_Document.md           <-- Formal 1NF, 2NF, 3NF Normalization
│   ├── gym_management_schema.sql           <-- Table Creation, PK, FK, CHECK Constraints
│   ├── sample_data.sql                     <-- Seed Data (Members, Plans, Attendance, Trainers)
│   ├── queries.sql                         <-- CRUD, Joins, Aggregations, Revenue & Footfall Reports
│   ├── execute_sql.py                      <-- Python Database Engine & Report Generator
│   ├── run_create_database.bat             <-- [BATCH 1] Double-click to create DB
│   ├── run_insert_records.bat              <-- [BATCH 2] Double-click to insert records
│   ├── run_generate_reports.bat            <-- [BATCH 3] Double-click to generate reports
│   ├── diagrams\
│   │   ├── er_diagram.jpg                  <-- IMPORTANT: Placed in DBMS folder
│   │   └── er_diagram_documentation.md
│   └── outputs\
│       ├── sql_queries_output.txt          <-- Saved Output Text File
│       └── sql_execution_screenshot.png    <-- Program Execution Screenshot
│
├── Java Programming\                       <-- FOLDER 3: JAVA PROGRAMMING (25ITT32)
│   ├── src\com\gym\
│   │   ├── model\                          <-- OOP Models (Person, Member, Trainer, Plan, etc.)
│   │   ├── dao\                            <-- JDBC Data Access Objects (CRUD, Joins, Summaries)
│   │   ├── service\                        <-- Business Services & Workflow Orchestration
│   │   ├── util\                           <-- DBConnection (Singleton), Validation, Exceptions
│   │   └── app\                            <-- Application Entrypoints (GymApp, Member, Attendance)
│   ├── bin\                                <-- Compiled Java Bytecode (.class)
│   ├── lib\                                <-- JDBC Drivers (sqlite-jdbc, mysql-connector-j, slf4j)
│   ├── run_member_management.bat           <-- [BATCH 1] Double-click to run Member Management
│   ├── run_membership_management.bat       <-- [BATCH 2] Double-click to run Membership & Renewals
│   ├── run_attendance_management.bat       <-- [BATCH 3] Double-click to run Attendance Tracking
│   ├── outputs\
│   │   ├── member_management_output.txt
│   │   ├── membership_management_output.txt
│   │   └── attendance_management_output.txt
│   └── screenshots\
│       ├── member_management_execution.png
│       ├── membership_management_execution.png
│       └── attendance_management_execution.png
│
└── Foundation of Data Science\             <-- FOLDER 4: FOUNDATION OF DATA SCIENCE (25ITC31)
    ├── data_loader.py                      <-- Database Extraction, Cleaning & CSV Pipeline
    ├── attendance_analysis.py              <-- Time Series & Participation Analysis
    ├── membership_analysis.py              <-- Plan Popularity & Subscription Expiry Analysis
    ├── trainer_analysis.py                 <-- Trainer Capacity & Workload Balance
    ├── comprehensive_eda.py                <-- Master 6-Panel Executive Dashboard
    ├── generate_execution_screenshots.py   <-- Terminal Screenshot Generator Utility
    ├── run_attendance_analysis.bat         <-- [BATCH 1] Double-click to run Attendance EDA
    ├── run_membership_analysis.bat         <-- [BATCH 2] Double-click to run Membership EDA
    ├── run_trainer_analysis.bat            <-- [BATCH 3] Double-click to run Trainer EDA
    ├── data\                               <-- Cleaned Extracted Datasets (CSV)
    │   ├── clean_members.csv
    │   ├── clean_plans.csv
    │   ├── clean_memberships.csv
    │   ├── clean_trainers.csv
    │   ├── clean_assignments.csv
    │   └── clean_attendance.csv
    ├── outputs\
    │   ├── attendance_analysis_output.txt
    │   ├── membership_analysis_output.txt
    │   └── trainer_analysis_output.txt
    ├── screenshots\
    │   ├── attendance_analysis_execution.png
    │   ├── membership_analysis_execution.png
    │   └── trainer_analysis_execution.png
    └── visualizations\                     <-- 9 Publication-Grade Analytical Charts
        ├── daily_monthly_attendance_trends.png
        ├── member_participation_analysis.png
        ├── peak_hours_analysis.png
        ├── membership_plan_popularity.png
        ├── active_vs_expired_memberships.png
        ├── membership_revenue_by_plan.png
        ├── trainer_workload_analysis.png
        ├── trainer_specialization_distribution.png
        └── gym_analytics_dashboard.png
```

---

## 4. Technologies & Tools Used

| Subject Domain | Technologies & Libraries | Key Concepts Applied |
| :--- | :--- | :--- |
| **Software Engineering** | IEEE 830-1998, UML 2.5, Mermaid.js, Markdown | Waterfall/Iterative Lifecycle, Requirements Elicitation, RTM, Black-Box & White-Box Testing |
| **Database Management** | ANSI SQL, MySQL 8.x, SQLite 3 | E-R Modeling, Relational Schema, 3NF Normalization, Indexing, ACID, Joins, Aggregates, Reports |
| **Java Programming** | Java SE 17 LTS, JDBC 4.2, SQLite/MySQL Connectors | Classes & Objects, Inheritance (`Person -> Member, Trainer`), Encapsulation, Polymorphism, Exceptions, Collections |
| **Foundation of Data Science**| Python 3.12, Pandas, Matplotlib, Seaborn, NumPy, Pillow | ETL Pipeline, Data Cleaning, Outlier Handling, Descriptive Statistics, Line/Bar/Pie/Histograms, EDA |

---

## 5. Execution Guide & Interactive Keyboard Testing

All 9 `.bat` files are configured to support **both Step-by-Step Interactive Manual Keyboard Input** and **Automated Verification**:

### 5.1 Database Management System Folder (`Database Management System\`)
Double-click:
1. **`run_create_database.bat`**: Prompts for confirmation to create/reset the database tables.
2. **`run_insert_records.bat`**: Interactive Menu:
   - `[1]` Insert Default Sample Records (15 Members, 4 Plans, 72 Footfalls)
   - `[2]` Manually Add New Member via Keyboard (Type Name, Age, Phone, Email)
   - `[3]` Manually Add New Membership Plan via Keyboard
   - `[4]` Manually Add New Trainer via Keyboard
   - `[5]` View Current Members Table
3. **`run_generate_reports.bat`**: Interactive Menu:
   - `[1-8]` View specific queries (Roster, Joins, Revenues, Status, Workloads)
   - `[9]` Execute any custom SQL query typed from keyboard
   - `[10]` Run all reports & save to `outputs\sql_queries_output.txt`

### 5.2 Java Programming Folder (`Java Programming\`)
Double-click:
1. **`run_member_management.bat`**: Interactive Menu:
   - `[1]` View All Registered Members (Roster)
   - `[2]` Add New Member (Type Name, Age, Phone, Email via keyboard with live validation)
   - `[3]` Search Member by ID
   - `[4]` Update Member Details
   - `[5]` Run Automated Verification & Export Output
2. **`run_membership_management.bat`**: Interactive Menu:
   - `[1]` View Available Membership Plans & Pricing
   - `[2]` Subscribe Member to Plan (Type Member ID & Plan ID)
   - `[3]` View Memberships Filtered by Status (Active, Expired, Expiring Soon)
   - `[4]` Process Membership Renewal (Type Member ID & New Plan ID)
   - `[5]` View Financial Revenue Report by Plan Tier
   - `[6]` Add New Plan Tier via Keyboard
3. **`run_attendance_management.bat`**: Interactive Menu:
   - `[1]` Record Member Check-In (Type Member ID; checks subscription validity)
   - `[2]` Record Member Check-Out (Type Attendance Log ID; calculates duration)
   - `[3]` View Recent Attendance Logs (Custom row count)
   - `[4]` View Attendance Operational Metrics Summary
   - `[5]` Test Check-In Access Control (Verify expired subscription rejection)

### 5.3 Foundation of Data Science Folder (`Foundation of Data Science\`)
Double-click:
1. **`run_attendance_analysis.bat`**: Interactive Menu:
   - `[1]` View Attendance Descriptive Statistics (Mean, Median, Std Dev)
   - `[2]` View Monthly Footfall Table
   - `[3]` View Top Active Members (Type custom top N from keyboard)
   - `[4]` Search Attendance Records by Member ID
   - `[5-7]` Generate Line Chart, Histogram, Peak Hours Bar Chart
   - `[8]` Run Full Automated Analysis & Save All Outputs
2. **`run_membership_analysis.bat`**: Interactive Menu:
   - `[1]` View Plan Popularity & Financial Contributions Table
   - `[2]` View Active vs. Expired vs. Expiring-Soon Statistics
   - `[3]` Search Member Subscription Details
   - `[4-6]` Generate Plan Bar Chart, Status Pie Chart, Revenue Bar Chart
   - `[7]` Run Full Automated Analysis & Save All Outputs
3. **`run_trainer_analysis.bat`**: Interactive Menu:
   - `[1]` View Trainer Workload & Client Capacity Table
   - `[2]` View Workload Descriptive Metrics
   - `[3]` Search Assigned Members for Specific Trainer ID
   - `[4-5]` Generate Workload Bar Chart & Specialization Donut Chart
   - `[6]` Run Full Automated Analysis & Save All Outputs

---

## 6. Generated Visualizations Overview

| Chart Title | File Name | Chart Type | Insights Derived |
| :--- | :--- | :---: | :--- |
| **Attendance Trends** | `daily_monthly_attendance_trends.png` | Line Chart | Footfall progression from Jan to Nov 2026 showing highest peak in November (10 visits). |
| **Member Participation** | `member_participation_analysis.png` | Histogram | Frequency distribution of member visit counts, showing core consistent trainees vs. casual visitors. |
| **Peak Check-in Hours** | `peak_hours_analysis.png` | Bar Chart | Identifies morning rush (06:00 - 08:00) with 60% of daily gym attendance. |
| **Plan Popularity** | `membership_plan_popularity.png` | Bar Chart | Highlights 'Pro Athlete' (7 members) and 'Elite VIP' (5 members) as dominant tiers. |
| **Membership Status** | `active_vs_expired_memberships.png` | Pie Chart | Visualizes 52.9% Active, 35.3% Expired, and 11.8% Expiring Soon for renewal targeting. |
| **Plan Revenue** | `membership_revenue_by_plan.png` | Horiz. Bar | Shows 'Elite Annual VIP' contributing Rs. 62,500 (48.8% of total gym revenue). |
| **Trainer Workload** | `trainer_workload_analysis.png` | Bar Chart | Compares active vs. historical clients, confirming no trainer exceeds the 5-client capacity threshold. |
| **Specialization Breakdown**| `trainer_specialization_distribution.png`| Donut Chart | Equal distribution across Strength, Functional HIIT, Yoga, Rehab, and Aerobics. |
| **Executive Dashboard** | `gym_analytics_dashboard.png` | 6-Panel Multi-plot | Comprehensive management overview unifying all operational and analytical metrics. |

---

## 7. Syllabus Compliance Matrix

| Syllabus Requirement | Project Deliverable | Location in Project | Status |
| :--- | :--- | :--- | :---: |
| **SRS Document** | IEEE 830-1998 formatted SRS | `Software Engineering/Software_Requirements_Specification.md` | **COMPLETED** |
| **Functional & Non-Functional** | Complete specification | `Software Engineering/Functional_and_Non_Functional_Requirements.md`| **COMPLETED** |
| **Use Case Diagram** | Actor interactions with `include`/`extend` | `Software Engineering/diagrams/use_case_diagram.jpg` | **COMPLETED** |
| **Activity Diagram** | System control and decision flow | `Software Engineering/diagrams/activity_diagram.jpg` | **COMPLETED** |
| **Class Diagram** | Static model with attributes & methods | `Software Engineering/diagrams/class_diagram.jpg` | **COMPLETED** |
| **DFD Level 0 & Level 1** | Context and Level 1 decomposition | `Software Engineering/diagrams/dfd_level_0.jpg`, `dfd_level_1.jpg` | **COMPLETED** |
| **Architecture Diagram** | 3-Tier system architecture | `Software Engineering/diagrams/system_architecture_diagram.jpg` | **COMPLETED** |
| **Sequence Diagram** | Chronological messaging sequence | `Software Engineering/diagrams/sequence_diagram.jpg` | **COMPLETED** |
| **State Transition Diagram** | Lifecycle finite state machine | `Software Engineering/diagrams/state_transition_diagram.png` | **COMPLETED** |
| **Testing Techniques & Test Cases**| 17 black-box & white-box test cases | `Software Engineering/Testing_Techniques_and_Test_Cases.md` | **COMPLETED** |
| **E-R Diagram (DBMS Folder)** | Entity sets, cardinalities, keys | `Database Management System/diagrams/er_diagram.jpg` | **COMPLETED** |
| **Relational Schema** | Schema notation and data dictionary | `Database Management System/Relational_Schema.md` | **COMPLETED** |
| **Normalization (1NF, 2NF, 3NF)**| Functional dependency analysis | `Database Management System/Normalization_Document.md` | **COMPLETED** |
| **SQL Table Creation & Seeds** | ANSI SQL scripts with constraints | `Database Management System/gym_management_schema.sql`, `sample_data.sql` | **COMPLETED** |
| **SQL Queries & Reports** | Joins, aggregations, revenue reports | `Database Management System/queries.sql`, `execute_sql.py` | **COMPLETED** |
| **Java OOP Implementation** | Classes, Inheritance, Polymorphism | `Java Programming/src/com/gym/model/*.java` | **COMPLETED** |
| **Java Exception Handling** | Custom exceptions and validation | `Java Programming/src/com/gym/util/GymException.java` | **COMPLETED** |
| **JDBC Database Connectivity**| Connection manager & DAOs | `Java Programming/src/com/gym/util/DBConnection.java`, `dao/*.java` | **COMPLETED** |
| **Python Data Science Retrieval**| Database connector & preprocessing | `Foundation of Data Science/data_loader.py` | **COMPLETED** |
| **Python Visualizations** | Matplotlib line, bar, pie, hist | `Foundation of Data Science/*.py`, `visualizations/*.png` | **COMPLETED** |
| **Runnable Batch Files** | 9 one-click `.bat` scripts | 3 in DBMS, 3 in Java, 3 in Data Science | **COMPLETED** |
| **Text Outputs & Screenshots** | Outputs & console screenshots | Available across all three programming folders | **COMPLETED** |
