class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            previous_row = self.getRow(rowIndex - 1)
            row = [1]
            for i in range(1, rowIndex):
                row.append(previous_row[i - 1] + previous_row[i])
            row.append(1)
            return row

        