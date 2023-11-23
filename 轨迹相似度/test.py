import frechet_distance_curve

if __name__ == "__main__":
    c1 = [(0.45, 1.6),  (4.9, 1.5), (3.9, 1.5)]
    c2 = [(0.45, 1.6), (2.7, 1.6), (2.7, 1.1), (3.7, 1.6)]
    if len(c1) != 0 and len(c2) != 0:
        frechet_distance_curve.test_2d_curve(c1, c2)
    else:
        print("error: can not input empty!")