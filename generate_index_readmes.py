#!/usr/bin/env python3
"""
Generate/update index README.md files for:
- Root (master index)
- Each semester folder
- Each subject folder (listing units or experiments)
"""

import os
import re
from pathlib import Path

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
SEMESTERS = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "4-1", "4-2", "DSA"]

# Optional: Map semester to a friendly name
SEMESTER_NAMES = {
    "1-1": "I Year - I Semester",
    "1-2": "I Year - II Semester",
    "2-1": "II Year - I Semester",
    "2-2": "II Year - II Semester",
    "3-1": "III Year - I Semester",
    "3-2": "III Year - II Semester",
    "4-1": "IV Year - I Semester",
    "4-2": "IV Year - II Semester",
    "DSA": "Data Structures & Algorithms",
}

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------

def get_subfolders(path):
    """Return list of immediate subdirectories (non-hidden)."""
    if not os.path.exists(path):
        return []
    return sorted([
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d)) and not d.startswith(".")
    ])

def get_units(path):
    """Return list of Unit-X folders in a theory subject."""
    units = []
    for d in get_subfolders(path):
        if re.match(r"^Unit-[1-5]$", d):
            units.append(d)
    return sorted(units, key=lambda x: int(x.split("-")[1]))

def get_experiments(path):
    """Return list of NN-Experiment folders in a lab subject."""
    exps = []
    for d in get_subfolders(path):
        if re.match(r"^[0-9][0-9]-Experiment$", d):
            exps.append(d)
    return sorted(exps, key=lambda x: int(x.split("-")[0]))

def is_lab_subject(subject_name):
    """Heuristic to identify lab subjects."""
    lab_keywords = ["Lab", "Project", "Workshop", "IT-Lab"]
    for kw in lab_keywords:
        if kw in subject_name or subject_name.endswith("-Lab"):
            return True
    return False

def write_file(path, content):
    """Write content to path, overwriting existing."""
    with open(path, "w") as f:
        f.write(content)
    print(f"Generated: {path}")

# ---------------------------------------------------------------------
# 1. ROOT README
# ---------------------------------------------------------------------
def generate_root_readme():
    content = f"""# College Repository – B.Tech CSE (VR24)

Welcome to my B.Tech Computer Science Engineering coursework repository.  
This repo contains lab experiments, assignments, notes, and projects organised by semester and subject.

---

## 📁 Semester Overview

| Semester | Folder |
|----------|--------|
"""
    for sem in SEMESTERS:
        if sem == "DSA":
            content += f"| **Data Structures & Algorithms** | [📂 DSA](/DSA) |\n"
        else:
            name = SEMESTER_NAMES.get(sem, sem)
            content += f"| **{name}** | [📂 {sem}](/{sem}) |\n"

    content += f"""
---

## 🚀 How to Use

1. Browse the semester folders above.
2. Each semester contains subject folders (theory and lab).
3. Inside theory subjects, you'll find `Unit-1` … `Unit-5` with detailed READMEs.
4. Inside lab subjects, you'll find numbered experiments (`01-Experiment` … `NN-Experiment`).

---

## 📬 Contact

For any queries or suggestions, please open an issue or reach out via [GitHub](https://github.com/anu-deepika).

---

**Happy Learning!** 🎓
"""
    write_file("README.md", content)

# ---------------------------------------------------------------------
# 2. SEMESTER README
# ---------------------------------------------------------------------
def generate_semester_readme(sem_path, sem_name):
    subjects = get_subfolders(sem_path)
    if not subjects:
        content = f"""# {sem_name}

This semester folder is currently empty.
"""
        write_file(os.path.join(sem_path, "README.md"), content)
        return

    content = f"""# {sem_name}

## 📚 Subjects

| Subject | Type | Contents |
|---------|------|----------|
"""
    for sub in subjects:
        sub_path = os.path.join(sem_path, sub)
        if is_lab_subject(sub):
            exp_count = len(get_experiments(sub_path))
            link = f"[📂 {sub}](/{sem_path}/{sub})"
            content += f"| {link} | Lab | {exp_count} experiments |\n"
        else:
            unit_count = len(get_units(sub_path))
            link = f"[📂 {sub}](/{sem_path}/{sub})"
            content += f"| {link} | Theory | {unit_count} units |\n"

    content += f"""

---

*This README lists all subjects in the {sem_name} semester.*
"""
    write_file(os.path.join(sem_path, "README.md"), content)

# ---------------------------------------------------------------------
# 3. SUBJECT README (Theory or Lab)
# ---------------------------------------------------------------------
def generate_subject_readme(subject_path, sem_name, subject_name):
    is_lab = is_lab_subject(subject_name)

    if is_lab:
        exps = get_experiments(subject_path)
        content = f"""# {subject_name}

**Semester:** {sem_name}  
**Type:** Lab

---

## 🧪 Experiments

| S.No | Experiment |
|------|------------|
"""
        for i, exp in enumerate(exps, 1):
            content += f"| {i} | [{exp}](/{subject_path}/{exp}/README.md) |\n"

        if not exps:
            content += "| - | No experiments found yet. |\n"

        content += f"""

---

*This README lists all experiments for the {subject_name} lab.*
"""
        write_file(os.path.join(subject_path, "README.md"), content)

    else:
        units = get_units(subject_path)
        content = f"""# {subject_name}

**Semester:** {sem_name}  
**Type:** Theory

---

## 📖 Units

| Unit | Folder |
|------|--------|
"""
        for unit in units:
            unit_num = unit.split("-")[1]
            content += f"| Unit {unit_num} | [{unit}](/{subject_path}/{unit}/README.md) |\n"

        if not units:
            content += "| - | No units found yet. |\n"

        content += f"""

---

*This README lists all units for the {subject_name} theory subject.*
"""
        write_file(os.path.join(subject_path, "README.md"), content)

# ---------------------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------------------
def main():
    print("Generating index READMEs...")

    # 1. Root
    generate_root_readme()

    # 2. Semesters
    for sem in SEMESTERS:
        sem_path = sem
        if not os.path.exists(sem_path):
            print(f"Warning: {sem_path} not found, skipping.")
            continue
        sem_name = SEMESTER_NAMES.get(sem, sem)
        generate_semester_readme(sem_path, sem_name)

        # 3. Subjects inside each semester
        subjects = get_subfolders(sem_path)
        for sub in subjects:
            sub_path = os.path.join(sem_path, sub)
            generate_subject_readme(sub_path, sem_name, sub)

    print("\nDone! All index READMEs have been generated/updated.")

if __name__ == "__main__":
    main()
    