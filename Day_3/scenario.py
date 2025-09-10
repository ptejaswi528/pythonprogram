

def cleans(day_1, day_2, day_3):

    day_1_c = {email.lower() for email in day_1}
    day_2_c = {email.lower() for email in day_2}
    day_3_c = {email.lower() for email in day_3}
    return day_1_c, day_2_c, day_3_c

def total_unique(day_1_c, day_2_c, day_3_c):

    all_attendees = day_1_c.union(day_2_c).union(day_3_c)
    # FIX IS HERE: Use a comma to return two values
    return len(all_attendees), sorted(list(all_attendees))

def attended_all(day_1_c, day_2_c, day_3_c):
    all_three = day_1_c.intersection(day_2_c).intersection(day_3_c)
    return sorted(list(all_three))

def attended_exactly_one(day_1_c, day_2_c, day_3_c):
    only_day_1 = day_1_c - (day_2_c.union(day_3_c))
    only_day_2 = day_2_c - (day_1_c.union(day_3_c))
    only_day_3 = day_3_c - (day_1_c.union(day_2_c))
    exactly_one = only_day_1.union(only_day_2).union(only_day_3)
    return sorted(list(exactly_one))

def pairwise_overlap(day_1_c, day_2_c, day_3_c):
    day1_day2 = day_1_c.intersection(day_2_c)
    day2_day3 = day_2_c.intersection(day_3_c)
    day1_day3 = day_1_c.intersection(day_3_c)
    return {
        "d1_d2": (len(day1_day2), sorted(list(day1_day2))),
        "d2_d3": (len(day2_day3), sorted(list(day2_day3))),
        "d1_d3": (len(day1_day3), sorted(list(day1_day3))),
    }

def final_report(day_1, day_2, day_3):
    day_1_c, day_2_c, day_3_c = cleans(day_1, day_2, day_3)

    total_count, total_list = total_unique(day_1_c, day_2_c, day_3_c)
    all_three_list = attended_all(day_1_c, day_2_c, day_3_c)
    exactly_one_list = attended_exactly_one(day_1_c, day_2_c, day_3_c)
    pairwise_data = pairwise_overlap(day_1_c, day_2_c, day_3_c)

    print("--- Tech Workshop Attendance Report ---")
    
    print(f"\nTotal Unique Attendees: {total_count}")
    
    print("\nAttendees Who Attended All Three Days:")
    if all_three_list:
        for email in all_three_list:
            print(f"- {email}")
    else:
        print("None")
        
    print("\nAttendees Who Attended Exactly One Day:")
    if exactly_one_list:
        for email in exactly_one_list:
            print(f"- {email}")
    else:
        print("None")

    print("\n--- Pairwise Overlap ---")
    d1_d2_count, d1_d2_list = pairwise_data["d1_d2"]
    print(f"\nDay 1 & Day 2 Overlap: {d1_d2_count} attendee(s)")
    if d1_d2_list:
        for email in d1_d2_list:
            print(f"- {email}")
    else:
        print("None")
        
    d2_d3_count, d2_d3_list = pairwise_data["d2_d3"]
    print(f"\nDay 2 & Day 3 Overlap: {d2_d3_count} attendee(s)")
    if d2_d3_list:
        for email in d2_d3_list:
            print(f"- {email}")
    else:
        print("None")

    d1_d3_count, d1_d3_list = pairwise_data["d1_d3"]
    print(f"\nDay 1 & Day 3 Overlap: {d1_d3_count} attendee(s)")
    if d1_d3_list:
        for email in d1_d3_list:
            print(f"- {email}")
    else:
        print("None")
    
    print("\n--- End of Report ---")
day_1 = ["alice@example.com", "bob@example.com", "charlie@example.com", "ALICE@EXAMPLE.COM"]
day_2 = ["bob@example.com", "david@example.com", "eve@example.com"]
day_3 = ["charlie@example.com", "bob@example.com", "frank@example.com"]
final_report(day_1, day_2, day_3)