def extract_language(code):
    return code.split('_')[0]

print(extract_language('en_US.UTF-8'))      
print(extract_language('en_GB.UTF-8'))      
print(extract_language('ko_KR.UTF-16'))     