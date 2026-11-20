# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
## For Gym Membership Management and Fitness Activity Analysis System
### Scenario 27 — Velalar College of Engineering and Technology (Autonomous)
**Academic Year:** 2026 - 2027 (ODD)  
**Department:** Information Technology  
**Course Code & Name:** 25ITT33 – Software Engineering  
**Standard:** IEEE 830-1998 Recommended Practice for Software Requirements Specifications  

---

## TABLE OF CONTENTS
1. [Introduction](#1-introduction)
   - 1.1 Purpose
   - 1.2 Document Conventions
   - 1.3 Intended Audience & Reading Suggestions
   - 1.4 Project Scope
   - 1.5 References
2. [Overall Description](#2-overall-description)
   - 2.1 Product Perspective
   - 2.2 Product Functions
   - 2.3 User Classes and Characteristics
   - 2.4 Operating Environment
   - 2.5 Design and Implementation Constraints
   - 2.6 User Documentation
   - 2.7 Assumptions and Dependencies
3. [External Interface Requirements](#3-external-interface-requirements)
   - 3.1 User Interfaces
   - 3.2 Hardware Interfaces
   - 3.3 Software Interfaces
   - 3.4 Communications Interfaces
4. [System Features & Functional Requirements](#4-system-features--functional-requirements)
   - 4.1 Member Lifecycle Management
   - 4.2 Membership Plan Administration
   - 4.3 Membership Registration & Subscription Engine
   - 4.4 Real-Time Attendance Check-In / Check-Out
   - 4.5 Fitness Trainer Management
   - 4.6 Member-Trainer Assignment & Workload Balancing
   - 4.7 Membership Expiry & Lifecycle Status Tracking
   - 4.8 Membership Renewal & Extension
   - 4.9 Reporting Engine (Revenue, Attendance, Renewals)
   - 4.10 Python Fitness Activity EDA & Visual Analytics
5. [Non-Functional Requirements](#5-non-functional-requirements)
   - 5.1 Performance Requirements
   - 5.2 Safety and Reliability Requirements
   - 5.3 Security Requirements
   - 5.4 Software Quality Attributes (Availability, Maintainability, Portability)
   - 5.5 Business Rules
6. [Design Models & Syllabus Alignment](#6-design-models--syllabus-alignment)
   - 6.1 Requirements Engineering Life Cycle
   - 6.2 Architectural Style
   - 6.3 Traceability Matrix

---

## 1. INTRODUCTION

### 1.1 Purpose
This Software Requirements Specification (SRS) document details the functional, operational, performance, and interface requirements for the **Gym Membership Management and Fitness Activity Analysis System**. This system resolves the inefficiencies, record loss, and manual errors inherent in traditional paper-based and spreadsheet gym management by providing an automated Java-based transactional engine coupled with a relational database and a Python-powered data science analysis pipeline.

### 1.2 Document Conventions
- **IEEE Std 830-1998** formatting standards are applied.
- Priority levels: `[High]`, `[Medium]`, `[Low]`.
- Requirement identifiers follow the taxonomy: `FR-<Category>-<Number>` for Functional Requirements and `NFR-<Category>-<Number>` for Non-Functional Requirements.

### 1.3 Intended Audience & Reading Suggestions
This document is targeted toward:
- **Academic Evaluators & Instructors:** To verify syllabus coverage according to Anna University / Autonomous Curriculum (Software Engineering, DBMS, Java, Foundations of Data Science).
- **Software Engineers & Developers:** To guide implementation of Java classes, JDBC layers, and Python visualization scripts.
- **Database Administrators (DBA):** To review entity relational integrity, 3NF normalization, and query optimization.
- **End-Users (Gym Administrators, Trainers):** To understand user workflows, validation rules, and generated visual reports.

### 1.4 Project Scope
The system provides end-to-end management for modern fitness clubs, covering:
1. Member registration, profiling, and lifecycle tracking.
2. Tiered membership plans with custom duration, pricing, and facility privileges.
3. Daily attendance logging with precise timestamps and duration calculation.
4. Trainer assignments based on specialized fitness requirements (Cardio, Strength, HIIT, Yoga).
5. Automated status tracking (`Active`, `Expired`, `Expiring Soon`).
6. Financial revenue aggregation and operational attendance summaries.
7. Advanced data preprocessing, exploratory data analysis (EDA), and graphical visualization using Python (Pandas, Matplotlib, Seaborn).

### 1.5 References
- IEEE Std 830-1998: *IEEE Recommended Practice for Software Requirements Specifications*.
- Pressman, R. S., & Maxim, B. R., *Software Engineering: A Practitioner's Approach*, 9th Edition, McGraw-Hill.
- Elmasri, R., & Navathe, S. B., *Fundamentals of Database Systems*, 7th Edition, Pearson.
- Schildt, H., *Java: The Complete Reference*, 12th Edition, Oracle Press.
- McKinney, W., *Python for Data Analysis*, 3rd Edition, O'Reilly Media.
- Velalar College of Engineering and Technology, Autonomous IT Curriculum: 25ITT33 (SE), 25ITT31 (DBMS), 25ITT32 (Java), 25ITC31 (FDS).

---

## 2. OVERALL DESCRIPTION

### 2.1 Product Perspective
The Gym Management System is a self-contained, three-tier software suite consisting of:
1. **Presentation & Application Layer (Java):** Object-oriented console and menu-driven desktop user interface with comprehensive validation and exception handling.
2. **Data Persistence Layer (DBMS):** Relational database storing normalized tables with referential integrity constraints.
3. **Data Science & Analytics Layer (Python):** Decoupled analytical engine that reads historical gym records via database connectors, performs ETL/data cleaning, and outputs high-resolution analytical plots.

### 2.2 Product Functions
```
+---------------------------------------------------------------------------------+
|              Gym Membership Management & Fitness Activity System                |
+---------------------------------------+-----------------------------------------+
|        Administrative & Operations    |         Data Analytics & Insights       |
+---------------------------------------+-----------------------------------------+
| 1. Member Registration & Profile      | 1. Daily/Monthly Attendance Trends      |
| 2. Membership Plan Configuration      | 2. Plan Popularity Distribution         |
| 3. Subscription & Renewal Management  | 3. Membership Expiry Ratio (Pie Chart)  |
| 4. Attendance Check-in / Check-out    | 4. Trainer Workload Balance             |
| 5. Trainer Profile & Assignment       | 5. Member Visit Frequency Histogram     |
| 6. Revenue & Operational Reports      | 6. Peak Hours & Duration Insights       |
+---------------------------------------+-----------------------------------------+
```

### 2.3 User Classes and Characteristics
1. **Gym Administrator:** Highly privileged user responsible for member registration, plan pricing, trainer allocation, and overall revenue auditing.
2. **Fitness Trainer:** Operational user accessing assigned member rosters, workout schedules, and attendance histories.
3. **Gym Member:** End-user viewing personal membership validity, attendance logs, and assigned trainer information.

### 2.4 Operating Environment
- **Operating System:** Microsoft Windows 10/11, Linux (Ubuntu 20.04+), macOS.
- **Java Runtime:** Java SE Development Kit (JDK) 11 / 17 / 21 LTS.
- **Python Environment:** Python 3.10+ with `pandas`, `matplotlib`, `seaborn`, `sqlite3`, and `mysql-connector-python`.
- **Database Engine:** MySQL Server 8.0+ / SQLite 3.x embedded.

### 2.5 Design and Implementation Constraints
- Compliance with Object-Oriented Programming (OOP) principles: Inheritance, Polymorphism, Encapsulation, and Abstraction.
- Adherence to Third Normal Form (3NF) in relational schema design to eliminate update, insertion, and deletion anomalies.
- Robust exception handling in Java preventing unexpected process crashes during invalid user input or database disconnection.
- Pure parameter-driven batch files (`.bat`) providing automated double-click execution for college demonstration.

### 2.6 Assumptions and Dependencies
- Members possess unique personal identifiers (email or phone).
- System clock on the host computer provides valid local date and time stamps.
- Host machine has permissions to write `.txt` and `.png` output files to designated directories.

---

## 3. EXTERNAL INTERFACE REQUIREMENTS

### 3.1 User Interfaces
- Clean, structured command-line interactive menu with formatted ANSI tables and ASCII banners.
- Clear numeric selections (1 to N) with input prompts, breadcrumb navigation, and confirmation dialogs.
- Clear error dialogues indicating invalid date formats, out-of-range numerical values, or nonexistent IDs.

### 3.2 Hardware Interfaces
- Standard x86-64 Architecture PC.
- Minimum 2 GB RAM (4 GB recommended for data science visualization).
- Minimum 500 MB free hard drive space for database files, runtime logs, and generated graphical charts.

### 3.3 Software Interfaces
- **JDBC Driver:** Type-4 Pure Java JDBC driver connecting Java services to the relational database.
- **Python-Database Connector:** Python DB-API 2.0 interface (`sqlite3` / `mysql.connector`) extracting relational data directly into Pandas DataFrames.
- **Operating System Shell:** Windows Command Prompt (`cmd.exe`) and PowerShell supporting `.bat` script triggers.

### 3.4 Communications Interfaces
- Local IPC (Inter-Process Communication) and TCP/IP loopback sockets (`localhost:3306`) for database client-server communication.

---

## 4. SYSTEM FEATURES & FUNCTIONAL REQUIREMENTS

### 4.1 Member Lifecycle Management
- **Description:** Enables administrators to capture and maintain member records.
- **Inputs:** `name` (String), `age` (Integer >= 14), `contact_no` (10-digit String), `registration_date` (Date).
- **Processing:** Validates fields, generates auto-incrementing `member_id`, stores into `members` table.
- **Outputs:** Member record confirmation, formatted member detail cards, searchable member rosters.

### 4.2 Membership Plan Administration
- **Description:** Allows definition of subscription plans with varied perks.
- **Inputs:** `plan_name`, `duration` (in months, positive integer), `fee` (decimal > 0), `facilities` (text).
- **Processing:** Persists plan to database, recalculates pricing models, prevents duplicate plan naming.
- **Outputs:** List of available plans, plan cost breakdown.

### 4.3 Membership Registration & Subscription Engine
- **Description:** Links a member with a specific plan and calculates valid period.
- **Inputs:** `member_id`, `plan_id`, `start_date`.
- **Processing:** Queries plan duration, sets `expiry_date = start_date + duration`, sets status = `Active`.
- **Outputs:** Generated `membership_id`, subscription receipt with explicit expiry date.

### 4.4 Real-Time Attendance Check-In / Check-Out
- **Description:** Logs physical member presence at the gym facility.
- **Inputs:** `member_id`, current timestamp.
- **Processing:** Verifies active membership status. If valid, logs `check_in_time`. On leaving, logs `check_out_time` and computes elapsed workout minutes.
- **Outputs:** Attendance confirmation, active workout counter, violation warning if membership is expired.

### 4.5 Fitness Trainer Management
- **Description:** Maintains profiles of certified fitness instructors.
- **Inputs:** `trainer_name`, `specialization` (Cardio, Strength, Crossfit, Yoga), `contact_no`.
- **Processing:** Inserts and indexes trainer in database.
- **Outputs:** Trainer directory with assigned specialization.

### 4.6 Member-Trainer Assignment & Workload Balancing
- **Description:** Allocates members to trainers based on fitness focus.
- **Inputs:** `member_id`, `trainer_id`.
- **Processing:** Inserts assignment record with timestamp. Tracks count of active members per trainer.
- **Outputs:** Trainer assignment roster, workload distribution report.

### 4.7 Membership Expiry & Lifecycle Status Tracking
- **Description:** Dynamic evaluation of subscription states.
- **Inputs:** Current system date compared against `expiry_date`.
- **Processing:** 
  - If `current_date > expiry_date` => `Expired`
  - If `0 <= (expiry_date - current_date) <= 7 days` => `Expiring Soon`
  - If `current_date <= expiry_date` => `Active`
- **Outputs:** Segmented lists for administrative follow-up.

### 4.8 Membership Renewal & Extension
- **Description:** Facilitates subscription renewal for expired or expiring members.
- **Inputs:** `member_id`, new or recurring `plan_id`.
- **Processing:** Updates or inserts new membership record, advancing `start_date` and `expiry_date`.
- **Outputs:** Renewal confirmation, updated revenue figures.

### 4.9 Reporting Engine
- **Description:** Computes operational and financial statistics via SQL aggregations.
- **Outputs:**
  - Total membership revenue categorized by plan.
  - Monthly attendance summaries and footfall averages.
  - Trainer member allocation roster.
  - Complete renewal history.

### 4.10 Python Fitness Activity EDA & Visual Analytics
- **Description:** Performs automated statistical analysis and plotting.
- **Inputs:** Relational database tables exported to Pandas DataFrames.
- **Processing:** Data cleaning, handling nulls, aggregation, group-by operations, time-series plotting.
- **Outputs:** High-resolution PNG charts:
  1. Attendance Trends (Line chart)
  2. Plan Popularity (Bar chart)
  3. Membership Status Distribution (Pie chart)
  4. Trainer Workload (Bar chart)
  5. Member Participation Frequency (Histogram)

---

## 5. NON-FUNCTIONAL REQUIREMENTS

| Category | Identifier | Metric / Target Specification |
| :--- | :--- | :--- |
| **Performance** | NFR-PERF-01 | SQL queries execute in < 100 ms for 10,000 records. |
| **Performance** | NFR-PERF-02 | Python chart rendering pipeline completes in < 3.0 s. |
| **Reliability** | NFR-REL-01 | Zero transaction data loss via atomic database commits. |
| **Security** | NFR-SEC-01 | Parameterized queries prevent 100% of SQL Injection attacks. |
| **Maintainability** | NFR-MNT-01 | Layered MVC/DAO architecture with > 80% code modularity. |
| **Portability** | NFR-PRT-01 | 100% runnable on both Windows (`.bat`) and Unix environments. |

---

## 6. DESIGN MODELS & SYLLABUS ALIGNMENT
The software development process followed conforms to the **Prescriptive Waterfall / Iterative Model** outlined in Unit 1 of 25ITT33:
1. **Requirements Elicitation & Analysis (Unit 2):** Documented in this SRS and RTM.
2. **Software Design (Unit 3):** Reflected in Class Diagram, Use Case Diagram, DFD Levels 0 & 1, Sequence Diagram, and Activity Diagram.
3. **Software Testing (Unit 4):** Reflected in the formal Verification and Validation Test Suite.
