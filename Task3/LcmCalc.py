def calc_gcd(x, y) -> int:
    if y == 0:
        return x
    return calc_gcd(y, x % y)


def calc_lcm(x, y) -> int:
    gcd = calc_gcd(x, y)
    return int((x * y) / gcd)


def calc_lcm_from_list(nums: list) -> int:
    if len(nums) < 2:
        return -1
    lcm = calc_lcm(nums[0], nums[1])
    for i in range(2, len(nums)):
        lcm = calc_lcm(lcm, nums[i])
    return lcm


if __name__ == '__main__':
    print(calc_lcm_from_list([4, 5, 6, 7]))
