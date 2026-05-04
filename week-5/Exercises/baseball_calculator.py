player = input("Enter player name: ")
at_bats = int(input("At bats: "))
hits = int(input("Hits: "))
walks = int(input("Walks: "))
hbp = int(input("Hit by pitch: "))
sac_flies = int(input("Sacrifice flies: "))
Strike_Outs = int(input("Strike Outs: "))
Home_Runs = int(input("Home Runs: "))
RBIs = int(input("Runs Batted In: "))

batting_avg = hits / at_bats
obp = (hits + walks + hbp) / (at_bats + walks + hbp + sac_flies)

print(f"\n--- {player}'s Stats ---")
print(f"Batting Average : {batting_avg: .3f}")
print(f"On-Base% : {obp:.3f}")
print(f"Home Runs : {Home_Runs}")
print(f"RBIs : {RBIs}")
print(f"Strike Outs : {Strike_Outs}")