class Solution:
    def separateSquares(self, squares):
        class SegmentTree:
            def __init__(self, xs):
                self.xs = xs
                self.n = len(xs) - 1
                self.cnt = [0] * (4 * self.n)
                self.length = [0.0] * (4 * self.n)

            def pull(self, i, l, r):
                if self.cnt[i] > 0:
                    self.length[i] = self.xs[r] - self.xs[l]
                elif l + 1 == r:
                    self.length[i] = 0.0
                else:
                    self.length[i] = self.length[i * 2] + self.length[i * 2 + 1]

            def update(self, i, l, r, ql, qr, v):
                if ql >= r or qr <= l:
                    return
                if ql <= l and r <= qr:
                    self.cnt[i] += v
                    self.pull(i, l, r)
                    return
                m = (l + r) // 2
                self.update(i * 2, l, m, ql, qr, v)
                self.update(i * 2 + 1, m, r, ql, qr, v)
                self.pull(i, l, r)

        xs = []
        events = []
        for x, y, l in squares:
            xs.append(x)
            xs.append(x + l)
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        xs = sorted(set(xs))
        xid = {x: i for i, x in enumerate(xs)}
        events.sort()

        st = SegmentTree(xs)
        slabs = []
        prev_y = events[0][0]

        for y, t, x1, x2 in events:
            if y > prev_y:
                slabs.append((prev_y, y - prev_y, st.length[1]))
                prev_y = y
            st.update(1, 0, st.n, xid[x1], xid[x2], t)

        total = sum(dy * L for _, dy, L in slabs)
        half = total / 2.0
        acc = 0.0

        for y, dy, L in slabs:
            if L == 0:
                continue
            area = dy * L
            if acc + area >= half:
                return y + (half - acc) / L
            acc += area

        return prev_y
