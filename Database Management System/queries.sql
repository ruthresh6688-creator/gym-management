-- =====================================================================
-- SQL QUERIES AND REPORTING SCRIPTS
-- Gym Membership Management and Fitness Activity Analysis System
-- Scenario 27 — Velalar College of Engineering and Technology (Autonomous)
-- Course: 25ITT31 - Database Management Systems (Units 2 & 3)
-- =====================================================================

USE gym_management;

-- =====================================================================
-- SECTION 1: BASIC CRUD OPERATIONS (Data Manipulation Language - DML)
-- =====================================================================

-- 1.1 SELECT: Retrieve all registered members
SELECT member_id, name, age, contact_no, email, registration_date 
FROM members 
ORDER BY member_id ASC;

-- 1.2 INSERT: Register a new member
INSERT INTO members (name, age, contact_no, email, registration_date)
VALUES ('Karthika V', 27, '9841667890', 'karthika.v@email.com', '2026-11-01');

-- 1.3 UPDATE: Modify contact number and age of a member
UPDATE members 
SET contact_no = '9840199999', age = 25 
WHERE member_id = 1;

-- 1.4 DELETE: Remove a cancelled trainer assignment
DELETE FROM trainer_assignments 
WHERE assignment_id = 10 AND status = 'Completed';

-- =====================================================================
-- SECTION 2: SQL JOINS (Unit 2: Intermediate SQL)
-- =====================================================================

-- 2.1 INNER JOIN: Get active member details along with their chosen plan name and fee
SELECT 
    m.member_id,
    m.name AS member_name,
    m.contact_no,
    p.plan_name,
    p.fee,
    ms.start_date,
    ms.expiry_date,
    ms.status
FROM members m
INNER JOIN memberships ms ON m.member_id = ms.member_id
INNER JOIN membership_plans p ON ms.plan_id = p.plan_id
WHERE ms.status = 'Active';

-- 2.2 LEFT OUTER JOIN: List all trainers and their assigned members (including trainers with 0 assignments)
SELECT 
    t.trainer_id,
    t.name AS trainer_name,
    t.specialization,
    m.name AS assigned_member_name,
    ta.assignment_date,
    ta.status AS assignment_status
FROM trainers t
LEFT JOIN trainer_assignments ta ON t.trainer_id = ta.trainer_id
LEFT JOIN members m ON ta.member_id = m.member_id
ORDER BY t.trainer_id;

-- 2.3 MULTI-TABLE JOIN: Comprehensive Member Profile (Member + Plan + Trainer + Attendance Count)
SELECT 
    m.member_id,
    m.name AS member_name,
    p.plan_name,
    ms.status AS membership_status,
    COALESCE(t.name, 'Unassigned') AS trainer_name,
    COUNT(a.attendance_id) AS total_attendance_sessions
FROM members m
LEFT JOIN memberships ms ON m.member_id = ms.member_id
LEFT JOIN membership_plans p ON ms.plan_id = p.plan_id
LEFT JOIN trainer_assignments ta ON m.member_id = ta.member_id AND ta.status = 'Active'
LEFT JOIN trainers t ON ta.trainer_id = t.trainer_id
LEFT JOIN attendance a ON m.member_id = a.member_id
GROUP BY m.member_id, m.name, p.plan_name, ms.status, t.name
ORDER BY m.member_id;

-- =====================================================================
-- SECTION 3: AGGREGATE FUNCTIONS & GROUP BY (Unit 2: SQL Basics)
-- =====================================================================

-- 3.1 Aggregating gym workout session metrics
SELECT 
    COUNT(attendance_id) AS total_footfalls,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_mins,
    MIN(duration_minutes) AS min_duration_mins,
    MAX(duration_minutes) AS max_duration_mins
FROM attendance;

-- 3.2 Plan Popularity: Count of members enrolled in each plan
SELECT 
    p.plan_id,
    p.plan_name,
    COUNT(ms.membership_id) AS total_subscribers,
    SUM(p.fee) AS total_revenue_generated
FROM membership_plans p
LEFT JOIN memberships ms ON p.plan_id = ms.plan_id
GROUP BY p.plan_id, p.plan_name
ORDER BY total_subscribers DESC;

-- 3.3 HAVING Clause: Filter trainers managing more than 2 members
SELECT 
    t.trainer_id,
    t.name AS trainer_name,
    t.specialization,
    COUNT(ta.assignment_id) AS active_member_count
FROM trainers t
JOIN trainer_assignments ta ON t.trainer_id = ta.trainer_id
WHERE ta.status = 'Active'
GROUP BY t.trainer_id, t.name, t.specialization
HAVING COUNT(ta.assignment_id) >= 2
ORDER BY active_member_count DESC;

-- =====================================================================
-- SECTION 4: MEMBERSHIP STATUS TRACKING (Active, Expired, Expiring Soon)
-- =====================================================================

