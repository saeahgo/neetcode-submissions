from typing import List

# 각각 구현해내야 하는게 키! 그냥 단순히 복원이 아니라, encode할 때 length + # + str 형식으로 하는걸 빨리 캐치하는게 중요하다
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Read the length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # '#' next position

            res.append(s[j:j + length])
            i = j + length

        return res