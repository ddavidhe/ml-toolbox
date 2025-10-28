import pandas as pd

# Code takes a Google doc (but a pub style? Honestly not sure) formatted as a table with x-coordinates, y-coordinates, and Unicode characters
# It then prints out each character into a grid, corresponding to the x and y coordinates
# Done for the DataAnnotations assessment

url = input("Provide link: ")
table = pd.read_html(url, header=0)

# character column encoding issue fix
def fix_encoding(val):
    if isinstance(val, str):
        try:
            return val.encode('latin1').decode('utf-8')
        except:
            return val
    return val
table[0]['Character'] = table[0]['Character'].apply(fix_encoding)


rows = table[0].sort_values(['y-coordinate', 'x-coordinate'], ascending=[False, True])


# establish boundaries of the grid
max_x = rows['x-coordinate'].max()
max_y = rows['y-coordinate'].max()

# fill with spaces
grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# slam characters into the grid
for i, row in rows.iterrows():
    grid[max_y - row['y-coordinate']][row['x-coordinate']] = row['Character']

# output
for line in grid:
    print("".join(line))
