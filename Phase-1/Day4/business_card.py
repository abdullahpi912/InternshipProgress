# ============================================================
# business_card.py -- Task 3: Digital Business Card (Dictionary)
# ============================================================
card = {
    "name": "Abd",
    "role": "AI & Data Science Student",
    "email": "abdullahpi912@gmail.com",
    "phone": "+91-XXXXXXXXXX",
    "linkedin": "linkedin.com/in/abdullahpi912",
}

def print_card(card):
    # Access dictionary values by key instead of position
    print("===== DIGITAL BUSINESS CARD =====")
    print(f"Name     : {card['name']}")
    print(f"Role     : {card['role']}")
    print(f"Email    : {card['email']}")
    print(f"Phone    : {card['phone']}")
    print(f"LinkedIn : {card['linkedin']}")

print_card(card)

card["role"] = "Full Stack AI Developer Intern"  # update an existing value
print("\nAfter updating role:")
print_card(card)
