# Description: String cleaning exercises
# Author: Jonathan Lopez

name_1 = "John Lopez"
name_2 = "Crystal Longoria"
name_3 = "Natalia Marquez"
salary_1 = "$82,500"
salary_2 = "$74,000"

# ── .lower() ──
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# ── .title() ──
print(name_1.title())
print(name_2.title())
print(name_3.title())

# ── .replace() to remove $ ──
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")
print(salary_1_clean)
print(salary_2_clean)
print(type(salary_1_clean))

# ── chain .replace() and int() in one line ──
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)
print(type(salary_1_int))