#My name is Jacob Baker and this is Chapter 9 and 10 Lab 1 which I am completing on July 8
print ("Name Processor" )


def fix_capitalization(name):
    return ' '.join(part.capitalize() for part in name.strip().split())

def format_full_name(name):
    name = name.strip()

    if ',' in name:
        parts = name.split(',')
        if len(parts) == 2:
            last = fix_capitalization(parts[0])
            first = fix_capitalization(parts[1])
            return f"{last}, {first}"
        else:
            return fix_capitalization(name)
    else:
        parts = name.split()
        if len(parts) == 2:
            first = fix_capitalization(parts[0])
            last = fix_capitalization(parts[1])
            return f"{last}, {first}"
        else:
            return fix_capitalization(name)

def main():
    user_input = input("Enter your full name: ")
    formatted = format_full_name(user_input)
    print (formatted)

main()