-- 4.1 Categorize and track memberships dynamically based on current date
SELECT 
    m.member_id,
    m.name,
    p.plan_name,
    ms.start_date,
    ms.expiry_date,
    DATEDIFF(ms.expiry_date, CURRENT_DATE) AS days_remaining,
    CASE 
        WHEN CURRENT_DATE > ms.expiry_date THEN 'Expired'
        WHEN DATEDIFF(ms.expiry_date, CURRENT_DATE) BETWEEN 0 AND 7 THEN 'Expiring Soon'
        ELSE 'Active'
    END AS dynamic_status
FROM members m
JOIN memberships ms ON m.member_id = ms.member_id
JOIN membership_plans p ON ms.plan_id = p.plan_id
ORDER BY days_remaining ASC;

-- 4.2 Summary count of memberships by status
SELECT 
    status,
    COUNT(*) AS total_count,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM memberships)), 2) AS percentage
FROM memberships
GROUP BY status;

-- =====================================================================
-- SECTION 5: MEMBERSHIP REVENUE REPORTS
-- =====================================================================

-- 5.1 Plan-wise Revenue Contribution Breakdown
SELECT 
    p.plan_name,
    p.duration AS duration_months,
    p.fee AS plan_fee,
    COUNT(ms.membership_id) AS subscriptions_count,
    SUM(p.fee) AS total_revenue
FROM membership_plans p
JOIN memberships ms ON p.plan_id = ms.plan_id
GROUP BY p.plan_id, p.plan_name, p.duration, p.fee
ORDER BY total_revenue DESC;

-- 5.2 Total Overall Revenue
SELECT 
    SUM(p.fee) AS grand_total_revenue,
    AVG(p.fee) AS average_plan_ticket_size,
    COUNT(ms.membership_id) AS total_memberships_sold
FROM memberships ms
JOIN membership_plans p ON ms.plan_id = p.plan_id;

-- =====================================================================
-- SECTION 6: ATTENDANCE SUMMARIES & PATTERNS
-- =====================================================================

-- 6.1 Monthly footfall trends (Jan to Nov 2026)
SELECT 
    DATE_FORMAT(attendance_date, '%Y-%m') AS workout_month,
    COUNT(attendance_id) AS total_visits,
    COUNT(DISTINCT member_id) AS unique_members_attended,
    ROUND(AVG(duration_minutes), 1) AS avg_workout_mins
FROM attendance
GROUP BY DATE_FORMAT(attendance_date, '%Y-%m')
ORDER BY workout_month ASC;

-- 6.2 Workout Time Slot Analysis (Morning vs Evening Footfalls)
SELECT 
    CASE 
        WHEN HOUR(check_in_time) BETWEEN 5 AND 11 THEN 'Morning (05:00 - 11:59)'
        WHEN HOUR(check_in_time) BETWEEN 12 AND 16 THEN 'Afternoon (12:00 - 16:59)'
        WHEN HOUR(check_in_time) BETWEEN 17 AND 22 THEN 'Evening (17:00 - 22:59)'
        ELSE 'Night'
    END AS time_slot,
    COUNT(*) AS slot_visits,
    ROUND(AVG(duration_minutes), 1) AS avg_duration
FROM attendance
GROUP BY time_slot
ORDER BY slot_visits DESC;

-- 6.3 Top 5 Most Active Members
SELECT 
    m.member_id,
    m.name AS member_name,
    COUNT(a.attendance_id) AS total_visits,
    SUM(a.duration_minutes) AS total_gym_minutes,
    ROUND(SUM(a.duration_minutes)/60.0, 1) AS total_gym_hours
FROM members m
JOIN attendance a ON m.member_id = a.member_id
GROUP BY m.member_id, m.name
ORDER BY total_visits DESC
LIMIT 5;

-- =====================================================================
-- SECTION 7: TRAINER WORKLOAD & MEMBERSHIP RENEWALS
-- =====================================================================

-- 7.1 Trainer Workload Distribution
SELECT 
    t.trainer_id,
    t.name AS trainer_name,
    t.specialization,
    COUNT(CASE WHEN ta.status = 'Active' THEN 1 END) AS current_active_clients,
    COUNT(ta.assignment_id) AS total_historical_clients
FROM trainers t
LEFT JOIN trainer_assignments ta ON t.trainer_id = ta.trainer_id
GROUP BY t.trainer_id, t.name, t.specialization
ORDER BY current_active_clients DESC;

-- 7.2 Members requiring renewal outreach (Expiring Soon and Expired)
SELECT 
    m.member_id,
    m.name AS member_name,
    m.contact_no,
    p.plan_name AS last_plan,
    ms.expiry_date,
    ms.status,
    DATEDIFF(CURRENT_DATE, ms.expiry_date) AS days_since_expiry
FROM members m
JOIN memberships ms ON m.member_id = ms.member_id
JOIN membership_plans p ON ms.plan_id = p.plan_id
WHERE ms.status IN ('Expired', 'Expiring Soon')
ORDER BY ms.expiry_date ASC;
