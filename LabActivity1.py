def check_borrowing(is_overdue, member_status):
   
    if is_overdue == "yes":
        return "Not allowed: overdue books"
    elif member_status == "suspended":
        return "Not allowed: suspended account"
    elif member_status == "active" and is_overdue == "no":
        return "Borrowing allowed"
    else:
        return "Not allowed: invalid status"


successful_borrowers_count = 0

print("Welcome to Aliah's Interactive Library Kiosk ")

while True:
    student_name = input("\nEnter your name (or type 'exit' to quit): ").strip()
    
   
    if student_name.lower() == "exit":
        break
        
    has_unreturned = input("Do you have overdue books? (yes/no): ").strip().lower()
    account_state = input("Enter your account status (active/suspended): ").strip().lower()
    
    
    try:
        requested_qty = int(input("How many books do you want to borrow?: ").strip())
    except ValueError:
        print("Invalid input for book quantity. Please enter a number.")
        continue

   
    borrow_result = check_borrowing(has_unreturned, account_state)
    
    if borrow_result == "Borrowing allowed":
       
        if requested_qty <= 0:
            print("Notice: You must request at least 1 book to borrow.")
        else:
          
            if requested_qty > 3:
                print("Warning: Maximum limit is 3 books per transaction. Your request has been capped at 3.")
                allowed_qty = 3
            else:
                allowed_qty = requested_qty
                
            print(f"Success! {student_name}, you are allowed to borrow {allowed_qty} book(s).")
            successful_borrowers_count += 1
    else:
        print(f"Transaction Result: {borrow_result}")

print("Kiosk Session Ended.")
print(f"Total students allowed to borrow books: {successful_borrowers_count}")
