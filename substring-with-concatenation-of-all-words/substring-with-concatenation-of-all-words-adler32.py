from typing import List
import itertools

def rolling_adler32(st, l=None, r=None, cksum=1):
    MODADLER = 65521
    #print(" ", st, l, r, cksum)
    if cksum == 1:
        a = 1
        b = 0
    else:
        a = cksum & 0xffff
        b = (cksum & 0xffff0000) >> 16
        #print("{:8x} {:8x}".format(a, b))
        if l and r:
            a += (r - l)
            a = a % MODADLER
            b += r
            b -= (1+len(st)) * l
            for x in st:
                b += ord(x[0])
            b = b % MODADLER
            return (b << 16) + a
    for x in st:
        a = (a + ord(x[0])) % MODADLER
        b = (a + b) % MODADLER
    return (b << 16) + a

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target_hashes = []
        target_strings = []
        for perm in itertools.permutations(words):
            s1 = 1
            for x in perm:
                s1 = rolling_adler32(x, cksum=s1)
            target_hashes.append(s1)
            target_strings.append("".join(perm))
            #print(perm, ":", s1)
        if len(words) == 0:
            return []
        fullen = len(words) * len(words[0])
        if len(s) < fullen:
            return []
        adler = 1
        solution = []
        for win in range(len(s) - fullen + 1):
            if win == 0:
                adler = rolling_adler32(s[win:(win+fullen)])
            else:
                adler = rolling_adler32(s[win:(win+fullen-1)], ord(s[win-1]), \
                                        ord(s[win+fullen-1]), adler)
            #print(adler, s[win:win+fullen], rolling_adler32(s[win:win+fullen]))
            for idx, x in enumerate(target_hashes):
                if adler == x:
                    if s[win:win+fullen] == target_strings[idx]:
                        solution.append(win)
                        break
        return solution

if __name__ == "__main__":
    S = Solution()
    # print(S.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
    # print(S.findSubstring(s = "wordgoodgoodgoodbestword",  words = ["word","good","best","word"]))
    # print(S.findSubstring(s = "barfoofoobarthefoobarman", words =["bar","foo","the"]))
    # print(S.findSubstring(s="wordgoodgoodgoodbestword", words=["word","good","best","good"]))
    print(S.findSubstring(s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", \
                          words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]))
