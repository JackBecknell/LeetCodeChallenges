// LeetCode problem 36
// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:

// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.
let breakPoint = 1;
function isValidSudoku(board) {
  for (let i = 1; i < 10; i++) {
    let gridPosContext;
    switch (i) {
      case 1:
        gridPosContext = [
          [0, 2],
          [0, 2],
        ];
        break;
      case 2:
        gridPosContext = 1;
        break;
      case 3:
        gridPosContext = 1;
        break;
      case 4:
        gridPosContext = 1;
        break;
      case 5:
        gridPosContext = 1;
        break;
      case 6:
        gridPosContext = 1;
        break;
      case 7:
        gridPosContext = 1;
        break;
      case 8:
        gridPosContext = 1;
        break;
      case 9:
        gridPosContext = 1;
        break;
    }
    let checkLists = [];
    let checkValues = [];
    let index = gridPosContext[0][0];
    // This is where I am running into a problem, something regarding my indexing is off.
    while (index !== gridPosContext[0][1] + 1) {
      checkLists.push(board[0][index]);
      index++;
    }
    for (list in checkList) {
      for (let i2 = gridPosContext[1][0]; i2 < gridPosContext[1][1] + 1; i2++) {
        if (list[i2] === ".") {
          continue;
        } else {
          checkValues.append(list[i2]);
        }
      }
    }
    console.log(checkValues);
  }
}

let answer = isValidSudoku([
  [
    [
      ["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
  ],
]);
// This video is driving me alittle bit crazy
