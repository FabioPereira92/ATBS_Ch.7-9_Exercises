import re

def regexVersionOfStrip(s: str, chars: str | None = None) -> str:
    """
    Regex version of str.strip:
    - If chars is None: remove leading/trailing whitespace.
    - If chars == '': return s unchanged (same as str.strip('')).
    - Else: remove any leading/trailing characters that are in `chars`.
    """
    if chars is None:
        # strip whitespace on both ends
        return re.sub(r'^\s+|\s+$', '', s)

    if chars == '':
        # str.strip('') leaves the string unchanged
        return s

    # strip any of the given characters from both ends
    escaped = re.escape(chars)         # treat chars literally inside [...]
    pattern = rf'^[{escaped}]+|[{escaped}]+$'
    return re.sub(pattern, '', s)


# Examples
print(regexVersionOfStrip('      asdfsdf     '))         # -> 'asdfsdf'
print(regexVersionOfStrip('---hello---', '-'))           # -> 'hello'
print(regexVersionOfStrip('xyxabcxyz', 'xyz'))           # -> 'abc'
print(regexVersionOfStrip('[]]hello[[]', '[]'))          # -> 'hello'
print(regexVersionOfStrip('abc', ''))                    # -> 'abc'
