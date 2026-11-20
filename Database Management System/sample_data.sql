-- =====================================================================
-- SAMPLE DATABASE RECORDS
-- Gym Membership Management and Fitness Activity Analysis System
-- Scenario 27 — Velalar College of Engineering and Technology
-- =====================================================================

USE gym_management;

-- 1. Insert Membership Plans
INSERT INTO membership_plans (plan_id, plan_name, duration, fee, facilities) VALUES
(1, 'Basic Fitness', 1, 1500.00, 'Cardio Machines, Locker Room, General Gym Floor'),
(2, 'Standard Strength', 3, 3800.00, 'Free Weights, Resistance Machines, Locker Room, Shower'),
(3, 'Pro Athlete', 6, 7000.00, 'All Standard + Crossfit Zone, Steam Bath, Nutrition Consultation'),
(4, 'Elite Annual VIP', 12, 12500.00, 'All Pro + Personal Locker, Sauna, Swimming Pool, 5 Guest Passes');

-- 2. Insert Certified Trainers
INSERT INTO trainers (trainer_id, name, specialization, contact_no, email) VALUES
(1, 'Vikram Rathore', 'Strength & Bodybuilding', '9876501234', 'vikram.trainer@gym.com'),
(2, 'Ananya Sharma', 'Yoga & Flexibility', '9876502345', 'ananya.yoga@gym.com'),
(3, 'Karthik Raja', 'CrossFit & Functional HIIT', '9876503456', 'karthik.hiit@gym.com'),
(4, 'Divya Menon', 'Weight Loss & Aerobics', '9876504567', 'divya.aerobics@gym.com'),
(5, 'Rahul Varma', 'Rehabilitation & Conditioning', '9876505678', 'rahul.rehab@gym.com');

-- 3. Insert Members
INSERT INTO members (member_id, name, age, contact_no, email, registration_date) VALUES
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
(15, 'Harish Balan', 41, '9841556789', 'harish.balan@email.com', '2026-09-01');

-- 4. Insert Memberships (Active, Expired, and Expiring Soon)
-- Reference current assessment date: November 2026
INSERT INTO memberships (membership_id, member_id, plan_id, start_date, expiry_date, status) VALUES
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
(15, 15, 3, '2026-09-01', '2027-03-01', 'Active');

-- 5. Insert Trainer Assignments
INSERT INTO trainer_assignments (assignment_id, member_id, trainer_id, assignment_date, status) VALUES
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
(15, 15, 5, '2026-09-05', 'Active');

-- 6. Insert Attendance Logs (Footfalls across months Jan - Nov 2026)
INSERT INTO attendance (member_id, attendance_date, check_in_time, check_out_time, duration_minutes) VALUES
-- January Footfalls
(1, '2026-01-10', '06:15:00', '07:30:00', 75),
(2, '2026-01-10', '07:00:00', '08:00:00', 60),
(3, '2026-01-10', '18:00:00', '19:15:00', 75),
(1, '2026-01-12', '06:20:00', '07:45:00', 85),
(2, '2026-01-12', '07:10:00', '08:10:00', 60),
(3, '2026-01-13', '18:15:00', '19:30:00', 75),
(1, '2026-01-15', '06:30:00', '07:40:00', 70),
(2, '2026-01-16', '07:05:00', '08:20:00', 75),
(3, '2026-01-25', '18:00:00', '19:00:00', 60),

-- February Footfalls
(1, '2026-02-05', '06:15:00', '07:30:00', 75),
(4, '2026-02-05', '08:00:00', '09:00:00', 60),
(5, '2026-02-18', '17:30:00', '18:45:00', 75),
(1, '2026-02-19', '06:20:00', '07:30:00', 70),
(4, '2026-02-20', '08:15:00', '09:15:00', 60),
(5, '2026-02-22', '18:00:00', '19:15:00', 75),

-- March Footfalls
(1, '2026-03-05', '06:10:00', '07:25:00', 75),
(6, '2026-03-05', '07:00:00', '08:00:00', 60),
(7, '2026-03-12', '18:30:00', '19:45:00', 75),
(5, '2026-03-15', '17:45:00', '19:00:00', 75),
(6, '2026-03-18', '07:15:00', '08:15:00', 60),
(7, '2026-03-25', '18:00:00', '19:10:00', 70),

