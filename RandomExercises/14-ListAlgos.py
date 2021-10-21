
#linear
def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None

    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

# print(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]))
# print(remove_adjacent_dups([]))
# print(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]))

def merge(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

            