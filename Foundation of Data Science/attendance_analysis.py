"""
Foundation of Data Science - Interactive Attendance Trends & Participation Analysis
Course: 25ITC31 - Foundations of Data Science (Units 3, 4, & 5)
Department of Information Technology, Velalar College of Engineering and Technology
"""

import os
import sys
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from data_loader import load_and_preprocess_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIZ_DIR = os.path.join(BASE_DIR, "visualizations")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "attendance_analysis_output.txt")

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

def generate_line_chart(monthly_trends):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.plot(monthly_trends['workout_month'], monthly_trends['total_visits'], 
            marker='o', color='#2563EB', linewidth=2.5, markersize=8, label='Monthly Footfall Visits')
    ax.plot(monthly_trends['workout_month'], monthly_trends['unique_members'], 
            marker='s', color='#10B981', linewidth=2, linestyle='--', markersize=6, label='Active Unique Members')

    for i, txt in enumerate(monthly_trends['total_visits']):
        ax.annotate(str(int(txt)), (monthly_trends['workout_month'][i], monthly_trends['total_visits'][i] + 0.3),
                    fontsize=9, ha='center', weight='bold', color='#1E40AF')

    ax.set_title("Gym Attendance Trends (Jan - Nov 2026)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Workout Month", fontsize=11, labelpad=10)
    ax.set_ylabel("Number of Footfalls", fontsize=11, labelpad=10)
    ax.set_ylim(0, max(monthly_trends['total_visits']) + 3)
    ax.legend(frameon=True, facecolor='white', framealpha=0.9)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "daily_monthly_attendance_trends.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Attendance Trends Line Chart saved: {path}")

def generate_histogram(participation):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    n, bins, patches = ax.hist(participation['visit_count'], bins=6, color='#6366F1', edgecolor='black', alpha=0.85, rwidth=0.85)

    for p in patches:
        p.set_facecolor('#4F46E5')

    ax.set_title("Member Participation Distribution (Workout Sessions per Member)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Workout Frequency (Number of Visits)", fontsize=11, labelpad=10)
    ax.set_ylabel("Member Count", fontsize=11, labelpad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "member_participation_analysis.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Member Participation Histogram saved: {path}")

def generate_peak_chart(attendance_df):
    os.makedirs(VIZ_DIR, exist_ok=True)
    hourly = attendance_df.groupby('check_in_hour')['attendance_id'].count().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    bars = ax.bar(hourly['check_in_hour'].astype(str) + ":00", hourly['attendance_id'], color='#0284C7', edgecolor='#0369A1', width=0.6)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, weight='bold')

    ax.set_title("Peak Facility Check-in Hours", fontsize=13, weight='bold', pad=15)
    ax.set_xlabel("Check-In Hour of Day", fontsize=11)
    ax.set_ylabel("Footfall Count", fontsize=11)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "peak_hours_analysis.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Peak Hours Bar Chart saved: {path}")

