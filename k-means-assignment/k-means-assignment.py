def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    assignments = []
    for p in points:
        # reset the step distances per point
        step_distances = {}
        for i, c in enumerate(centroids):
            # distance to center
            if (len(p) & len(c)) == 1:
                step_distances[i] = (p[0] - c[0]) ** 2
            else:
                step_distances[i] = (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2
        # There could be an improvement for this function to accomdate,N-Dimensional data
        # get the min diatnce
        nearest_idx = min(step_distances, key=step_distances.get)
        assignments.append(nearest_idx)

    return assignments