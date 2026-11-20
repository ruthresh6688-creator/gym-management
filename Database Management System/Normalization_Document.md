# Database Normalization Document
## Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
**Academic Year:** 2026 - 2027 (ODD)  
**Course Code & Name:** 25ITT31 – Database Management Systems (Unit 3: Normalization & Relational Design)  
**Department:** Information Technology, Velalar College of Engineering and Technology, Erode - 12  

---

## 1. Overview of Relational Database Normalization

Normalization is a systematic technique of organizing relational database schemas to:
1. **Minimize Data Redundancy:** Avoid duplicate storage of member, plan, trainer, and attendance data.
2. **Prevent Anomalies:** Eliminate Insertion Anomalies, Deletion Anomalies, and Update/Modification Anomalies.
3. **Preserve Functional Dependencies:** Ensure lossless decomposition through Boyce-Codd / 3rd Normal Form (3NF).

---

## 2. Unnormalized Form (UNF) Representation

Consider a single flat spreadsheet record representing gym activities:

| Column Name | Sample Value | Issues Observed |
| :--- | :--- | :--- |
| `Member_Record` | (1, 'Aarav Patel', 24, '9840112345') | Repeating operational rows |
| `Plan_Details` | ('Elite Annual VIP', 12, 12500, {Locker, Sauna, Pool}) | Multi-valued facilities attribute |
| `Trainer_Details`| (1, 'Vikram Rathore', 'Strength & Bodybuilding', '9876501234') | Redundant trainer data replicated per member |
| `Attendance_Logs`| {(2026-01-10, 06:15, 07:30), (2026-01-12, 06:20, 07:45), ...} | Multi-valued repeating groups |

### Anomalies in UNF:
- **Insertion Anomaly:** Cannot introduce a new trainer or new membership plan until at least one member subscribes.
- **Deletion Anomaly:** Deleting a member record removes historical attendance and trainer profiles if they were the only assigned member.
- **Update Anomaly:** Updating a plan fee requires updating multiple duplicate rows, risking data inconsistency.

---

## 3. First Normal Form (1NF)

### 1NF Rule:
* Each column must contain atomic (indivisible) values.
* There must be no repeating groups or multi-valued arrays.
* Each record must have a unique identifier (Primary Key).

### Transformation to 1NF:
Repeating attendance entries and trainer details are broken down into discrete rows. The multi-valued facilities string is formatted into standardized comma-separated or relational token attributes.

**Resulting 1NF Schema:**
- `MEMBERS_FLAT` (`member_id`, `name`, `age`, `contact_no`, `plan_name`, `duration`, `fee`, `trainer_id`, `trainer_name`, `attendance_date`, `check_in_time`, `check_out_time`)
- **Primary Key in 1NF:** Composite key `(member_id, attendance_date, check_in_time)`.

---

## 4. Second Normal Form (2NF)

### 2NF Rule:
* The relation must already be in **1NF**.
* Every non-prime attribute must be **fully functionally dependent** on the whole primary key (No **Partial Dependencies**).

### Identifying Partial Dependencies:
- In the composite key `(member_id, attendance_date, check_in_time)`:
  - `member_name`, `age`, `contact_no` depend solely on `member_id` (Partial Dependency).
  - `plan_name`, `duration`, `fee` depend solely on the plan or member's subscription, not on the attendance timestamp.
  - `trainer_name`, `specialization` depend solely on `trainer_id`.

### Decomposition to 2NF:
We decompose into distinct entities where attributes depend entirely on each entity's primary key:

1. **`MEMBERS`** (`member_id` [PK], `name`, `age`, `contact_no`, `email`, `registration_date`)
   - Functional Dependency: `member_id` -> `name`, `age`, `contact_no`, `email`, `registration_date`
2. **`MEMBERSHIP_PLANS`** (`plan_id` [PK], `plan_name`, `duration`, `fee`, `facilities`)
   - Functional Dependency: `plan_id` -> `plan_name`, `duration`, `fee`, `facilities`
3. **`TRAINERS`** (`trainer_id` [PK], `name`, `specialization`, `contact_no`, `email`)
   - Functional Dependency: `trainer_id` -> `name`, `specialization`, `contact_no`, `email`
