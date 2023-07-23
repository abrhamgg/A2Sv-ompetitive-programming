class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        def add_to_obj(obj, key, val):
            if key in obj.keys():
                obj[key] += val
            else:
                obj[key] = val
        dom = {}
        result = []
        for i in cpdomains:
            cd = i.split(" ")
            if cd[1] in dom.keys():
                dom[cd[1]] += int(cd[0])
            else:
                dom[cd[1]] = int(cd[0])
            sdm = cd[1].split(".")
            if len(sdm) == 2:
                add_to_obj(dom, sdm[1], int(cd[0]))
            else:
                add_to_obj(dom, sdm[2], int(cd[0]))
                k = sdm[1] + '.' + sdm[2]
                add_to_obj(dom, k, int(cd[0]))
        for key,val in dom.items():
            r = str(val) + " " + key
            result.append(r)
        return result
