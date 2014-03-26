"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [
                [0, 1, 2],
                [-1, 0, 1],
                [-2, -1, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, 1, 2],
                [-1, 1, 1],
                [-2, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 1, 2],
                [-1, 0, 1],
                [-3, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 1, 1, 1, 1],
                [-1, 0, 1, 1, 1],
                [-1, -1, 0, 1, 1],
                [-1, -1, -1, 0, 1],
                [-1, -1, -1, -1, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, 2, 1, 1, 1],
                [-1, 0, 1, 1, 1],
                [-1, -1, 0, 1, 1],
                [-1, -1, -1, 0, 1],
                [-1, -1, -1, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 1, 2, 3, 4],
                [-1, 0, 5, 6, 7],
                [-2, -5, 0, 8, 9],
                [-3, -6, -8, 0, 0],
                [-4, -7, -9, 0, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, -1, -1, -1, -1],
                [1, 0, -1, -1, -1],
                [1, 1, 0, -1, -1],
                [1, 1, 1, 0, -1],
                [1, 1, 1, 1, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [5, 4, 1, 1, 2],
                [-1, 0, 1, 9, 1],
                [-1, -3, 0, 1, 4],
                [-6, 4, 1, 0, 1],
                [-5, -1, 2, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [9, 0, 0, 0, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0],
                [0, 0, 8, 0, 0],
                [0, 0, 0, 0, 0],
                [-9, 0, 0, 0, 0]
            ],
            "answer": False
        }
    ],
    "Extra": [
        {
            "input": [
                [0, 1, 3],
                [-1, 0, 1],
                [-3, -1, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, 1, 2],
                [-1, 9, 1],
                [-2, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 1, 3],
                [-1, 0, 1],
                [-3, -2, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 2, 2, 2, 2],
                [-2, 0, 2, 2, 2],
                [-2, -2, 0, 2, 2],
                [-2, -2, -2, 0, 2],
                [-2, -2, -2, -2, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, 3, 1, 1, 1],
                [-1, 0, 1, 1, 1],
                [-1, -1, 0, 1, 1],
                [-1, -1, -1, 0, 1],
                [-1, -1, -1, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 1, 2, 3, 4],
                [-1, 0, 5, 6, 7],
                [-2, -5, 0, 8, 0],
                [-3, -6, -8, 0, 9],
                [-4, -7, 0, -9, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [0, -2, -2, -2, -2],
                [2, 0, -2, -2, -2],
                [2, 2, 0, -2, -2],
                [2, 2, 2, 0, -2],
                [2, 2, 2, 2, 0]
            ],
            "answer": True
        },
        {
            "input": [
                [5, 4, 1, 1, 2],
                [-1, 0, 1, 9, 1],
                [-1, -3, 4, 1, 4],
                [-6, 4, 1, 3, 1],
                [-5, -1, 2, -1, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 0, 0, 0, 5],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [5, 0, 0, 0, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0],
                [0, 0, 7, 0, 0],
                [0, 0, 0, 0, 0],
                [-9, 0, 0, 0, 0]
            ],
            "answer": False
        },
        {
            "input": [
                [0]
            ],
            "answer": True
        },
        {
            "input": [
                [1]
            ],
            "answer": False
        },


    ]
}
