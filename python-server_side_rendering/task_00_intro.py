import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data or "N/A"
        output_text = template

        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output_text = output_text.replace(f"{{{key}}}", str(value))

        # Create output file name
        filename = f"output_{index}.txt"

        # Optional: avoid overwriting existing files
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten.")

        # Write to file
        try:
            with open(filename, "w") as file:
                file.write(output_text)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

    print("Invitation files generated successfully.")