#https://leetcode.com/problems/unique-email-addresses/
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def process_address(adrr):
            name, domain = adrr.split("@",1)
            name_plus = name.split("+",1)
            if len(name_plus) > 1:
                name, _ = name_plus
            else:
                name = name_plus[0]
            name = name.replace(".","")
            return (name, domain)
        s = set((process_address(addr) for addr in emails))
        return len(s)
            
