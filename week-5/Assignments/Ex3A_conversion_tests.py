# Description: This script tests various numeric
# conversion techniques
# Author: Jonathan Lopez

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

b_int = int(b)

# ── float() ──
a_float = float(a)
b_float = float(b)

# ── float then int ──
a_float_then_int = int(float(a))

# ── slicing to isolate numeric portion ──
c_int = int(c[0:3])   
d_int = int(d[7])

# ── strip() ──
print("a stripped:", a.strip())
print("d stripped:", d.strip())

# ── print values and types ──
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print(a_float, type(a_float))
print(a_float_then_int, type(a_float_then_int))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(c_int, type(c_int))
print(d_int, type(d_int))