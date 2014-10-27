SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = '⚑'
EMPTY = '◠'


def render_grid(grid):
    """
    Draw grid on command line terminal.
    """
    #make column headers = abc's
    line = '   '
    for a in ABC:
        line += a
        line += ' '
    print(line)
    # add row header and row
    for i in range(1, LIMIT + 1):
        # if row header # is one digit
        # add a space before printing to align with
        # two digit header
        line = ' ' if len(str(i)) == 1 else ''
        # add header (ie '5')
        line += str(i)
        line += ' '
        # add row cells
        for a in ABC:
            node = grid.grid[a][i]
            if node.ship:
                if node.hit:
                    line += HIT
                else:
                    line += SHIP_MARKER
            else:
                if node.hit:
                    line += ENEMY_MISS
                else:
                    line += EMPTY
            line += ' '
        #print row and cell
        print(line)