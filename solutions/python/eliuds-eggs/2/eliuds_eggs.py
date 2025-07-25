def egg_count(display_value):
    count = 0
    remaining = display_value
    while remaining > 0:
        count += remaining & 1
        remaining = remaining >> 1
    return count
