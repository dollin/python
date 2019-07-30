
"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists,
return null. All flights must be used in the itinerary.

For example, given the following list of flights:

HNL ➔ AKL
YUL ➔ ORD
ORD ➔ SFO
SFO ➔ HNL
"""
def get_itinerary(flights, current_itinerary):
    # If we've used up all the flights, we're done
    if not flights:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        # Make a copy of flights without the current one to mark it as used
        flights_minus_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()
    return None


c = ["b"]
f = [["c", "e"], ["b", "d"], ["d", "c"]]

print(get_itinerary(f, c))
