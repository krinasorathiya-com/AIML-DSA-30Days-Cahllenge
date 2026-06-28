emails = ["aman@gmail.com","riya@yahoo.com","yug@gmail.com","raj@outlook.com"]
domains = {}

for email in emails:
    domain = email.split("@")[1]

    if domain in domains:
        domains[domain] += 1
    else:
        domains[domain] = 1

print("Domain Counts:")

for domain, count in domains.items():
    print(domain, "->", count)