import os
import re

keys_to_remove = [
    "event_dates",
    "location",
    "registration_status",
    "contact_name",
    "contact_email",
    "contact_phone",
    "contact_phone_link",
    "flyer_pdf"
]

md_files = [f for f in os.listdir('.') if f.endswith('.md')]

for file in md_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_lines = []
    in_frontmatter = False
    lines = content.split('\n')
    
    if lines and lines[0] == '---':
        in_frontmatter = True
        new_lines.append(lines[0])
        for line in lines[1:]:
            if in_frontmatter:
                if line == '---':
                    in_frontmatter = False
                    new_lines.append(line)
                    continue
                
                # Check if line starts with any of the keys
                should_remove = False
                for key in keys_to_remove:
                    if line.startswith(f"{key}:"):
                        should_remove = True
                        break
                
                if not should_remove:
                    new_lines.append(line)
            else:
                new_lines.append(line)
    
        new_content = '\n'.join(new_lines)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
print("Cleanup complete.")
