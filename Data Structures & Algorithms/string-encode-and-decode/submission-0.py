class Solution:

    # length-prefix encoding
    # 3#cat4#dogo
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result

    # length-prefix decoding
    # shift j until delim is found
    # range between i and j is length, convert to int
    # start of string is j + 1
    # end of string is start + length
    # append string to output array
    # set i to end of string
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

