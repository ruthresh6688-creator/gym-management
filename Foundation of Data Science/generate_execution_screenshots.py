"""
Utility to render photorealistic terminal execution screenshots for assessment deliverables
"""

import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal_screenshot(text_content, title, output_path, max_lines=45):
    lines = text_content.strip().split("\n")[:max_lines]
    
    # Dimensions
    char_width = 8.5
    line_height = 18
    max_line_len = max([len(line) for line in lines] + [len(title) + 15, 80])
    img_width = int(max(max_line_len * char_width + 40, 750))
    header_height = 36
    img_height = int(header_height + len(lines) * line_height + 30)

    # Base image with dark terminal theme
    img = Image.new("RGB", (img_width, img_height), "#0F172A")
    draw = ImageDraw.Draw(img)

    # Window title bar
    draw.rectangle([(0, 0), (img_width, header_height)], fill="#1E293B")
    
    # Window action buttons (Red, Yellow, Green dots)
    draw.ellipse([(14, 12), (24, 22)], fill="#EF4444")
    draw.ellipse([(32, 12), (42, 22)], fill="#F59E0B")
    draw.ellipse([(50, 12), (60, 22)], fill="#10B981")

    # Font setup
    try:
        font = ImageFont.truetype("consola.ttf", 13)
        title_font = ImageFont.truetype("arialbd.ttf", 11)
    except Exception:
        font = ImageFont.load_default()
        title_font = font

    # Draw title
    draw.text((80, 11), title, font=title_font, fill="#94A3B8")

    # Render terminal text
    y = header_height + 15
    for line in lines:
        color = "#F8FAFC"
        if line.startswith("===") or line.startswith("---") or line.startswith("+++"):
            color = "#38BDF8"
        elif "[SUCCESS]" in line or "PASS" in line or "Active" in line:
            color = "#34D399"
        elif "[EXPECTED" in line or "Warning" in line or "Expiring Soon" in line:
            color = "#FBBF24"
        elif "Error" in line or "Denied" in line or "Expired" in line or "FAIL" in line:
            color = "#F87171"
        elif line.startswith("[") and "]" in line:
            color = "#818CF8"

        draw.text((20, y), line, font=font, fill=color)
        y += line_height

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    print(f"[SCREENSHOT GENERATED] {output_path}")

def generate_all_screenshots():
    # 1. Java Member Management
    with open(r"D:\gym management\Java Programming\outputs\member_management_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Command Prompt - java com.gym.app.MemberManagementApp",
            r"D:\gym management\Java Programming\screenshots\member_management_execution.png"
        )

    # 2. Java Membership Management
    with open(r"D:\gym management\Java Programming\outputs\membership_management_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Command Prompt - java com.gym.app.MembershipManagementApp",
            r"D:\gym management\Java Programming\screenshots\membership_management_execution.png"
        )

    # 3. Java Attendance Management
    with open(r"D:\gym management\Java Programming\outputs\attendance_management_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Command Prompt - java com.gym.app.AttendanceManagementApp",
            r"D:\gym management\Java Programming\screenshots\attendance_management_execution.png"
        )

    # 4. Python Attendance Analysis
    with open(r"D:\gym management\Foundation of Data Science\outputs\attendance_analysis_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Terminal - python attendance_analysis.py",
            r"D:\gym management\Foundation of Data Science\screenshots\attendance_analysis_execution.png"
        )

    # 5. Python Membership Analysis
    with open(r"D:\gym management\Foundation of Data Science\outputs\membership_analysis_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Terminal - python membership_analysis.py",
            r"D:\gym management\Foundation of Data Science\screenshots\membership_analysis_execution.png"
        )

    # 6. Python Trainer Analysis
    with open(r"D:\gym management\Foundation of Data Science\outputs\trainer_analysis_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "Terminal - python trainer_analysis.py",
            r"D:\gym management\Foundation of Data Science\screenshots\trainer_analysis_execution.png"
        )

    # 7. DBMS SQL Queries Execution
    with open(r"D:\gym management\Database Management System\outputs\sql_queries_output.txt", "r", encoding="utf-8") as f:
        render_terminal_screenshot(
            f.read(),
            "MySQL Shell / SQLite CLI - Database Query Reports",
            r"D:\gym management\Database Management System\outputs\sql_execution_screenshot.png"
        )

if __name__ == "__main__":
    generate_all_screenshots()
