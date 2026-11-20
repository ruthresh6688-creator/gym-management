# Testing Techniques and Test Cases Document
## Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
**Academic Year:** 2026 - 2027 (ODD)  
**Course:** 25ITT33 - Software Engineering (Unit 4: Software Testing)  
**Department:** Information Technology, Velalar College of Engineering and Technology, Erode - 12  

---

## 1. Testing Strategy and Methodology

In accordance with the 25ITT33 Software Engineering syllabus (Unit 4), a structured verification and validation process was executed for the Gym Management and Fitness Analysis System. Both **Black-Box Testing** (functional validation without looking at internal logic) and **White-Box Testing** (structural path coverage) were performed across all system modules.

### 1.1 Levels of Testing
1. **Unit Testing:** Individual validation of core entities and data access objects (`MemberDAO`, `PlanDAO`, `AttendanceDAO`, `TrainerDAO`).
2. **Integration Testing:** Verification of inter-module data flow between Java business services and database persistence layers, and between SQL repositories and Python data pipelines.
3. **System Testing:** End-to-end operational execution of complete workflows (e.g., Member Registration -> Plan Assignment -> Daily Check-In/Check-Out -> Renewal -> Visual Reporting).
4. **Validation Testing:** Ensuring software complies with all client specifications stated in Scenario 27.

### 1.2 Black-Box Testing Techniques
- **Equivalence Class Partitioning (ECP):** Input domains (such as member age, plan duration, contact numbers) were split into valid and invalid partitions.
- **Boundary Value Analysis (BVA):** Testing boundary conditions (e.g., minimum age of 14, 0 vs 7 days for expiring soon, zero and negative plan fees).

### 1.3 White-Box Testing Techniques
- **Basis Path Testing:** Cyclomatic complexity calculated for membership status calculation and check-in validation methods to ensure 100% independent path coverage.
- **Exception Handling Coverage:** Testing database connection timeouts, SQL constraint violations, and invalid numeric conversions.

---

## 2. Test Cases and Execution Results

| Test Case ID | Test Scenario | Module / Component | Test Input Data | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-MEM-01** | Add new gym member with valid data | Member Management | Name: "Rajesh Kumar", Age: 26, Phone: "9876543210", Date: "2026-01-10" | Member successfully inserted with unique `member_id` | Member ID assigned and saved in database | **PASS** |
| **TC-MEM-02** | Add member with invalid age (< 14) | Member Management | Name: "Kavya", Age: 11, Phone: "9876543211" | System rejects with validation error "Age must be >= 14" | Input validation threw error; record rejected | **PASS** |
| **TC-MEM-03** | Add member with invalid phone number (< 10 digits) | Member Management | Name: "Vikram", Age: 29, Phone: "98765" | System rejects with validation error "Invalid 10-digit phone" | Input rejected; appropriate prompt displayed | **PASS** |
| **TC-PLN-01** | Create valid membership plan | Plan Management | Plan: "Pro Fitness", Duration: 6 months, Fee: 7500.00, Facilities: "Gym+Crossfit+Steam" | Plan record persisted to database with unique `plan_id` | Plan saved with generated `plan_id` | **PASS** |
| **TC-PLN-02** | Create plan with negative fee | Plan Management | Plan: "Free Trial", Duration: 1 month, Fee: -500.00 | System rejects input with "Fee cannot be negative" | Input rejected; prompt to re-enter valid fee | **PASS** |
| **TC-REG-01** | Register member to plan and compute expiry | Membership Module | Member ID: 1, Plan ID: 2 (3 Months), Start Date: "2026-01-01" | Membership created; `expiry_date` computed as "2026-04-01"; Status = "Active" | Start: 2026-01-01, Expiry: 2026-04-01, Status: Active | **PASS** |
| **TC-ATT-01** | Record valid attendance check-in and check-out | Attendance Module | Member ID: 1, Date: "2026-02-15", Check-In: "06:30:00", Check-Out: "07:45:00" | Attendance logged; duration computed as 75 minutes | Logged successfully; duration = 75 min | **PASS** |
| **TC-ATT-02** | Attempt check-in for expired member | Attendance Module | Member ID with expired subscription (Expiry: 2025-12-31) | System displays warning "Membership expired! Please renew before check-in" | Warning surfaced; prompt to renew membership | **PASS** |
| **TC-ATT-03** | Record check-out earlier than check-in | Attendance Module | Check-In: "09:00:00", Check-Out: "08:15:00" | System rejects entry with chronological order violation | Error reported: "Check-out time cannot precede check-in" | **PASS** |
| **TC-TRN-01** | Add new trainer details | Trainer Management | Name: "Suresh Raina", Specialization: "Strength & Conditioning", Phone: "9843210987" | Trainer registered with generated `trainer_id` | Trainer saved and indexed in system | **PASS** |
| **TC-TRN-02** | Assign member to trainer | Trainer Assignment | Member ID: 1, Trainer ID: 2, Date: "2026-01-05" | Assignment linked successfully; trainer active member count incremented | Record linked; trainer workload reflected | **PASS** |
| **TC-STS-01** | Evaluate Active membership status | Status Tracker | Start: "2026-01-01", Expiry: "2026-07-01", Current: "2026-03-01" | Status evaluated as `Active` | Evaluated as `Active` | **PASS** |
| **TC-STS-02** | Evaluate Expiring Soon membership status | Status Tracker | Expiry: "2026-03-25", Current: "2026-03-20" (5 days remaining) | Status evaluated as `Expiring Soon` | Evaluated as `Expiring Soon` | **PASS** |
| **TC-STS-03** | Evaluate Expired membership status | Status Tracker | Expiry: "2026-01-15", Current: "2026-03-01" | Status evaluated as `Expired` | Evaluated as `Expired` | **PASS** |
| **TC-RNW-01** | Renew expired membership with updated plan | Renewal Module | Member ID: 2, New Plan ID: 3 (Annual), Renewal Date: "2026-03-01" | Expiry recalculated to 2027-03-01; status updated to `Active` | Renewed successfully; expiry set to 2027-03-01 | **PASS** |
| **TC-REP-01** | Generate Revenue and Footfall Reports | Reporting Module | Request all-time financial and attendance aggregations | Accurate sum of plan fees and average workout session duration | Detailed report output generated with totals matching DB | **PASS** |
| **TC-DAT-01** | Python data retrieval and visualization | Python Analytics | Query all attendance and membership tables via connector | Preprocessed DataFrame, zero unhandled nulls, 5 clean charts generated | 5 PNG charts saved in `visualizations/` folder | **PASS** |

---

## 3. Test Summary and Quality Metrics

- **Total Test Cases Executed:** 17
- **Passed Test Cases:** 17 (100%)
- **Failed Test Cases:** 0 (0%)
- **Defects Identified and Resolved:** 0 open defects
- **Code Coverage:** > 90% statement coverage across Java domain modules.
- **Verification Statement:** The Gym Membership Management and Fitness Activity Analysis System fulfills all operational criteria defined in Scenario 27 of the Velalar College of Engineering and Technology curriculum.