4. **`ATTENDANCE`** (`attendance_id` [PK], `member_id` [FK], `attendance_date`, `check_in_time`, `check_out_time`, `duration_minutes`)
   - Functional Dependency: `attendance_id` -> `member_id`, `attendance_date`, `check_in_time`, `check_out_time`, `duration_minutes`

---

## 5. Third Normal Form (3NF)

### 3NF Rule:
* The relation must be in **2NF**.
* There must be **no transitive dependencies** (Non-prime attributes must not depend on other non-prime attributes).
* Formally: For every functional dependency $X \rightarrow Y$, either:
  1. $X$ is a super key, OR
  2. $Y$ is a prime attribute (part of a candidate key).

### Analyzing Transitive Dependencies:
- If `memberships` were stored inside `members`: `member_id` -> `plan_id` -> `fee`, creating a transitive dependency: `member_id` -> `fee`.
- Similarly, member-to-trainer assignments represent a distinct association entity with its own lifecycle (members can change trainers without altering member demographic details).

### Decomposition into 3NF Entities:

1. **`MEMBERS`** (Member Entity)
   $$\text{FD}_1: \text{member\_id} \rightarrow \{\text{name}, \text{age}, \text{contact\_no}, \text{email}, \text{registration\_date}\}$$
   - Key: `member_id` is Super Key. (Satisfies 3NF)

2. **`MEMBERSHIP_PLANS`** (Plan Catalog)
   $$\text{FD}_2: \text{plan\_id} \rightarrow \{\text{plan\_name}, \text{duration}, \text{fee}, \text{facilities}\}$$
   - Key: `plan_id` is Super Key. (Satisfies 3NF)

3. **`MEMBERSHIPS`** (Subscription Association Entity)
   $$\text{FD}_3: \text{membership\_id} \rightarrow \{\text{member\_id}, \text{plan\_id}, \text{start\_date}, \text{expiry\_date}, \text{status}\}$$
   - Foreign Keys: `member_id` references `MEMBERS`, `plan_id` references `MEMBERSHIP_PLANS`.
   - Key: `membership_id` is Super Key. No transitive attributes. (Satisfies 3NF)

4. **`TRAINERS`** (Instructor Entity)
   $$\text{FD}_4: \text{trainer\_id} \rightarrow \{\text{name}, \text{specialization}, \text{contact\_no}, \text{email}\}$$
   - Key: `trainer_id` is Super Key. (Satisfies 3NF)

5. **`TRAINER_ASSIGNMENTS`** (Coaching Association Entity)
   $$\text{FD}_5: \text{assignment\_id} \rightarrow \{\text{member\_id}, \text{trainer\_id}, \text{assignment\_date}, \text{status}\}$$
   - Foreign Keys: `member_id` references `MEMBERS`, `trainer_id` references `TRAINERS`. (Satisfies 3NF)

6. **`ATTENDANCE`** (Operational Transaction Entity)
   $$\text{FD}_6: \text{attendance\_id} \rightarrow \{\text{member\_id}, \text{attendance\_date}, \text{check\_in\_time}, \text{check\_out\_time}, \text{duration\_minutes}\}$$
   - Foreign Key: `member_id` references `MEMBERS`. (Satisfies 3NF)

7. **`REPORTS`** (Reporting & Audit Entity)
   $$\text{FD}_7: \text{report\_id} \rightarrow \{\text{report\_type}, \text{generated\_date}, \text{details}\}$$
   - Key: `report_id` is Super Key. (Satisfies 3NF)

---

## 6. Summary of Normalization Benefits

| Metric | Unnormalized / Flat Design | 3NF Normalized Design |
| :--- | :--- | :--- |
| **Data Redundancy** | Extremely high; duplicate member and trainer records | Zero redundant non-key data |
| **Update Integrity** | High risk of partial updates and inconsistencies | Single point of truth for plans, members, and trainers |
| **Referential Integrity** | No constraints; vulnerable to corrupted foreign references | Enforced via declarative Foreign Key constraints |
| **Lossless Join Property** | Natural joins produced false spurius tuples | Guaranteed lossless join via relational keys |
| **Dependency Preservation**| Violated | 100% of functional dependencies preserved |
