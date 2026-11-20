"""
Foundation of Data Science - Interactive Trainer Workload & Client Analysis
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "trainer_analysis_output.txt")

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

def generate_workload_bar_chart(workload_summary):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    x = np.arange(len(workload_summary))
    width = 0.35

    bars1 = ax.bar(x - width/2, workload_summary['active_clients'], width, 
                   label='Current Active Clients', color='#4F46E5', edgecolor='black')
    bars2 = ax.bar(x + width/2, workload_summary['total_historical_clients'], width, 
                   label='Total Historical Clients', color='#A5B4FC', edgecolor='black')

    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, weight='bold')

    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

    ax.set_title("Trainer Workload Distribution (Active vs. Total Clients)", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Certified Fitness Trainers", fontsize=11, labelpad=10)
    ax.set_ylabel("Number of Assigned Members", fontsize=11, labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(workload_summary['name'], rotation=15, ha='right', fontsize=10)
    ax.set_ylim(0, max(workload_summary['total_historical_clients']) + 2)
    ax.legend(frameon=True, facecolor='white')
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "trainer_workload_analysis.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Trainer Workload Bar Chart saved: {path}")

def generate_donut_chart(trainers_df):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
    spec_counts = trainers_df['specialization'].value_counts()
    colors = ['#0EA5E9', '#14B8A6', '#F97316', '#EC4899', '#8B5CF6']

    wedges, texts, autotexts = ax.pie(
        spec_counts.values,
        labels=spec_counts.index,
        autopct='%1.0f%%',
        pctdistance=0.75,
        colors=colors[:len(spec_counts)],
        startangle=90,
        textprops={'fontsize': 10, 'weight': 'bold'}
    )

    centre_circle = plt.Circle((0, 0), 0.55, fc='white')
    fig.gca().add_artist(centre_circle)

    ax.set_title("Trainer Coaching Specialization Distribution", fontsize=13, weight='bold', pad=20)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "trainer_specialization_distribution.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Specialization Donut Chart saved: {path}")

def run_automated_pipeline():
    os.makedirs(VIZ_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    datasets = load_and_preprocess_data()
    trainers_df = datasets["trainers"]
    assignments_df = datasets["assignments"]

    merged = assignments_df.merge(trainers_df, on='trainer_id', how='right')
    workload_summary = merged.groupby(['trainer_id', 'name', 'specialization']).agg(
        active_clients=('status', lambda s: (s == 'Active').sum()),
        total_historical_clients=('assignment_id', 'count')
    ).reset_index().sort_values(by='active_clients', ascending=False)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("=" * 75 + "\n")
        out.write("GYM MEMBERSHIP MANAGEMENT - TRAINER WORKLOAD ANALYSIS REPORT\n")
        out.write(f"Generated at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write("=" * 75 + "\n\n")

        out.write("[1] TRAINER CLIENT CAPACITY & WORKLOAD DISTRIBUTION:\n")
        for _, row in workload_summary.iterrows():
            out.write(f" - {row['name']:<18} ({row['specialization']}): {row['active_clients']} active / {row['total_historical_clients']} total clients\n")

        out.write("\n[2] DESCRIPTIVE METRICS (Unit 1):\n")
        out.write(f" - Average Active Clients per Trainer : {workload_summary['active_clients'].mean():.2f}\n")
        out.write(f" - Standard Deviation of Workloads     : {workload_summary['active_clients'].std():.2f}\n")

    generate_workload_bar_chart(workload_summary)
    generate_donut_chart(trainers_df)
    print(f"\n[COMPLETED] Automated trainer report saved to: {OUTPUT_FILE}")

def interactive_trainer_menu():
    datasets = load_and_preprocess_data()
    trainers_df = datasets["trainers"]
    assignments_df = datasets["assignments"]

    merged = assignments_df.merge(trainers_df, on='trainer_id', how='right')
    workload_summary = merged.groupby(['trainer_id', 'name', 'specialization']).agg(
        active_clients=('status', lambda s: (s == 'Active').sum()),
        total_historical_clients=('assignment_id', 'count')
    ).reset_index().sort_values(by='active_clients', ascending=False)

    while True:
        print("\n" + "=" * 75)
        print("  FOUNDATION OF DATA SCIENCE: TRAINER WORKLOAD (INTERACTIVE)")
        print("=" * 75)
        print(" 1. View Trainer Workload & Capacity Table")
        print(" 2. View Workload Balance Descriptive Metrics (Mean, Std Dev)")
        print(" 3. Search Assigned Members for Specific Trainer (Manual Keyboard Input)")
        print(" 4. Generate Trainer Workload Bar Chart")
        print(" 5. Generate Trainer Specialization Donut Chart")
        print(" 6. Run Full Automated Analysis & Save All Visualizations/Output")
        print(" 0. Exit to Main / Close")
        print("=" * 75)
        choice = input("Enter choice (0-6): ").strip()

        if choice == '1':
            print("\n--- TRAINER CLIENT CAPACITY & WORKLOAD TABLE ---")
            print(f"{'Trainer Name':<18} | {'Specialization':<30} | {'Active':<8} | {'Total'}")
            print("-" * 68)
            for _, row in workload_summary.iterrows():
                print(f"{row['name']:<18} | {row['specialization']:<30} | {row['active_clients']:<8} | {row['total_historical_clients']}")
        elif choice == '2':
            print("\n--- WORKLOAD DESCRIPTIVE METRICS (Unit 1) ---")
            print(f"Average Active Clients per Trainer : {workload_summary['active_clients'].mean():.2f}")
            print(f"Standard Deviation                 : {workload_summary['active_clients'].std():.2f}")
            print(f"Maximum Workload on Single Trainer : {workload_summary['active_clients'].max()} trainees")
        elif choice == '3':
            t_id = input("\nEnter Trainer ID to check assigned trainees (1-5): ").strip()
            if t_id.isdigit():
                sub = assignments_df[assignments_df['trainer_id'] == int(t_id)]
                if not sub.empty:
                    print(f"\nAssigned Members for Trainer ID {t_id}:")
                    for _, r in sub.iterrows():
                        print(f" Assignment ID: {r['assignment_id']} | Member ID: {r['member_id']} | Status: {r['status']} | Date: {r['assignment_date'].strftime('%Y-%m-%d')}")
                else:
                    print(f"No assignments found for Trainer ID {t_id}.")
        elif choice == '4':
            generate_workload_bar_chart(workload_summary)
        elif choice == '5':
            generate_donut_chart(trainers_df)
        elif choice == '6':
            run_automated_pipeline()
        elif choice == '0':
            print("Exiting Trainer Analysis.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "auto":
        run_automated_pipeline()
    else:
        interactive_trainer_menu()
