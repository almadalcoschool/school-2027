import os
import re

new_box = """<div class="fixed-box">
    <strong>Date:</strong> {{ site.event_dates }}<br>
    <strong>Location:</strong> {{ site.location }}<br>
    <strong>Registration:</strong> {{ site.registration_status }}<br>
    <strong style="color: black;">Contacts:</strong> <a href="mailto:{{ site.contact_email }}" style="color: black;">{{ site.contact_name }}</a>, <a href="{{ site.contact_phone_link }}" style="color: black;">{{ site.contact_phone }}</a><br>
    <a href="{{ site.baseurl }}/{{ site.flyer_pdf }}" download="POSTER.pdf" style="color: black;"><strong style="color: black;">ADC school's flyer</strong></a><br>
</div>"""

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != "404.html"]

# We will regex `<div class="fixed-box">.*?</div>` (non greedy), dotall so it matches newlines
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the exact block
    # Look for `<div class="fixed-box">` and the first `</div>` after it
    new_content = re.sub(r'<div class="fixed-box">.*?</div>', new_box, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Updated {file}")

print("Done updating HTML files.")
