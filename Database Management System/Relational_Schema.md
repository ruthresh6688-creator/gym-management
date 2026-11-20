# Relational Schema Specification
## Gym Membership Management and Fitness Activity Analysis System (Scenario 27)
**Academic Year:** 2026 - 2027 (ODD)  
**Course:** 25ITT31 – Database Management Systems (Unit 1 & Unit 2)  
**Institution:** Velalar College of Engineering and Technology, Erode - 12  

---

## 1. Relational Schema Representation

The schema follows standard relational notation where **bold underline** denotes a Primary Key (PK) and *italic with dagger* ($\dagger$) denotes a Foreign Key (FK).

1. **`MEMBERS`** (
   **`member_id`**: INT,  
   `name`: VARCHAR(100),  
   `age`: INT,  
   `contact_no`: VARCHAR(15),  
   `email`: VARCHAR(100),  
   `registration_date`: DATE  
)

2. **`MEMBERSHIP_PLANS`** (
   **`plan_id`**: INT,  
   `plan_name`: VARCHAR(50),  
   `duration`: INT,  
   `fee`: DECIMAL(10,2),  
   `facilities`: TEXT  
)

3. **`MEMBERSHIPS`** (
   **`membership_id`**: INT,  
   *`member_id`*$\dagger$: INT,  
   *`plan_id`*$\dagger$: INT,  
   `start_date`: DATE,  
   `expiry_date`: DATE,  
   `status`: VARCHAR(20)  
)

4. **`TRAINERS`** (
   **`trainer_id`**: INT,  
   `name`: VARCHAR(100),  
   `specialization`: VARCHAR(100),  
   `contact_no`: VARCHAR(15),  
   `email`: VARCHAR(100)  
)

5. **`TRAINER_ASSIGNMENTS`** (
   **`assignment_id`**: INT,  
   *`member_id`*$\dagger$: INT,  
   *`trainer_id`*$\dagger$: INT,  
   `assignment_date`: DATE,  
   `status`: VARCHAR(20)  
)

6. **`ATTENDANCE`** (
   **`attendance_id`**: INT,  
   *`member_id`*$\dagger$: INT,  
   `attendance_date`: DATE,  
   `check_in_time`: TIME,  
   `check_out_time`: TIME,  
   `duration_minutes`: INT  
)

7. **`REPORTS`** (
   **`report_id`**: INT,  
   `report_type`: VARCHAR(50),  
   `generated_date`: DATETIME,  
   `details`: TEXT  
)

---

## 2. Integrity Constraints & Referential Actions

| Source Table | Foreign Key Column | Target Table | Target Primary Key | On Delete Action | On Update Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `MEMBERSHIPS` | `member_id` | `MEMBERS` | `member_id` | CASCADE | CASCADE |
| `MEMBERSHIPS` | `plan_id` | `MEMBERSHIP_PLANS` | `plan_id` | RESTRICT | CASCADE |
| `TRAINER_ASSIGNMENTS`| `member_id` | `MEMBERS` | `member_id` | CASCADE | CASCADE |
| `TRAINER_ASSIGNMENTS`| `trainer_id` | `TRAINERS` | `trainer_id` | RESTRICT | CASCADE |
| `ATTENDANCE` | `member_id` | `MEMBERS` | `member_id` | CASCADE | CASCADE |

---

## 3. Data Dictionary

### Table: `members`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `member_id` | INT | NO | AUTO_INCREMENT | Unique identifier for gym member (Primary Key) |
| `name` | VARCHAR(100) | NO | None | Full legal name of gym member |
| `age` | INT | NO | None | Member age (Constraint: age >= 14) |
| `contact_no` | VARCHAR(15) | NO | None | Member telephone/mobile (Min 10 digits) |
| `email` | VARCHAR(100) | YES | NULL | Unique email address for notifications |
| `registration_date`| DATE | NO | None | Date when the member joined the gym |

### Table: `membership_plans`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `plan_id` | INT | NO | AUTO_INCREMENT | Unique identifier for membership plan (Primary Key) |
| `plan_name` | VARCHAR(50) | NO | None | Unique name (e.g. Basic, Standard, Pro, VIP) |
| `duration` | INT | NO | None | Duration in months (Constraint: > 0) |
| `fee` | DECIMAL(10,2)| NO | None | Plan price in INR (Constraint: >= 0.00) |
| `facilities` | TEXT | NO | None | Included facilities (Cardio, Sauna, Weights) |

### Table: `memberships`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `membership_id` | INT | NO | AUTO_INCREMENT | Subscription record identifier (Primary Key) |
| `member_id` | INT | NO | None | FK referencing `members.member_id` |
| `plan_id` | INT | NO | None | FK referencing `membership_plans.plan_id` |
| `start_date` | DATE | NO | None | Effective subscription start date |
| `expiry_date` | DATE | NO | None | Computed expiration date |
| `status` | VARCHAR(20) | NO | 'Active' | Status: 'Active', 'Expired', 'Expiring Soon' |

### Table: `trainers`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `trainer_id` | INT | NO | AUTO_INCREMENT | Unique identifier for certified trainer (Primary Key) |
| `name` | VARCHAR(100) | NO | None | Full name of trainer |
| `specialization`| VARCHAR(100) | NO | None | Core training domain (Cardio, Strength, HIIT, Yoga) |
| `contact_no` | VARCHAR(15) | NO | None | Contact telephone number |
| `email` | VARCHAR(100) | YES | NULL | Trainer email address |

### Table: `trainer_assignments`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `assignment_id` | INT | NO | AUTO_INCREMENT | Assignment relationship identifier (Primary Key) |
| `member_id` | INT | NO | None | FK referencing `members.member_id` |
| `trainer_id` | INT | NO | None | FK referencing `trainers.trainer_id` |
| `assignment_date`| DATE | NO | None | Date of assignment initiation |
| `status` | VARCHAR(20) | NO | 'Active' | Assignment status ('Active', 'Completed') |

### Table: `attendance`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `attendance_id` | INT | NO | AUTO_INCREMENT | Daily attendance log identifier (Primary Key) |
| `member_id` | INT | NO | None | FK referencing `members.member_id` |
| `attendance_date`| DATE | NO | None | Date of gym visit |
| `check_in_time` | TIME | NO | None | Timestamp of facility entry |
| `check_out_time`| TIME | YES | NULL | Timestamp of facility exit |
| `duration_minutes`| INT | YES | 0 | Computed duration in minutes |

### Table: `reports`
| Column | Type | Nullable | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `report_id` | INT | NO | AUTO_INCREMENT | Report log identifier (Primary Key) |
| `report_type` | VARCHAR(50) | NO | None | Type (e.g. Revenue, Attendance, Renewal) |
| `generated_date`| DATETIME | NO | CURRENT_TIMESTAMP| Report generation timestamp |
| `details` | TEXT | NO | None | Narrative or JSON report payload |
