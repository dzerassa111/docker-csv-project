import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["employee_id", "full_name", "department", "salary", "performance_score", "years_experience", "is_manager"]

def generate_row():
    first_names = ["Алексей", "Мария", "Иван", "Елена", "Дмитрий", "Ольга", "Сергей", "Анна", "Константин", "Татьяна"]
    last_names = ["Иванов", "Петров", "Сидоров", "Козлов", "Смирнов", "Волков", "Морозов", "Новиков", "Федоров", "Орлов"]
    departments = ["IT", "HR", "Finance", "Marketing", "Sales", "Operations", "R&D"]
    
    return {
        "employee_id": f"EMP{random.randint(1000, 9999)}",
        "full_name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "department": random.choice(departments),
        "salary": round(random.uniform(45000, 150000), 2),
        "performance_score": random.randint(1, 10),
        "years_experience": random.randint(0, 30),
        "is_manager": random.choice(["Yes", "No"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)