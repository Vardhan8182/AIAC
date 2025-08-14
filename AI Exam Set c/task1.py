import re

text = input("Enter the text: ")

# Regex pattern for URLs (http, https, www)
url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'

urls = re.findall(url_pattern, text)

print("Extracted URLs:")
for url in urls:
    print(url)
