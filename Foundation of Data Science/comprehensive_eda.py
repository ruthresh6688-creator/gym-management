"""
Foundation of Data Science - Master Exploratory Data Analysis (EDA) & Dashboard
Course: 25ITC31 - Foundations of Data Science (Full Syllabus Integration: Units 1 to 5)
Department of Information Technology, Velalar College of Engineering and Technology
"""

import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from data_loader import load_and_preprocess_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIZ_DIR = os.path.join(BASE_DIR, "visualizations")

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

def generate_master_dashboard():
    os.makedirs(VIZ_DIR, exist_ok=True)
    datasets = load_and_preprocess_data()
    attendance_df = datasets["attendance"]
    memberships_df = datasets["memberships"]
    trainers_df = datasets["trainers"]
    assignments_df = datasets["assignments"]
    members_df = datasets["members"]

    # Create figure with 2 rows and 3 columns
    fig, axes = plt.subplots(2, 3, figsize=(18, 10), dpi=300)
    fig.suptitle("Gym Membership Management & Fitness Activity Analysis Dashboard", 
                 fontsize=18, weight='bold', y=0.98, color='#1E3A8A')

    # Panel 1: Monthly Attendance Footfall (Line Chart)
    monthly = attendance_df.groupby('workout_month')['attendance_id'].count().reset_index()
    axes[0, 0].plot(monthly['workout_month'], monthly['attendance_id'], 
                    marker='o', color='#2563EB', linewidth=2.5, markersize=6)
    axes[0, 0].set_title("1. Monthly Attendance Trends (Line Chart)", fontsize=12, weight='bold')
    axes[0, 0].set_xlabel("Workout Month", fontsize=10)
    axes[0, 0].set_ylabel("Total Footfalls", fontsize=10)
    axes[0, 0].tick_params(axis='x', rotation=30)

    # Panel 2: Plan Popularity (Bar Chart)
    plan_counts = memberships_df['plan_name'].value_counts()
    bars2 = axes[0, 1].bar(plan_counts.index, plan_counts.values, color='#3B82F6', edgecolor='black', width=0.55)
    axes[0, 1].set_title("2. Membership Plan Popularity (Bar Chart)", fontsize=12, weight='bold')
    axes[0, 1].set_xlabel("Plan Tier", fontsize=10)
    axes[0, 1].set_ylabel("Subscribers", fontsize=10)
    axes[0, 1].tick_params(axis='x', rotation=15)
    for b in bars2:
        axes[0, 1].annotate(f'{int(b.get_height())}', (b.get_x() + b.get_width() / 2, b.get_height()),
                            xytext=(0, 3), textcoords="offset points", ha='center', weight='bold', fontsize=9)

    # Panel 3: Active vs Expired Status (Pie Chart)
    status_counts = memberships_df['status'].value_counts()
    axes[0, 2].pie(
        status_counts.values,
        labels=status_counts.index,
        autopct='%1.1f%%',
        colors=['#10B981', '#EF4444', '#F59E0B'],
        startangle=140,
        textprops={'fontsize': 10, 'weight': 'bold'}
    )
    axes[0, 2].set_title("3. Membership Status Ratio (Pie Chart)", fontsize=12, weight='bold')

    # Panel 4: Trainer Workloads (Bar Chart)
    merged_trn = assignments_df.merge(trainers_df, on='trainer_id', how='right')
    workload = merged_trn.groupby('name')['assignment_id'].count().reset_index()
    bars4 = axes[1, 0].bar(workload['name'], workload['assignment_id'], color='#8B5CF6', edgecolor='black', width=0.55)
    axes[1, 0].set_title("4. Trainer Workload Analysis (Bar Chart)", fontsize=12, weight='bold')
    axes[1, 0].set_xlabel("Trainer Name", fontsize=10)
    axes[1, 0].set_ylabel("Assigned Trainees", fontsize=10)
    axes[1, 0].tick_params(axis='x', rotation=20)
    for b in bars4:
        axes[1, 0].annotate(f'{int(b.get_height())}', (b.get_x() + b.get_width() / 2, b.get_height()),
                            xytext=(0, 3), textcoords="offset points", ha='center', weight='bold', fontsize=9)

    # Panel 5: Member Participation (Histogram)
    part = attendance_df.groupby('member_id')['attendance_id'].count()
    axes[1, 1].hist(part, bins=5, color='#06B6D4', edgecolor='black', rwidth=0.85)
    axes[1, 1].set_title("5. Member Participation Analysis (Histogram)", fontsize=12, weight='bold')
    axes[1, 1].set_xlabel("Workout Visits Count", fontsize=10)
    axes[1, 1].set_ylabel("Number of Members", fontsize=10)

    # Panel 6: Peak Check-in Hours (Bar Chart)
    hourly = attendance_df.groupby('check_in_hour')['attendance_id'].count()
    axes[1, 2].bar(hourly.index.astype(str) + ":00", hourly.values, color='#F97316', edgecolor='black', width=0.55)
    axes[1, 2].set_title("6. Peak Facility Check-In Hours (Bar Chart)", fontsize=12, weight='bold')
    axes[1, 2].set_xlabel("Check-In Hour", fontsize=10)
    axes[1, 2].set_ylabel("Footfall Sessions", fontsize=10)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    dashboard_path = os.path.join(VIZ_DIR, "gym_analytics_dashboard.png")
    fig.savefig(dashboard_path)
    plt.close(fig)
    print(f"[SUCCESS] Master 6-panel executive dashboard saved to: {dashboard_path}")

if __name__ == "__main__":
    generate_master_dashboard()
