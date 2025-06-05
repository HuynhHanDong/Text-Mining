import re

with open("regex.txt", "r") as f:
    text = f.read()

# a. Remove repeated spaces or tabs
text = re.sub(r'[ \t]+', ' ', text)

# b. Remove repeated words (case-insensitive)
text = re.sub(r'\b(\w+)(?:\s+\1\b)+', r'\1', text, flags=re.IGNORECASE)

# c. Remove repeated sentences
text = re.sub(r'(\b[^.?!]+[.?!])(?:\s*\1)+', r'\1', text)

# d. Extract dates
dates = re.findall(r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\w{3,9} \d{2},? \d{4})\b', text)

# e. Extract all UPPERCASE words
uppercase_words = re.findall(r'\b[A-Z]{2,}\b', text)

# f. Extract addresses that start with digits and end with "City" or "HCMC"
addresses = re.findall(r'\b\d+[^\n]*?(?:City|HCMC)\b', text)

# g. Extract email addresses
emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)

# h. Extract all quoted texts (single or double)
quoted = re.findall(r'[\'"]([^\'"]+)[\'"]', text)

# i. Extract and reformat phone numbers
pattern = r'\b(\d{3})-(\d{3})-(\d{4})\b'
def format_phone(m):
    return f"({m.group(1)}) {m.group(2)} {m.group(3)}"
text = re.sub(pattern, format_phone, text)
phone_numbers = re.findall(r'\(\d{3}\) \d{3} \d{4}', text)

# j. Extract proper names (assumes capitalized words)
proper_names = re.findall(r'\b([A-Z][a-z]+(?: [A-Z][a-z.]+)+)\b', text)

# k. Extract all topics like: # Topic 1: News #
topics = re.findall(r'#\s*Topic\s*\d+:[^#]+#', text)

# l. Extract content of each topic (assume each topic is followed by a paragraph)
topic_contents = re.findall(r'#\s*Topic\s*\d+:[^#]+#\s*(.*?)(?=\n#|$)', text, flags=re.DOTALL)

# Print results:
print("Document after proccessing:")
print("-"*30)
print(text)
print("-"*30)
print("Dates:", dates)
print("UPPERCASE Words:", uppercase_words)
print("Addresses:", addresses)
print("Emails:", emails)
print("Quoted:", quoted)
print("Phone numbers:", phone_numbers)
print("Proper Names:", proper_names)
print("Topics:", topics)
print("Topic Contents:", topic_contents)
