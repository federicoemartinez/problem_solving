# https://leetcode.com/problems/satisfiability-of-equality-equations/
from collections import defaultdict
class Solution(object):
    def equationsPossible(self, equations):
        group = {}
        member_to_groups = defaultdict(list)
        conflicts = list()
        for each in equations:
            var_1, nor_or_equal,_,var_2 = each
            var_1, var_2 = min(var_1, var_2), max(var_1,var_2)
            if nor_or_equal == "=":
                if var_1 not in group:
                    group[var_1] = var_1
                    member_to_groups[var_1].append(var_1)
                if var_2 in group and group[var_1] != group[var_2]:
                        var_2_friends = member_to_groups[group[var_2]]
                        del member_to_groups[group[var_2]]
                        for friend in var_2_friends:
                            group[friend] = group[var_1]
                            member_to_groups[group[var_1]].append(friend)
                elif var_2 not in group:
                        group[var_2] = group[var_1]
                        member_to_groups[group[var_1]].append(var_2)     
            else:
                conflicts.append((var_1, var_2))
        for var_1, var_2 in conflicts:
            if group.get(var_1, var_1) == group.get(var_2,var_2): return False
        return True
            
