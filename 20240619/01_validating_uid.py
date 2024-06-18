import re

def validate_uid(uid: str) -> str:
    if not len(uid) == 10:
        return "Invalid"
    if not bool(re.search(r'[A-Z].*[A-Z]', uid)):
        return "Invalid"
    if not bool(re.search(r'[0-9].*[0-9].*[0-9]', uid)):
        return "Invalid"
    if not bool(re.search(r'^[a-zA-Z0-9]*$', uid)):
        return "Invalid"
    if bool(re.search(r'(.)\1', uid)):
        return "Invalid"

    for i in range(len(uid)):
        if uid[i] in uid[i+1:]:
            return "Invalid"
        
    return "Valid"

n = int(input())

for i in range(n):
    print(validate_uid(input()))

