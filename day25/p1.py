decode = lambda s: decode(s[:-1]) * 5 + '=-012'.find(s[-1]) - 2 if s else 0
encode = lambda d: encode((d + 2) // 5) + '=-012'[(d + 2) % 5] if d else ''

print(encode(sum(map(decode, open('inp').read().split()))))
