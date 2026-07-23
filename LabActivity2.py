def check_fast_lane(time_remaining, item_count, has_pass):
   
    if has_pass:
        return "Fast lane approved"
    #
    elif time_remaining < 10 and item_count <= 3:
        return "Fast lane approved"
    
    else:
        return f"Use regular line (You have {time_remaining} minutes left)"

queue_list = [
    {"name": "Marco", "time_remaining": 8, "item_count": 2, "has_pass": False},
    {"name": "Diane", "time_remaining": 15, "item_count": 1, "has_pass": False},
    {"name": "Kyle", "time_remaining": 5, "item_count": 6, "has_pass": False},
    {"name": "Ella", "time_remaining": 20, "item_count": 5, "has_pass": True},
]

approved_fast_lane_count = 0

print("=== Cafeteria Fast Lane Queue Evaluation ===\n")


for student in queue_list:
    student_name = student["name"]
    result = check_fast_lane(
        student["time_remaining"], 
        student["item_count"], 
        student["has_pass"]
    )
    
    print(f"{student_name}: {result}")
    

    if "Fast lane approved" in result:
        approved_fast_lane_count += 1

print(f"Total students approved for Fast Lane: {approved_fast_lane_count}")
