def largest_rectangle1(heights):
    max_area = 0
    for i in range(len(heights)):
        left = i
        while left-1 >= 0 and heights[left-1] >= heights[i]:
            left -= 1
        right = i
        while right+1 < len(heights) and heights[right+1] >= heights[i]:
            right += 1
        max_area = max(max_area, heights[i]*(right-left))
    return max_area

def rec(heights, low, high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh = min(heights[low:high+1])
        pos_min = heights.index(minh, low, high+1)
        from_left = rec(heights, low, pos_min-1)
        from_right = rec(heights, pos_min+1, high)
        return max(from_left, from_right, minh * (high - low))
    
def largest_rectangle2(heights):
    return rec(heights, 0, len(heights)-1)

def largest_rectangle4(heights):
    heights = [-1]+heights+[-1]
    max_area = 0
    stack = [(0, -1)]
    for i in range(1, len(heights)):
        start = i
        while stack[-1][1] > heights[i]:
            top_index, top_height = stack.pop()
            max_area = max(max_area, top_height*(i-top_index-1))
            start = top_index
        stack.append((start, heights[i]))
    return max_area

heights=[3,2,4,5,7,6,1,3,8,9,10,11,10,7,5,2,6]
print(largest_rectangle1(heights))
print(largest_rectangle2(heights))
print(largest_rectangle4(heights))