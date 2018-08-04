def get_dtype_from_input(dtype=int):
    return map(dtype, input().rstrip().split())


class Score(object):

    def get_emotion_name(index):
        return 'like' if index == 0 else 'hate'

    def __init__(self, arr, like, hate):
        self._arr = sorted(arr)
        self._emotion = [sorted(like), sorted(hate)]
        self._lengths = [len(a) for a in self._emotion]
        self._index = [0, 0]
        self._hits = [0, 0]
        self._overflow = [False, False]
        self.build_score()
        
    def build_score(self):
        for el in self._arr:
            self.sorted_compare(el)

    def sorted_compare(self, el):
        self.sorted_compare_by_emotion_index(el, 0)
        self.sorted_compare_by_emotion_index(el, 1)

    def sorted_compare_by_emotion_index(self, el, index):
        while el > self._emotion[index][self._index[index]] and not self._overflow[index]:
            if self._index[index] + 1 >= self._lengths[index]:
                self._overflow[index] = True
            else:
                self._index[index] += 1
        if el == self._emotion[index][self._index[index]]:
            self._hits[index] += 1

    def get_score(self):
        return self._hits[0]-self._hits[1]


if __name__ == '__main__':
    n, m = get_dtype_from_input()
    arr = get_dtype_from_input()
    like = get_dtype_from_input()
    hate = get_dtype_from_input()
    score = Score(arr, like, hate)
    print(score.get_score())
