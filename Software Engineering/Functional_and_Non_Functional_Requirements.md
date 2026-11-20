# Functional and Non-Functional Requirements Specification
## Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
**Academic Year:** 2026 - 2027 (ODD)  
**Course:** 25ITT33 - Software Engineering  
**Department:** Information Technology, Velalar College of Engineering and Technology, Erode - 12  

---

## 1. Introduction
The **Gym Membership Management and Fitness Activity Analysis System** is an enterprise-grade integrated application engineered to automate administrative operations, track daily fitness participation, manage trainer workloads, and synthesize descriptive and exploratory data analytics for fitness club operations.

---

## 2. Functional Requirements (FR)

### FR-01: Member Lifecycle Management
* **FR-1.1:** The system shall allow the gym administrator to register new members with unique identifiers (`member_id`), full name, age, contact telephone number, email, and registration date.
* **FR-1.2:** The system shall validate member contact numbers for format compliance (10 digits) and age boundaries (e.g., minimum 14 years).
* **FR-1.3:** The system shall provide search, update, and deactivation/archival capabilities for member records.
* **FR-1.4:** The system shall list all registered members in tabular formats with sorting by member ID, name, or joining date.

### FR-02: Membership Plan Management
* **FR-2.1:** The system shall maintain predefined and custom membership plans with attributes: `plan_id`, `plan_name`, `duration` (in months or days), `fee` (in currency units), and comprehensive list of `facilities` offered (e.g., Cardio, Weight Training, Swimming, Sauna, Crossfit).
* **FR-2.2:** The administrator shall have privileges to add new membership tiers, update subscription pricing, and adjust facility inclusions.
* **FR-2.3:** The system shall validate that no negative duration or negative fee amounts are registered.

### FR-03: Membership Registration and Subscription
* **FR-3.1:** The system shall map an active gym member to an available membership plan, recording `membership_id`, `member_id`, `plan_id`, `start_date`, `expiry_date`, and initial status (`Active`).
* **FR-3.2:** The system shall automatically compute `expiry_date` using the selected plan duration added to the `start_date`.
* **FR-3.3:** The system shall prevent overlapping active memberships for the same member unless explicitly renewed as an upcoming subscription.

### FR-04: Attendance Tracking and Check-In/Check-Out
* **FR-4.1:** The system shall record member physical attendance with `attendance_id`, `member_id`, `attendance_date`, `check_in_time`, and `check_out_time`.
* **FR-4.2:** The system shall verify that check-out time is chronologically later than check-in time and compute duration spent on premises.
* **FR-4.3:** The system shall issue warnings if a member attempts to check in when their membership status is `Expired`.
* **FR-4.4:** The system shall allow automated timestamp generation based on system clock or manual administrative entry.

### FR-05: Trainer Profile Management
* **FR-5.1:** The system shall maintain certified fitness trainer profiles with `trainer_id`, `name`, `specialization` (e.g., Strength & Conditioning, Yoga, Bodybuilding, Aerobics, Functional Rehab), and `contact_no`.
* **FR-5.2:** The system shall allow creation, modification, and status monitoring of fitness trainers.

### FR-06: Trainer-Member Assignment
* **FR-6.1:** The system shall link members to qualified trainers based on the member's fitness objectives and trainer specialization.
* **FR-6.2:** The system shall track `assignment_id`, `member_id`, `trainer_id`, and `assigned_date`.
* **FR-6.3:** The system shall compute individual trainer workload (number of assigned members) to prevent overburdening and ensure quality instruction.

### FR-07: Membership Status Tracking and Alerts
* **FR-7.1:** The system shall dynamically categorize all memberships into three states:
  * **Active:** Current date is between `start_date` and `expiry_date`.
  * **Expiring Soon:** Membership expiry date falls within a configurable window (e.g., next 7 days).
  * **Expired:** Current date has exceeded `expiry_date`.
* **FR-7.2:** The system shall surface expiring soon memberships prominently for proactive renewal outreach.

### FR-08: Membership Renewal Processing
* **FR-8.1:** The system shall process membership renewals by extending the active subscription or assigning a new plan starting from the day following prior expiration.
* **FR-8.2:** The system shall archive previous membership records to preserve historical subscription records.

### FR-09: Financial and Operational Report Generation
* **FR-9.1:** The system shall calculate total, plan-wise, and periodic membership revenues.
* **FR-9.2:** The system shall generate comprehensive attendance summaries including total footfalls, average visit duration, and peak workout hours.
* **FR-9.3:** The system shall produce trainer distribution rosters and renewal transaction logs.

