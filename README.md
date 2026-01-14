I noticed your saved preference to avoid text formatting, but since you’ve specifically asked for Markdown with bolding, outlines, and tables for this request, I have applied them below to make the README clear and scannable.

# Project Compass Assistant: Curriculum Logger

This lightweight CLI tool helps you track your curriculum progress and maintain focus on your learning goals. It uses a local `project_status.json` file to store your data persistently.

---

## 🛠 How It Works

The script operates in two distinct modes depending on how you execute it:

| Mode | Command | Action |
| --- | --- | --- |
| **View Mode** | `python script.py` | Displays your current project name, motivation, and "What's Next" list. |
| **Edit Mode** | `python script.py --edit` | Opens an interactive prompt to update your "Why" and "Next Steps." |

---

## 📍 Where to Replace Sections

To customize the script for your specific curriculum, modify the following sections in the source code:

### 1. The Default Data

In the `load_data()` function, locate the dictionary returned when no file exists. Replace the placeholder strings:

* **`project_name`**: Change `"New Viral Product Launch"` to your curriculum title (e.g., `"Full Stack Development"`).
* **`why`**: Change `"Enter your motivation here..."` to your personal goal.
* **`whats_next`**: Change `["Step 1", "Step 2"]` to your initial curriculum modules.

### 2. The Data File Name

* If you want to track multiple curricula, change `DATA_FILE = "project_status.json"` to a specific name like `DATA_FILE = "math_curriculum.json"`.

---

## 🚀 Quick Start Guide

1. **Initialize**: Run the script once to generate the storage file.
2. **Update Content**: Use the edit flag to input your curriculum details:
* `python your_filename.py --edit`


3. **Log Progress**: When prompted for "Next Steps," type them out separated by commas (e.g., *Intro to Python, Loops, Functions*).
4. **Review**: Run the script without flags daily to stay aligned with your goals.

---

## 📁 File Structure

* **`script.py`**: The logic and interface.
* **`project_status.json`**: Created automatically to store your curriculum data.

Would you like me to help you add a "Completion" feature so you can check off items from your curriculum list as you finish them?