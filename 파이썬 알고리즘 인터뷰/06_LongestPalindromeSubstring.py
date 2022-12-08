def longest_palindtome(s : str) -> str :
    def expaned( left : int , right : int ) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left  -= 1
            right += 1
        return s[ left+1 : right-1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range( len(s) -1 ):
        # 문자열의 길이만큼 범위를 줌, 홀짝의 범위를 체크하기 위해 [i,i+1]과 [i,i+2]범위를 비교
        result = max( result , expaned(i, i+1), expaned(i, i+2), key=len)
    return result

print(longest_palindtome('babadasdffdsaerwr'))