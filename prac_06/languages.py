from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

dynamic_languages = []
if ruby.is_dynamic():
    dynamic_languages.append(ruby.name)
if python.is_dynamic():
    dynamic_languages.append(python.name)
if visual_basic.is_dynamic():
    dynamic_languages.append(visual_basic.name)

print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language)

