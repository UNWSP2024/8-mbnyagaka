# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def main():
    courses = {}

    while True:
        course_id = input("Enter course ID (or press Enter to stop): ").strip()
        if course_id == "":
            break
        course_name = input("Enter course name: ").strip()
        courses[course_id] = course_name

    subject = input("\nEnter a subject to search for (e.g., COS): ").strip().upper()

    print(f"\nCourses with subject '{subject}':")
    found = False
    for cid, cname in courses.items():
        if cid.upper().startswith(subject):
            print(f"  {cid} — {cname}")
            found = True

    if not found:
        print("  No courses found for that subject.")

main()