class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sen = s.split(' ')
        new_dic = {}
        new_sentence = ""
        for s in sen:
            key = s[-1]
            s = s[:-1]
            new_dic[key] = s
        new_dic = sorted(new_dic.items())
        for i in range(len(new_dic)):
            if i != len(new_dic) - 1:
                new_sentence += new_dic[i][1]
                new_sentence += " "
            else:
                new_sentence += new_dic[i][1]
        return new_sentence
