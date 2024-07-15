import os
"""
Create a Python function that generates personalized invitation files from a
template with placeholders and a list of objects.
Each output file should be named sequentially, starting from 1.
Implement specific error handling for various edge cases.
"""


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """

    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Check if the attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees should be a list.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over each attendee and create a personalized invitation
    for index, attendee in enumerate(attendees, start=1):
        # Ensure each attendee is a dictionary
        if not isinstance(attendee, dict):
            print(
                f"Error: Each attendee should be a dictionary. Skipping attendee at index {index}.")
            continue

        # Replace placeholders with actual values or "N/A"
        personalized_invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Generate the filename
        output_filename = f"output_{index}.txt"

        # Write the personalized invitation to a file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_invitation)
            print(f"Generated file: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")


# Example main file content to test the program
if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
            "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
            "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
            "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
