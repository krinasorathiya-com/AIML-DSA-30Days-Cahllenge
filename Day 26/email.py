emails = ["abc@gmail.com","xyz@gmail.com", "user@yahoo.com","krina@outlook.com","code@gmail.com"]

domains = {}

for email in emails:
    domain = email.split("@")[1]

    if domain in domains:
        domains[domain] += 1
    else:
        domains[domain] = 1

for domain, count in domains.items():
    print(domain, "->", count)