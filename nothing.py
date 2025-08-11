import json
pas_list = "D:/UNIVERSTIY/ai project/python/ending_project/save_directory_tech/pas.json"
professors = [
    {"name": "Dr. Alavi", "professor_id": "123456", "password": "A1l2v3!#"},
    {"name": "Dr. Moradi", "professor_id": "234567", "password": "M9o8r7@#"},
    {"name": "Dr. Sharifi", "professor_id": "345678", "password": "S5h6a7$%"},
    {"name": "Dr. Khademi", "professor_id": "456789", "password": "K3h4d5&*"}
]

with open(pas_list, "w") as file:
    json.dump(professors, file, indent=4)