def run_automated_pipeline():
    os.makedirs(VIZ_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    datasets = load_and_preprocess_data()
    attendance_df = datasets["attendance"]
    members_df = datasets["members"]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        def log(text):
            print(text)
            out.write(text + "\n")

        log("=" * 75)
        log("GYM MEMBERSHIP MANAGEMENT - ATTENDANCE ANALYSIS REPORT")
        log(f"Generated at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log("=" * 75 + "\n")

        log("[1] ATTENDANCE DESCRIPTIVE STATISTICS (Unit 1):")
        log(f" - Total Workout Sessions Logged: {len(attendance_df)}")
        log(f" - Unique Members Participating : {attendance_df['member_id'].nunique()} / {len(members_df)}")
        log(f" - Mean Workout Duration        : {attendance_df['duration_minutes'].mean():.2f} minutes")
        log(f" - Standard Deviation (Duration): {attendance_df['duration_minutes'].std():.2f} minutes")
        log(f" - Median Workout Duration      : {attendance_df['duration_minutes'].median():.2f} minutes\n")

        monthly_trends = attendance_df.groupby('workout_month').agg(
            total_visits=('attendance_id', 'count'),
            unique_members=('member_id', 'nunique'),
            avg_duration=('duration_minutes', 'mean')
        ).reset_index()

        log("[2] MONTHLY ATTENDANCE FOOTFALL TRENDS:")
        log(f"{'Month':<10} | {'Total Visits':<12} | {'Unique Members':<14} | {'Avg Duration (mins)':<20}")
        log("-" * 62)
        for _, row in monthly_trends.iterrows():
            log(f"{row['workout_month']:<10} | {int(row['total_visits']):<12} | {int(row['unique_members']):<14} | {row['avg_duration']:<20.1f}")
        log("")

        participation = attendance_df.groupby(['member_id', 'name']).agg(
            visit_count=('attendance_id', 'count'),
            total_time_mins=('duration_minutes', 'sum')
        ).reset_index().sort_values(by='visit_count', ascending=False)

        log("[3] TOP 5 MOST ACTIVE GYM MEMBERS:")
        for idx, row in participation.head(5).reset_index().iterrows():
            log(f"{idx+1:<4} | {row['name']:<18} | {int(row['visit_count']):<12} | {row['total_time_mins']/60.0:<12.1f} hours")
        log("")

    generate_line_chart(monthly_trends)
    generate_histogram(participation)
    generate_peak_chart(attendance_df)
    print(f"\n[COMPLETED] Automated attendance report saved to: {OUTPUT_FILE}")

def interactive_attendance_menu():
    datasets = load_and_preprocess_data()
    attendance_df = datasets["attendance"]
    members_df = datasets["members"]

    monthly_trends = attendance_df.groupby('workout_month').agg(
        total_visits=('attendance_id', 'count'),
        unique_members=('member_id', 'nunique'),
        avg_duration=('duration_minutes', 'mean')
    ).reset_index()

    participation = attendance_df.groupby(['member_id', 'name']).agg(
        visit_count=('attendance_id', 'count'),
        total_time_mins=('duration_minutes', 'sum')
    ).reset_index().sort_values(by='visit_count', ascending=False)

    while True:
        print("\n" + "=" * 75)
        print("  FOUNDATION OF DATA SCIENCE: ATTENDANCE ANALYSIS (INTERACTIVE)")
        print("=" * 75)
        print(" 1. View Attendance Descriptive Statistics (Mean, Median, Std Dev)")
        print(" 2. View Monthly Footfall Breakdown Table")
        print(" 3. View Top Active Members (Custom N via Keyboard)")
        print(" 4. Search Attendance Records by Member ID (Manual Keyboard Input)")
        print(" 5. Generate Attendance Trends Line Chart")
        print(" 6. Generate Member Participation Histogram")
        print(" 7. Generate Peak Workout Hours Bar Chart")
        print(" 8. Run Full Automated Analysis & Save All Outputs to File")
        print(" 0. Exit to Main / Close")
        print("=" * 75)
        choice = input("Enter choice (0-8): ").strip()

        if choice == '1':
            print("\n--- ATTENDANCE DESCRIPTIVE STATISTICS (Unit 1) ---")
            print(f"Total Workout Sessions Logged: {len(attendance_df)}")
            print(f"Unique Participating Members : {attendance_df['member_id'].nunique()} / {len(members_df)}")
            print(f"Mean Workout Duration        : {attendance_df['duration_minutes'].mean():.2f} minutes")
            print(f"Standard Deviation           : {attendance_df['duration_minutes'].std():.2f} minutes")
            print(f"Median Workout Duration      : {attendance_df['duration_minutes'].median():.2f} minutes")
        elif choice == '2':
            print("\n--- MONTHLY ATTENDANCE FOOTFALL TRENDS ---")
            print(f"{'Month':<10} | {'Total Visits':<12} | {'Unique Members':<14} | {'Avg Duration':<15}")
            print("-" * 55)
            for _, row in monthly_trends.iterrows():
                print(f"{row['workout_month']:<10} | {int(row['total_visits']):<12} | {int(row['unique_members']):<14} | {row['avg_duration']:<15.1f} mins")
        elif choice == '3':
            n_val = input("How many top active members to display? [Default 5]: ").strip()
            n = int(n_val) if n_val.isdigit() else 5
            print(f"\n--- TOP {n} MOST ACTIVE MEMBERS ---")
            print(f"{'Rank':<4} | {'Member Name':<18} | {'Total Visits':<12} | {'Total Hours':<12}")
            print("-" * 52)
            for idx, row in participation.head(n).reset_index().iterrows():
                print(f"{idx+1:<4} | {row['name']:<18} | {int(row['visit_count']):<12} | {row['total_time_mins']/60.0:<12.1f} hrs")
        elif choice == '4':
            mem_id = input("\nEnter Member ID to search: ").strip()
            if mem_id.isdigit():
                sub = attendance_df[attendance_df['member_id'] == int(mem_id)]
                if not sub.empty:
                    print(f"\nFound {len(sub)} visits for Member ID {mem_id}:")
                    for _, r in sub.iterrows():
                        print(f" Date: {r['attendance_date'].strftime('%Y-%m-%d')} | In: {r['check_in_time']} | Out: {r['check_out_time']} | Duration: {r['duration_minutes']} mins")
                else:
                    print(f"No attendance logs found for Member ID {mem_id}.")
        elif choice == '5':
            generate_line_chart(monthly_trends)
        elif choice == '6':
            generate_histogram(participation)
        elif choice == '7':
            generate_peak_chart(attendance_df)
        elif choice == '8':
            run_automated_pipeline()
        elif choice == '0':
            print("Exiting Attendance Analysis.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "auto":
        run_automated_pipeline()
    else:
        interactive_attendance_menu()
