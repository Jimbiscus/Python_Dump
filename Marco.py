msg = "J'adore le python"
print("".join(w.upper() if i % 2 else w.lower() for i,w in enumerate(msg)))

msg = "I love online learning"
msg = msg.split(' ')
print(f"👏 {(' 👏 ' * 1).join(msg)} 👏")
