import re

# Parse BHK from query
def parse_bhk(query: str):
    match = re.search(r"(\d+)\s*bhk", query)
    if match:
        return int(match.group(1))
    return None

# Parse budget in lakhs/crores
def parse_budget(query: str):
    match = re.search(r"(\d+)\s*(lakh|lakhs|cr|crore|crores)", query)
    if not match:
        return None

    amount = int(match.group(1))
    unit = match.group(2)

    if "lakh" in unit:
        return amount * 100000
    elif "cr" in unit or "crore" in unit:
        return amount * 10000000
    return None
