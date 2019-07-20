# list your annotation
KEYPOINTS = [
    "Head",
    "LEyebrows",
    "REyebrows",
    "LEye",
    "REye",
    "Nose",
    "LWhiskers",
    "RWhiskers",
    "LHand",
    "RHand",
    "LTail",
    "RTail"
]

KEYPOINTS_MAP = {i: anno for i, anno in enumerate(KEYPOINTS)}

NUM_KEYPOINTS = len(KEYPOINTS)

COLOR_MAP = {
    "Head": (246, 13, 26),
    "LEyebrows": (140, 133, 26), "REyebrows": (167, 85, 20),
    "LEye": (225, 101, 73), "REye": (168, 9, 69),
    "Nose": (20, 133, 158),
    "LWhiskers": (0, 255, 255), "RWhiskers": (0, 170, 255),
    "LHand": (80, 238, 171), "RHand": (117, 243, 84),
    "LTail": (217, 83, 252), "RTail": (132, 78, 235),
}

assert sorted(KEYPOINTS) == sorted(list(COLOR_MAP.keys()))
