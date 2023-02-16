no_fqdn = "https://api.domain.com"
fqdn = no_fqdn.removeprefix("https://")

print(f"no_fqdn: {no_fqdn}")
print(f"fqdn: {fqdn}")