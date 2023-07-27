import string


def licenseKeyFormatting(s: str, k: int):
    s = s.replace("-", "").upper()

    first_group_len = len(s) % k

    reformatted = s[:first_group_len]

    for i in range(first_group_len, len(s), k):
        if reformatted:
            reformatted += "-"
        reformatted += s[i:i + k]

    return reformatted

print(licenseKeyFormatting("2-4A0r7-4k", 4))
