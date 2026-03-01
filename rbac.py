# rbac.py
# Тестові дані для завдання 2.2 "Role-Based Access Control (RBAC)"

# Атомарні ролі та їхні права
ROLE_PERMISSIONS = {
    "guest": {"read"},
    "intern": {"read"},
    "developer": {"read", "write", "debug"},
    "analyst": {"read", "analyze"},
    "support": {"read", "debug", "assist"},
    "manager": {"read", "approve_requests", "view_reports"},
    "accountant": {"read", "approve_payments", "generate_reports"},
    "security": {"read", "audit", "ban_users"},
    "editor": {"read", "write", "edit_content"},
    "admin": {"read", "write", "edit_users", "delete_system"},
    "cto": {"read", "write", "approve_architecture"},
    "ceo": {"read", "approve_requests", "override_security"},
    "hr": {"read", "manage_staff", "approve_leaves"},
}

# Тестові запити
test_requests = [
    ["developer", "manager"],       # Запит 1: обчислення
    ["manager", "developer"],       # Запит 2: кеш, має повернути той самий об'єкт
    ["guest"],                      # Запит 3: обчислення
    ["developer", "manager"],       # Запит 4: кеш
    ["intern"],                     # Запит 5: обчислення
    ["security", "editor"],         # Запит 6: обчислення
    ["editor", "security"],         # Запит 7: кеш
    ["cto"],                        # Запит 8: обчислення
    ["cto", "ceo"],                 # Запит 9: обчислення
    ["ceo", "cto"],                 # Запит 10: кеш
    ["hr"],                         # Запит 11: обчислення
    ["manager", "accountant"],      # Запит 12: обчислення
    ["accountant", "manager"],      # Запит 13: кеш
    ["developer", "analyst", "support"],  # Запит 14: обчислення
    ["support", "analyst", "developer"],  # Запит 15: кеш
]

permissions_cache = {}

def get_user_permissions(roles):
    key = frozenset(roles)

    if key in permissions_cache:
        print("received from cache")
        return permissions_cache[key]

    print("calculated permissions")

    final_permissions = set()

    for role in roles:
        if role in ROLE_PERMISSIONS:
            final_permissions |= ROLE_PERMISSIONS[role]

    permissions_cache[key] = final_permissions

    return final_permissions

for req_roles in test_requests:
    
    print(f"Roles: {req_roles} -> Permissions: {get_user_permissions(req_roles)}")