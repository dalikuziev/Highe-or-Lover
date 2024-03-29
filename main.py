import random as r
from game_data import data
from emoji import logo, vs

print(logo)
a = r.choice(data)
b = r.choice(data)
while a == b:
  b = r.choice(data)
i = 0
print(f"A: {a['name']}, {a['description']}, {a['country']}.")
print(vs)
print(f"B: {b['name']}, {b['description']}, {b['country']}.")

while True:
  user = input("qay birini ko'proq odam kuzatadi? A/B: ").lower()
  if user == "a" and a["follower_count"] > b["follower_count"]:
    i += 1
    print(logo)
    print(f"hozircha ochko: {i}")
    b = r.choice(data)
    print(f"A: {a['name']} {a['description']} {a['country']}")
    print(vs)
    print(f"B: {b['name']} {b['description']} {b['country']}")
  elif user == "a" and a["follower_count"] < b["follower_count"]:
    print(logo)
    print(f"oxirgi ochko: {i}")
    break
  elif user == "b" and a["follower_count"] > b["follower_count"]:
    print(logo)
    print(f"oxirgi ochko: {i}")
    break
  elif user == "b" and a["follower_count"] < b["follower_count"]:
    i += 1
    print(logo)
    print(f"hozircha ochko: {i}")
    a = b
    b = r.choice(data)
    print(f"A: {a['name']} {a['description']} {a['country']}")
    print(vs)
    print(f"B: {b['name']} {b['description']} {b['country']}")
