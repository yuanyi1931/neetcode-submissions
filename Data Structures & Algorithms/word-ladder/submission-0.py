class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        patterns = defaultdict(list)
        for w in words:
            for i in range(len(w)):
                patterns[w[:i] + "*" + w[i + 1:]].append(w)
        
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, steps = q.popleft()
            for i in range(len(word)):
                for nxt in patterns[word[:i] + "*" + word[i + 1:]]:
                    if nxt == endWord:
                        return steps + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return 0
                 

