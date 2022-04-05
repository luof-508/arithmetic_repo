"""
添加和搜索单词
1、添加的单词都是小写字母
2、搜索的单词由小写字母和'.'组成， '.'代表任何小写字母

深度搜索 BFS
"""


class Tree:
    def __init__(self):
        self.words_tree = {}
        self.end_flag = False


class WordDictionary:
    def __init__(self):
        self.tree = Tree()

    def add_word(self, word):
        for s in word:
            if s not in self.tree.words_tree:
                self.tree.words_tree[s] = Tree()
            self.tree = self.tree.words_tree[s]
        self.tree.end_flag = True

    def search_word(self, word):
        """
        1、当前字符为小写字母时，只需根据索引取字母，并在单词树中搜索是否有该字符：
            有则继续往下搜索，当搜索的深度达到单词长度时，停止搜索，返回end_flag标记
            没有则返回false
        2、当前字符为'.'时，需遍历当前层的每一个字母，并进行第一点的搜索逻辑
        """
        # 构造字母和 . 的for循环
        search_dict = self.tree
        print(search_dict.words_tree)
        idx = 0
        return self.bfs_method(search_dict, idx, word)

    def bfs_method(self, child_tree, idx, word):
        if len(word) == idx:
            return child_tree.end_flag

        cur = word[idx] if word[idx].islower() else child_tree.words_tree
        print(cur)

        for s in cur:
            if s in child_tree.words_tree:
                search_dict = child_tree.words_tree[s]
                idx += 1
                return self.bfs_method(search_dict, idx, word)
        else:
            return False


if __name__ == '__main__':
    word_dct = WordDictionary()
    word_dct.add_word('app')
    word_dct.add_word('ap')
    print(word_dct.tree.words_tree)
    print(word_dct.search_word('.p'))
