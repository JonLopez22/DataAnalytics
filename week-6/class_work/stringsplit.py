def split_lineup(lineup):
    parts = lineup.split(", ")
    return parts
result = split_lineup("Judge, Soto, Stanton, Rizzo, Trevino")
print("Today's lineup:")
print(result)