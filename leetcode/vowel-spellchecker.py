# https://leetcode.com/problems/vowel-spellchecker/
import re
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        d = {}
        d_vowels = {}
        for each in wordlist:
            lower_each = each.lower()
            if lower_each not in d:
                d[lower_each] = (set(), [each])
            d[lower_each][0].add(each)
            without_vowel_each = re.sub('[aeiou]', 'a', lower_each, flags=re.I)
            if without_vowel_each not in d_vowels:
                d_vowels[without_vowel_each] = (set(), [each])
            d_vowels[without_vowel_each][0].add(each)
        res = []
        for each in queries:
            lower_each = each.lower()
            if lower_each in d:
                s,l = d[lower_each]
                if each in s:
                    res.append(each)
                else:
                    res.append(l[0])
            else:
                without_vowel_each = re.sub('[aeiou]', 'a', lower_each, flags=re.I)
                if without_vowel_each in d_vowels:
                    s, l = d_vowels[without_vowel_each]
                    if each in s:
                        res.append(each)
                    else:
                        res.append(l[0])
                else:
                    res.append("")
        return res
                
                