-- April Footfalls
(1, '2026-04-08', '06:30:00', '07:45:00', 75),
(8, '2026-04-10', '07:30:00', '08:30:00', 60),
(5, '2026-04-12', '18:00:00', '19:15:00', 75),
(9, '2026-04-20', '19:00:00', '20:15:00', 75),
(8, '2026-04-22', '07:45:00', '08:45:00', 60),
(9, '2026-04-28', '18:30:00', '19:50:00', 80),

-- May Footfalls
(1, '2026-05-04', '06:15:00', '07:30:00', 75),
(10, '2026-05-05', '08:00:00', '09:00:00', 60),
(11, '2026-05-22', '06:45:00', '08:00:00', 75),
(7, '2026-05-24', '18:15:00', '19:30:00', 75),
(9, '2026-05-25', '19:00:00', '20:15:00', 75),
(10, '2026-05-28', '08:10:00', '09:10:00', 60),

-- June Footfalls
(1, '2026-06-05', '06:30:00', '07:45:00', 75),
(11, '2026-06-08', '06:45:00', '07:55:00', 70),
(12, '2026-06-15', '17:30:00', '18:45:00', 75),
(7, '2026-06-18', '18:00:00', '19:15:00', 75),
(9, '2026-06-20', '18:45:00', '20:00:00', 75),
(12, '2026-06-25', '17:40:00', '18:50:00', 70),

-- July Footfalls
(1, '2026-07-08', '06:15:00', '07:35:00', 80),
(11, '2026-07-10', '06:30:00', '07:45:00', 75),
(13, '2026-07-12', '18:00:00', '19:15:00', 75),
(7, '2026-07-15', '18:15:00', '19:30:00', 75),
(12, '2026-07-20', '17:30:00', '18:45:00', 75),
(13, '2026-07-26', '18:10:00', '19:10:00', 60),

-- August Footfalls
(1, '2026-08-04', '06:20:00', '07:30:00', 70),
(11, '2026-08-10', '06:30:00', '07:45:00', 75),
(14, '2026-08-18', '07:00:00', '08:15:00', 75),
(9, '2026-08-20', '19:00:00', '20:15:00', 75),
(12, '2026-08-22', '17:30:00', '18:45:00', 75),
(14, '2026-08-28', '07:15:00', '08:30:00', 75),

-- September Footfalls
(1, '2026-09-02', '06:15:00', '07:30:00', 75),
(15, '2026-09-05', '06:30:00', '07:45:00', 75),
(11, '2026-09-10', '06:45:00', '08:00:00', 75),
(14, '2026-09-15', '07:00:00', '08:15:00', 75),
(15, '2026-09-20', '06:30:00', '07:40:00', 70),
(9, '2026-09-25', '18:30:00', '19:45:00', 75),

-- October Footfalls
(1, '2026-10-05', '06:30:00', '07:45:00', 75),
(11, '2026-10-08', '06:40:00', '07:50:00', 70),
(14, '2026-10-12', '07:15:00', '08:25:00', 70),
(15, '2026-10-18', '06:30:00', '07:45:00', 75),
(8, '2026-10-25', '07:30:00', '08:30:00', 60),
(12, '2026-10-28', '17:30:00', '18:45:00', 75),

-- November Footfalls (Current Month Active Trends)
(1, '2026-11-02', '06:15:00', '07:30:00', 75),
(11, '2026-11-04', '06:30:00', '07:45:00', 75),
(14, '2026-11-06', '07:00:00', '08:15:00', 75),
(15, '2026-11-08', '06:30:00', '07:45:00', 75),
(8, '2026-11-10', '07:30:00', '08:30:00', 60),
(9, '2026-11-12', '18:45:00', '20:00:00', 75),
(12, '2026-11-14', '17:30:00', '18:45:00', 75),
(1, '2026-11-16', '06:20:00', '07:35:00', 75),
(15, '2026-11-17', '06:30:00', '07:50:00', 80);

-- 7. Insert Historical Reports Log
INSERT INTO reports (report_id, report_type, generated_date, details) VALUES
(1, 'Monthly Revenue', '2026-06-30 20:00:00', 'Mid-year revenue calculation: Total Revenue Rs. 54,400 across all active and expired plans.'),
(2, 'Quarterly Attendance', '2026-09-30 20:00:00', 'Quarter 3 attendance summary: Average workout duration 73.2 minutes, highest footfall in morning slot (06:00 - 08:00).'),
(3, 'Trainer Workload Audit', '2026-11-01 10:00:00', 'Trainer assignment audit: Trainer 1 (Strength) holds 4 assigned members, Trainer 3 holds 3 members.');
