import plotFunc
import bf

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


def sudoku(puzzle):
    plotFunc.plot_zero_values(bf.get_zeros_plus_value(puzzle))
    plotFunc.plot_rows_avgvalue(bf.get_rows_avgvalue(puzzle))
    plotFunc.plt.show()
    return 0


print(sudoku(puzzle))

