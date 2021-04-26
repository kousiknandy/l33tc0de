import re
import os

phone_pattern = re.compile("""
\(?
\d{3}
\)?
-
\d{3}
-
\d{4}
""", re.VERBOSE)

def matching_files(directory="."):
    for d_name, d_subdir, file_names in os.walk(directory):
        for fn in file_names:
            fn = os.path.join(d_name, fn)
            # print("     ", fn)
            with open(fn) as f:
                for l in f.readlines():
                    l = l.strip()
                    # print("         ", l, end="")
                    if phone_pattern.match(l):
                        # print(" Ok")
                        yield fn
                        break

for f in matching_files("."):
    print(f)
