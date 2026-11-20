-- =====================================================================
-- GYM MEMBERSHIP MANAGEMENT AND FITNESS ACTIVITY ANALYSIS SYSTEM
-- Scenario 27 — Velalar College of Engineering and Technology (Autonomous)
-- Course: 25ITT31 - Database Management Systems
-- =====================================================================

-- Step 1: Database Initialization
CREATE DATABASE IF NOT EXISTS gym_management;
USE gym_management;

-- Drop dependent tables first to ensure clean execution
DROP TABLE IF EXISTS reports;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS trainer_assignments;
DROP TABLE IF EXISTS memberships;
DROP TABLE IF EXISTS trainers;
DROP TABLE IF EXISTS membership_plans;
DROP TABLE IF EXISTS members;

-- =====================================================================
-- Table 1: members
-- Stores personal and registration details of gym members
-- =====================================================================
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE,
    registration_date DATE NOT NULL,
    CONSTRAINT chk_member_age CHECK (age >= 14),
    CONSTRAINT chk_member_contact CHECK (LENGTH(contact_no) >= 10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 2: membership_plans
-- Stores available membership tiers, fees, duration, and facilities
-- =====================================================================
CREATE TABLE membership_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL UNIQUE,
    duration INT NOT NULL COMMENT 'Duration in Months',
    fee DECIMAL(10, 2) NOT NULL,
    facilities TEXT NOT NULL,
    CONSTRAINT chk_plan_duration CHECK (duration > 0),
    CONSTRAINT chk_plan_fee CHECK (fee >= 0.00)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 3: memberships
-- Stores member subscription mapping, validity periods, and status
-- =====================================================================
CREATE TABLE memberships (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    plan_id INT NOT NULL,
    start_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Active',
    CONSTRAINT chk_membership_dates CHECK (expiry_date >= start_date),
    CONSTRAINT chk_membership_status CHECK (status IN ('Active', 'Expired', 'Expiring Soon')),
    CONSTRAINT fk_memberships_member FOREIGN KEY (member_id) 
        REFERENCES members(member_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_memberships_plan FOREIGN KEY (plan_id) 
        REFERENCES membership_plans(plan_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 4: trainers
-- Stores fitness instructors, specializations, and contact details
-- =====================================================================
CREATE TABLE trainers (
    trainer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 5: trainer_assignments
-- Maps members to specialized trainers for personal coaching
-- =====================================================================
CREATE TABLE trainer_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    trainer_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Active',
    CONSTRAINT chk_assignment_status CHECK (status IN ('Active', 'Completed', 'Transferred')),
    CONSTRAINT fk_assignments_member FOREIGN KEY (member_id) 
        REFERENCES members(member_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_assignments_trainer FOREIGN KEY (trainer_id) 
        REFERENCES trainers(trainer_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 6: attendance
-- Records daily physical footfalls, check-in, check-out, and duration
-- =====================================================================
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    check_in_time TIME NOT NULL,
    check_out_time TIME,
    duration_minutes INT DEFAULT 0,
    CONSTRAINT fk_attendance_member FOREIGN KEY (member_id) 
        REFERENCES members(member_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =====================================================================
-- Table 7: reports
-- Stores system-generated operational, financial, and renewal audits
-- =====================================================================
CREATE TABLE reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    report_type VARCHAR(50) NOT NULL,
    generated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    details TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create Indexes for Query Optimization (Unit 3: Indexing)
CREATE INDEX idx_members_registration ON members(registration_date);
CREATE INDEX idx_memberships_status ON memberships(status, expiry_date);
CREATE INDEX idx_attendance_date ON attendance(attendance_date, member_id);
CREATE INDEX idx_assignments_trainer ON trainer_assignments(trainer_id);
