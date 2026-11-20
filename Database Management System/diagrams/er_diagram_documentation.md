# Entity-Relationship (E-R) Diagram Specification
## Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
**Course:** 25ITT31 – Database Management Systems (Unit 1: Database Systems and Design)  
**Institution:** Velalar College of Engineering and Technology, Erode - 12  

---

### E-R Diagram Reference
The formal visual E-R diagram is archived directly in this directory:
**[View E-R Diagram Image](er_diagram.jpg)**

---

## 1. Entity Sets and Attributes

1. **Member Entity Set**
   - `member_id` (Primary Key, Underlined)
   - `name` (Single-valued attribute)
   - `age` (Single-valued numeric attribute)
   - `contact_no` (Single-valued attribute)
   - `registration_date` (Date attribute)

2. **Membership Plan Entity Set**
   - `plan_id` (Primary Key, Underlined)
   - `plan_name` (Descriptive attribute)
   - `duration` (Numeric duration in months)
   - `fee` (Monetary attribute)
   - `facilities` (Descriptive textual attribute)

3. **Membership Entity Set (Associative Entity)**
   - `start_date`
   - `expiry_date`
   - `status` ('Active', 'Expired', 'Expiring Soon')

4. **Trainer Entity Set**
   - `trainer_id` (Primary Key, Underlined)
   - `name` (Single-valued attribute)
   - `specialization` (Expertise area)
   - `contact_no` (Contact number)

5. **Attendance Entity Set**
   - `attendance_id` (Primary Key, Underlined)
   - `attendance_date` (Date of workout)
   - `check_in_time` (Time of facility entry)
   - `check_out_time` (Time of facility exit)

6. **Reports Entity Set**
   - `report_id` (Primary Key, Underlined)
   - `report_type` (Categorical type)
   - `generated_date` (Timestamp)
   - `details` (Report text summary)

7. **Analysis Entity Set**
   - `analysis_id` (Primary Key, Underlined)
   - `analysis_type` (Type of analytics: Attendance, Workload, Popularity)
   - `insights` (Summary conclusions)
   - `visualization_url` (Path to output chart image)

---

## 2. Relationships and Mapping Cardinalities

| Relationship Name | Connecting Entities | Mapping Cardinality | Participation Constraints |
| :--- | :--- | :---: | :--- |
| **Has** | `Member` — `Membership` | **1 : 1** | Total on Member (Each member subscribes to membership) |
| **Uses** | `Membership` — `Membership Plan` | **M : 1** | Total on Membership (Every membership uses a defined plan) |
| **Assigned To** | `Member` — `Trainer` | **M : 1** | Partial (Members may choose personal training or general access) |
| **Trains** | `Trainer` — `Attendance` | **1 : M** | Partial on Trainer, Total on Attendance sessions |
| **Records** | `Membership` — `Attendance` | **1 : M** | Total on Attendance (Attendance must belong to a membership) |
| **Generates** | `Attendance` — `Reports` | **1 : M** | Partial (Footfalls feed into recurring reports) |
| **Uses** | `Attendance` — `Analysis` | **1 : 1** | Partial (Python engine processes attendance logs for analysis) |

---

## 3. Structural Constraints Summary
- **Referential Actions:** Deleting a member removes related membership and attendance logs (CASCADE) while preserving the trainer and membership plan catalog records (RESTRICT).
- **Domain Constraints:** Age must be $\ge 14$, plan fee $\ge 0$, and valid check-out timestamp must chronologically follow check-in time.
