import ACO
import numpy as np

# 旅行商测试矩阵
# 	1	2	3	4	5	6
# 1	0	6	2	1	MAX	MAX
# 2	6	0	6	MAX	3	MAX
# 3	2	6	0	2	2	4
# 4	1	MAX	2	0	MAX	5
# 5	MAX	3	2	MAX	0	3
# 6	MAX	MAX	4	5	3	0



# 旅行商初始化函数，总共6个城市
def InitD():
    cityNum = 11
    coordinate = [
        (120.226687, 31.523240),
        (114.365248, 30.537860),
        (39.925327,116.298111
),
        (120.352370, 36.064990
),
        (102.711898, 25.051640
),
        (106.627802, 29.555423
),
        (120.143570,30.227910
),
        (121.261953,38.851705
),
        (121.397743,31.347715
),
        (106.782973,27.354407
),
        (121.516566,30.836661
),
    ]
    MAX_INT = 1e8
    point = np.array(
        [
            [0, 6, 2, 1, MAX_INT, MAX_INT],
            [6, 0, 6, MAX_INT, 3, MAX_INT],
            [2, 6, 0, 2, 2, 4],
            [1, MAX_INT, 2, 0, MAX_INT, 5],
            [MAX_INT, 3, 2, MAX_INT, 0, 3],
            [MAX_INT, MAX_INT, 4, 5, 3, 0],
        ]
    )

    return cityNum, coordinate, point


def ACOTest():
    cityNum, coordinate, point = InitD()
    ACO.antColonyOptimization(
        cityNum,
        coordinate,
        point,
        setting={
            "iter_max": 300,
            "ifOptimanation": False,
            "threshold": 6,
            "skipNum": 20,
        },
    )


if __name__ == "__main__":
    ACOTest()
