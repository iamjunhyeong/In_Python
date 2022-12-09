h = [0,1,0,2,1,0,1,3,2,1,2,1]
volume = 0

left = 0
right = len(h) - 1
left_max, right_max = h[left], h[right]

while left < right:
    left_max, right_max = max(left_max, h[left]), max(right_max, h[right])

    if left_max <= right_max:
        volume += left_max - h[left]
        left += 1
    else:
        volume += right_max - h[right]
        right -= 1
    
print(volume)
    