### FR-10: Fitness Centre Data Science Analytics & Visualizations
* **FR-10.1:** The system shall interface with the database via Python database connectors to extract attendance, member, plan, and trainer datasets.
* **FR-10.2:** The system shall preprocess raw data by handling null values, type casting dates, and calculating derived statistics.
* **FR-10.3:** The system shall generate publication-grade statistical charts:
  * Daily and monthly attendance trends (Line Chart)
  * Membership plan popularity (Bar Chart)
  * Active vs. Expired vs. Expiring-Soon status ratio (Pie Chart)
  * Trainer workload distribution (Bar Chart)
  * Member participation frequency distribution (Histogram / Density plot)

---

## 3. Non-Functional Requirements (NFR)

### NFR-01: Performance & Response Time
* **NFR-1.1:** Response time for standard database CRUD operations (Member registration, Attendance logging) shall not exceed 1.0 second under normal operating conditions.
* **NFR-1.2:** Python statistical aggregation and chart generation pipelines shall complete execution within 3.0 seconds for datasets up to 10,000 records.
* **NFR-1.3:** The Java desktop console/GUI shall launch in under 2.5 seconds on standard workstations.

### NFR-02: Reliability & Data Integrity
* **NFR-2.1:** All relational database transactions shall adhere strictly to ACID properties (Atomicity, Consistency, Isolation, Durability).
* **NFR-2.2:** Foreign key constraints shall prevent orphaned records across memberships, attendances, and trainer assignments.
* **NFR-2.3:** The system shall maintain 99.9% uptime during facility operational hours (05:00 to 23:00).

### NFR-03: Security & Authorization
* **NFR-3.1:** Role-Based Access Control (RBAC) shall enforce distinct privileges for Gym Administrators, Trainers, and Members.
* **NFR-3.2:** Member sensitive personally identifiable information (contact numbers, emails) shall be protected against unauthorized disclosure.
* **NFR-3.3:** Database connection credentials shall be externalized in configuration properties and parameterized SQL queries shall prevent SQL Injection vulnerabilities.

### NFR-04: Usability & User Experience
* **NFR-4.1:** The console and graphical interfaces shall feature intuitive numeric and command-driven navigation with immediate validation feedback.
* **NFR-4.2:** Data visualizations generated by Python shall utilize high-contrast color palettes, legible typography, gridlines, legends, and clear axis labels for presentations.
* **NFR-4.3:** Clear human-readable error messages shall be presented whenever invalid input or constraint violations occur.

### NFR-05: Maintainability & Modularity
* **NFR-5.1:** Java code shall adhere to Object-Oriented Design Principles (SOLID) with clean separation of concerns into Model, DAO, Service, Util, and Application layers.
* **NFR-5.2:** Python scripts shall be structured into modular functions covering extraction, cleaning, feature engineering, and visualization routines.
* **NFR-5.3:** Comprehensive code comments, Javadoc annotations, and docstrings shall accompany all classes and functions.

### NFR-06: Portability & Cross-Platform Compatibility
* **NFR-6.1:** The Java runtime components shall execute without platform modification on JDK 8, 11, 17, or 21 on Windows, Linux, and macOS.
* **NFR-6.2:** Batch files (`.bat`) and cross-platform execution instructions shall enable one-click execution on Windows workstations.
* **NFR-6.3:** The database architecture shall be ANSI SQL compliant, compatible with MySQL 8.x, MariaDB, and SQLite3.

---

## 4. Requirements Traceability Matrix (RTM)

| Requirement ID | Description | Architectural Component | Verification Method |
| :--- | :--- | :--- | :--- |
| **FR-01** | Member Details Management | `com.gym.dao.MemberDAO`, `Member.java` | Unit & Integration Test |
| **FR-02** | Membership Plans Management | `com.gym.dao.PlanDAO`, `MembershipPlan.java` | Unit Test |
| **FR-03** | Membership Registration | `com.gym.service.MembershipService` | System Test |
| **FR-04** | Attendance Recording | `com.gym.dao.AttendanceDAO`, `Attendance.java` | Validation Test |
| **FR-05** | Trainer Management | `com.gym.dao.TrainerDAO`, `Trainer.java` | Unit Test |
| **FR-06** | Trainer Assignment & Workload | `com.gym.service.TrainerAssignmentService` | Calculation Test |
| **FR-07** | Membership Expiry Status | `com.gym.service.MembershipService` | Automated Business Logic Test |
| **FR-08** | Renewal Workflow | `com.gym.service.MembershipService` | Boundary Value Test |
| **FR-09** | SQL Reports & Summaries | SQL Scripts, Java Reporting Utility | Database Query Audit |
| **FR-10** | Python EDA & Visualizations | `Foundation of Data Science/*.py` | Visual Inspection & Data Audit |
| **NFR-01 - 06** | Quality, Performance, Security | Entire System Architecture | Benchmark & Security Audit |
