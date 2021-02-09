class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        palindromes = [[ False for _ in range(size) ] for _ in range(size)]
        result = (0, 0)
        for i in range(size):
            palindromes[i][i] = True
            if i < size-1:
                if s[i] == s[i+1]:
                    palindromes[i][i+1] = True
                    result = (i, i+1)
        for j in range(2,size):
            for i in range(size):
                if i+j >= size: break
                if s[i] == s[i+j]:
                    #print(i, i+j, palindromes[i+1][i+j-1])
                    palindromes[i][i+j] = palindromes[i+1][i+j-1]
                    if palindromes[i][i+j] and j > (result[1] - result[0]):
                        result = (i, i+j)
                else:
                    palindromes[i][i+j] = False
        #for p in palindromes: print(p)
        return s[result[0]:result[1]+1]
        
S = Solution()
print(S.longestPalindrome("axbcdefedcby")) #2,10
#print(S.longestPalindrome(
print(S.longestPalindrome("cbbd"))
print(S.longestPalindrome("123456789987654300"))
print(S.longestPalindrome("lfzwymgfcaqlozazylwpafzwgjhxbibllvdgsaiadtpryangehchkwkprhzpbszkobjcfmhffqxdcvghqftqyxorllrrheptcrhhlhrytwkytqmqlnvgoogjdlejnslpehtndmounvrtxplzyzlvcyuviknxoyhomwjzigiufhwqmjnwqpuukcxxhatxrgqiayqkkuwbxxbyejvxjpiflbeqjqemvkzcayitimalelkqmvrydiknqeghabhfuogujutrnzkmqqphbnrbnxhlgotbyghsbgmxschmbuhkobwvwajkcghrmgvvfzmxmaihcenxerznbnkotjubqxhbfqrcwsyfeowixusgfdgreywudrxjbylrnydtpfawayptifhlbmvrklplxahkxqahqalwsivszwvblpnozfmabzmouaxxbvbsibbzirgiqurhoitzlmpsovcjnkbeeydtkpelxmaulsvozwomofyvcafcenaprlnfxhvvkwpuyycqokybyqrujpdgpnpqcfrmdunejkidxpkdipigmkqwasfdewnhumokvubzqxserhpsxoskmvhsflmtvootrhpnjguqmqhpuiosqpiwmmahvuimwcquktrfnniybyhuftrfzqpmvvklgoilbwvtvaprddkwiwiezxarnxnzgqzqxhseodyyleerusznmmyxxvlmokiyhpsghcububxzrglgskrkbagamwvxxrkplpjrcsxvvvcjmjzsemvjvfmesckkrfabzfxxzmwthxldyoyhbsdsqmrugnsyracggnsextkzjqyivpiiambvsulqjefbheakvwkffcvjnuvkgusnawxdtibaycabnzeobaljpfhlhbaismpplqckycavmhttyakpngcnuawxdwwfhswyllbbhbkmuvgdu"))

        
