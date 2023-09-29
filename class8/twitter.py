import re

url = input("UPL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# # re.sub returns the results of substitution

match = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if match:
    print(f"Username: {match.group(1)}")