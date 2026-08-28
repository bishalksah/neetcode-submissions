class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move after '#'
            i = j + 1

            # Extract exactly 'length' characters
            result.append(s[i:i + length])

            # Move to the beginning of next encoded string
            i = i + length
        return result