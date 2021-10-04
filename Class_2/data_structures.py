"""
Porkland is a community of pigs who live in n houses lined up along one side of a long, straight
street running east to west. Every house in Porkland was built from straw and bricks, but some
houses were built with more bricks than others. One day, a wolf arrives in Porkland and all the
pigs run inside their homes to hide. Unfortunately for the pigs, this wolf is extremely skilled at
blowing down pig houses, aided by a strong wind already blowing from west to east. If the wolf
blows in an easterly direction on a house containing b bricks, that house will fall down, along with
every house east of it containing strictly fewer than b bricks. For every house in Porkland, the wolf
wants to know its damage, i.e., the number of houses that would fall were he to blow on it in an
easterly direction.

(a) Suppose n = 10 and the number of bricks in each house in Porkland from west to east
is [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]. Compute for this instance the
damage for every house in Porkland.

(b) A house in Porkland is special if it either (1) has no easterly neighbor or (2) its adjacent neighbor to the east contains at least as many bricks as it does. Given an array
containing the number of bricks in each house of Porkland, describe an O(n)-time
algorithm to return the damage for every house in Porkland when all but one house
in Porkland is special.

(c) Given an array containing the number of bricks in each house of Porkland, describe
an O(n log n)-time algorithm to return the damage for every house in Porkland.

(d) Write a Python function get damages that implements your algorithm. 
"""


# Wind blows west to east
# Wolf blows from west to east
# Wolf picks a house, every house to the east of it with less bricks also falls down
# For each house, return the damages the wolf would get if he blew it down

# Input: H | list of bricks per house from west to east
# Output: D | list of damage per house from west to east
# Must run in O(n log n) time

def get_damages_O_n_squared(houses):
    damages = [1 for _ in houses]
    
    for i in range(len(houses)):
        for j in range(i, len(houses)):
            if houses[j] < houses[i]:
                damages[i] += 1
    return damages

def get_damages_O_n_log_n(houses):
    damages = [1 for _ in houses]
    housePairs = [(houses[i], i) for i in range(len(houses))]

    def special_merge_sort(A, a = 0, b = None):
        if b is None: b = len(A)
        if 1 < b - a:
            mid = (a + b + 1) // 2
            special_merge_sort(A, a, mid)
            special_merge_sort(A, mid, b)

            i, j = 0, 0
            L, R = A[a:mid], A[mid:b]
            while a < b:
                if (j >= len(R)) or (i < len(L) and L[i][0] <= R[j][0]):
                    damages[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                else:
                    A[a] = R[j]
                    j += 1
                a += 1

    special_merge_sort(housePairs)
    return damages

houses = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
slowDamages = get_damages_O_n_squared(houses)
fastDamages = get_damages_O_n_log_n(houses)
print(f"O(n^2):      Damages: {slowDamages}.  Houses: {houses}")
print(f"O(n log(n)): Damages: {fastDamages}.  Houses: {houses}")
print (f"Equal?: {slowDamages == fastDamages}")