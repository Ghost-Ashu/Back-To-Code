#include <bits/stdc++.h>
using namespace std;

#define N 9

int row[N], col[N], box[N];
bool seted = false;

int getBox(int i, int j) { return i / 3 * 3 + j / 3; }

bool isSafe(int i, int j, int number)
{
  return !((row[i] >> number) & 1) && !((col[j] >> number) & 1) && !((box[getBox(i, j)] >> number) & 1);
}

void setInitialValues(int grid[N][N])
{
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      row[i] |= 1 << grid[i][j],
          col[j] |= 1 << grid[i][j],
          box[getBox(i, j)] |= 1 << grid[i][j];
}

bool SolveSudoku(int grid[N][N], int i, int j)
{
  // Set the initial values
  if (!seted)
    seted = true, setInitialValues(grid);

  if (i == N - 1 && j == N)
    return true;
  if (j == N)
    j = 0, i++;

  if (grid[i][j])
    return SolveSudoku(grid, i, j + 1);

  for (int nr = 1; nr <= N; nr++)
  {
    if (isSafe(i, j, nr))
    {

      grid[i][j] = nr;
      row[i] |= 1 << nr;
      col[j] |= 1 << nr;
      box[getBox(i, j)] |= 1 << nr;

      if (SolveSudoku(grid, i, j + 1))
        return true;

      row[i] &= ~(1 << nr);
      col[j] &= ~(1 << nr);
      box[getBox(i, j)] &= ~(1 << nr);
    }

    grid[i][j] = 0;
  }

  return false;
}

// Utility function to print the solved grid
void print(int grid[N][N])
{
  for (int i = 0; i < N; i++, cout << '\n')
    for (int j = 0; j < N; j++)
      cout << grid[i][j] << ' ';
}

// Driver Code
int main()
{

  int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                    {5, 2, 0, 0, 0, 0, 0, 0, 0},
                    {0, 8, 7, 0, 0, 0, 0, 3, 1},
                    {0, 0, 3, 0, 1, 0, 0, 8, 0},
                    {9, 0, 0, 8, 6, 3, 0, 0, 5},
                    {0, 5, 0, 0, 9, 0, 6, 0, 0},
                    {1, 3, 0, 0, 0, 0, 2, 5, 0},
                    {0, 0, 0, 0, 0, 0, 0, 7, 4},
                    {0, 0, 5, 2, 0, 6, 3, 0, 0}};

  if (SolveSudoku(grid, 0, 0))
    print(grid);
  else
    cout << "No solution exists\n";

  return 0;
}
