import re

def hackerrankInString(s):
    pattern = re.findall(r'h.*a.*.*c.*k.*e.*r.*.*r.*a.*n.*k',s)
    if len(pattern)>0:
            return 'YES'
    return 'NO'
