import re

def validate_credit_card(card: str) -> str:
    if not bool(re.search(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', card)):
        return "Invalid"
    
    card = card.replace("-", "")
    if bool(re.search(r'(.)\1{3}', card)):
        return "Invalid"
        
    return "Valid"

n = int(input())

for i in range(n):
    print(validate_credit_card(input()))
