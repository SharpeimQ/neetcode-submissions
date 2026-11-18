class Solution:

    # length-prefix encoding
    # encode the length + # before the string for easy decoding
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string

        return result

    # length-prefix decoding
    # decode by:
    # two pointers, i and j
    # shift j until you find delimiter
    # extract the length as it sits between i and j, convert to integer
    # start is j + 1
    # end is start + length
    # append the string to the result array
    # update i position accordingly
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end
        
        return result



