import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the .hero-photo-inner class style rule block and replace the base64 background url with hero.jpg
# The pattern should match .hero-photo-inner { followed by width, height, and background url, up to the ending of that rule or next lines.
# Specifically, we want to replace the url('data:image/png;base64,...') with url('hero.jpg')
pattern = r"(\.hero-photo-inner\s*\{[^}]*background:\s*url\(')[^']+(\'\))"

new_content, count = re.subn(pattern, r"\g<1>hero.jpg\g<2>", content)
print(f"Replaced {count} occurrences using regex.")

# If regex subn count is 0, let's try a string split/replace based on the start and end of .hero-photo-inner style rule
if count == 0:
    start_idx = content.find(".hero-photo-inner {")
    if start_idx != -1:
        end_idx = content.find("}", start_idx)
        if end_idx != -1:
            style_block = content[start_idx:end_idx+1]
            print("Found style block:")
            print(style_block[:100] + "..." + style_block[-50:])
            # Replace the background url in this style block
            # Matches url('...') or url("...") or url(...)
            bg_pattern = r"(background:\s*url\(['\"]?)[^'\"]+(['\"]?\))"
            new_style_block = re.sub(bg_pattern, r"\g<1>hero.jpg\g<2>", style_block)
            new_content = content[:start_idx] + new_style_block + content[end_idx+1:]
            count = 1
            print("Replaced style block manually.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
