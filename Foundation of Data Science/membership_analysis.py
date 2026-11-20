"""
Foundation of Data Science - Interactive Membership Plan & Status Analysis
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "membership_analysis_output.txt")

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

def generate_plan_bar_chart(plan_summary):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)
    colors = ['#3B82F6', '#10B981', '#F59E0B', '#8B5CF6']
    bars = ax.bar(plan_summary['plan_name'], plan_summary['subscriber_count'], 
                  color=colors[:len(plan_summary)], edgecolor='black', width=0.55)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)} Enrolled',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, weight='bold')

    ax.set_title("Membership Plan Popularity Distribution", fontsize=14, weight='bold', pad=15)
    ax.set_xlabel("Membership Plan Tier", fontsize=11, labelpad=10)
    ax.set_ylabel("Number of Subscribed Members", fontsize=11, labelpad=10)
    ax.set_ylim(0, max(plan_summary['subscriber_count']) + 2)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "membership_plan_popularity.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Plan Popularity Bar Chart saved: {path}")

def generate_status_pie_chart(status_counts):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
    status_colors = {
        'Active': '#10B981',
        'Expired': '#EF4444',
        'Expiring Soon': '#F59E0B'
    }
    labels = status_counts.index.tolist()
    slice_colors = [status_colors.get(lbl, '#6B7280') for lbl in labels]
    explode = [0.05 if lbl == 'Active' else 0.02 for lbl in labels]

    wedges, texts, autotexts = ax.pie(
        status_counts.values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=slice_colors,
        explode=explode,
        shadow=True,
        textprops={'fontsize': 11, 'weight': 'bold'}
    )

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)

    ax.set_title("Membership Subscription Status Ratio\n(Active vs. Expired vs. Expiring Soon)", 
                 fontsize=14, weight='bold', pad=20)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "active_vs_expired_memberships.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Membership Status Pie Chart saved: {path}")

def generate_revenue_bar_chart(plan_summary):
    os.makedirs(VIZ_DIR, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8.5, 4.5), dpi=300)
    y_pos = np.arange(len(plan_summary))
    bars = ax.barh(y_pos, plan_summary['total_revenue'], color='#059669', edgecolor='black', height=0.55)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(plan_summary['plan_name'], fontsize=10)
    ax.invert_yaxis()

    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'Rs. {width:,.0f}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=9, weight='bold')

    ax.set_title("Total Revenue Generation by Membership Tier", fontsize=13, weight='bold', pad=15)
    ax.set_xlabel("Revenue (INR)", fontsize=11)
    ax.set_xlim(0, max(plan_summary['total_revenue']) * 1.2)
    plt.tight_layout()

    path = os.path.join(VIZ_DIR, "membership_revenue_by_plan.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"[SUCCESS] Revenue Breakdown Chart saved: {path}")

def run_automated_pipeline():
    os.makedirs(VIZ_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    datasets = load_and_preprocess_data()
    memberships_df = datasets["memberships"]

    plan_summary = memberships_df.groupby('plan_name').agg(
        subscriber_count=('membership_id', 'count'),
        total_revenue=('fee', 'sum')
    ).reset_index().sort_values(by='subscriber_count', ascending=False)
    status_counts = memberships_df['status'].value_counts()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("=" * 75 + "\n")
        out.write("GYM MEMBERSHIP MANAGEMENT - MEMBERSHIP ANALYSIS REPORT\n")
        out.write(f"Generated at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write("=" * 75 + "\n\n")

        out.write("[1] PLAN POPULARITY & FINANCIAL CONTRIBUTION:\n")
        for _, row in plan_summary.iterrows():
            out.write(f" - {row['plan_name']:<18}: {int(row['subscriber_count']):<2} members | Rs. {row['total_revenue']:,.2f}\n")
        out.write(f"Total Revenue: Rs. {plan_summary['total_revenue'].sum():,.2f}\n\n")

        out.write("[2] MEMBERSHIP STATUS RATIO:\n")
        for st, c in status_counts.items():
            pct = (c / len(memberships_df)) * 100
            out.write(f" - {st:<15}: {c} memberships ({pct:.1f}%)\n")

    generate_plan_bar_chart(plan_summary)
    generate_status_pie_chart(status_counts)
    generate_revenue_bar_chart(plan_summary)
    print(f"\n[COMPLETED] Automated membership report saved to: {OUTPUT_FILE}")

def interactive_membership_menu():
    datasets = load_and_preprocess_data()
    memberships_df = datasets["memberships"]

    plan_summary = memberships_df.groupby('plan_name').agg(
        subscriber_count=('membership_id', 'count'),
        total_revenue=('fee', 'sum')
    ).reset_index().sort_values(by='subscriber_count', ascending=False)
    status_counts = memberships_df['status'].value_counts()

    while True:
        print("\n" + "=" * 75)
        print("  FOUNDATION OF DATA SCIENCE: MEMBERSHIP ANALYSIS (INTERACTIVE)")
        print("=" * 75)
        print(" 1. View Plan Popularity & Financial Contributions")
        print(" 2. View Active vs. Expired vs. Expiring-Soon Statistics")
        print(" 3. Search Member Subscription Details (Manual Keyboard Input)")
        print(" 4. Generate Membership Plan Popularity Bar Chart")
        print(" 5. Generate Active vs. Expired Status Ratio Pie Chart")
        print(" 6. Generate Revenue Breakdown Horizontal Bar Chart")
        print(" 7. Run Full Automated Analysis & Save All Visualizations/Output")
        print(" 0. Exit to Main / Close")
        print("=" * 75)
        choice = input("Enter choice (0-7): ").strip()

        if choice == '1':
            print("\n--- MEMBERSHIP PLAN POPULARITY & FINANCIAL CONTRIBUTION ---")
            print(f"{'Plan Name':<20} | {'Subscribers':<12} | {'Revenue (INR)':<15} | {'Share (%)':<10}")
            print("-" * 65)
            for _, row in plan_summary.iterrows():
                share = (row['subscriber_count'] / len(memberships_df)) * 100.0
                print(f"{row['plan_name']:<20} | {int(row['subscriber_count']):<12} | Rs. {row['total_revenue']:<11.2f} | {share:<10.1f}%")
            print(f"Total Revenue Generated: Rs. {plan_summary['total_revenue'].sum():,.2f}")
        elif choice == '2':
            print("\n--- MEMBERSHIP STATUS DISTRIBUTION ---")
            for status, count in status_counts.items():
                pct = (count / len(memberships_df)) * 100.0
                print(f" - {status:<15}: {count:<3} memberships ({pct:.1f}%)")
        elif choice == '3':
            m_id = input("\nEnter Member ID to inspect subscription: ").strip()
            if m_id.isdigit():
                sub = memberships_df[memberships_df['member_id'] == int(m_id)]
                if not sub.empty:
                    for _, r in sub.iterrows():
                        print(f"\n[MEMBERSHIP RECORD] ID: {r['membership_id']}")
                        print(f" Plan Name  : {r['plan_name']}")
                        print(f" Start Date : {r['start_date'].strftime('%Y-%m-%d')}")
                        print(f" Expiry Date: {r['expiry_date'].strftime('%Y-%m-%d')}")
                        print(f" Status     : {r['status']}")
                else:
                    print(f"No membership subscriptions found for Member ID {m_id}.")
        elif choice == '4':
            generate_plan_bar_chart(plan_summary)
        elif choice == '5':
            generate_status_pie_chart(status_counts)
        elif choice == '6':
            generate_revenue_bar_chart(plan_summary)
        elif choice == '7':
            run_automated_pipeline()
        elif choice == '0':
            print("Exiting Membership Analysis.")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "auto":
        run_automated_pipeline()
    else:
        interactive_membership_menu()
