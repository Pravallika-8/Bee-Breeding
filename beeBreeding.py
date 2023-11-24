coordinates = [[1,0,-1],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0]]
coordinates = [[1, 0, -1], [0, 1, -1], [-1, 1, 0], [-1, 0, 1], [0, -1, 1], [1, -1, 0]]
RADIUS = 58

def shortestDistance(cellsDict, cell_num1, cell_num2):
    x1, y1, z1 = cellsDict[cell_num1]
    x2, y2, z2 = cellsDict[cell_num2]

    return (abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)) // 2

def createGrid(radius):
    cell_num = 1
    cellsDict = {}
    x_coord, y_coord, z_coord = 0, 0, 0
    cellsDict[cell_num] = x_coord, y_coord, z_coord

    for rad in range(radius):
        x_coord = 0
        y_coord = -rad
        z_coord = rad
        for i in range(6):
            for j in range(rad):
                x_coord += coordinates[i][0]
                y_coord += coordinates[i][1]
                z_coord += coordinates[i][2]
                cell_num += 1
                cellsDict[cell_num] = x_coord, y_coord, z_coord

    return cellsDict
 
while(True):
    cell_num1, cell_num2 = map(int, input().split())
    if cell_num1 == 0 and cell_num2 == 0:
        break
    else:
        print(shortestDistance(createGrid(RADIUS), cell_num1, cell_num2))
