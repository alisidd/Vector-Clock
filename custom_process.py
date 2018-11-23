def compare_vectors(v1, v2):
    gt_diff, lt_diff = 0, 0
    for (value1, value2) in zip(v1, v2):
        gt_diff |= value1 > value2
        lt_diff |= value1 < value2
        if gt_diff and lt_diff:
            break
    return int(gt_diff) - int(lt_diff)

class CustomProcess(object):
    def __init__(self, idx, len):
        self.idx = idx
        self.vector = [0] * len

    def finished_event(self):
        self.vector[self.idx] += 1
        print('{} finished event at {}'.format(self.idx, self.vector))

    def send_message(self, pipe):
        self.vector[self.idx] += 1
        pipe.send(self.vector)

        print('{} sent a message at {}'.format(self.idx, self.vector))

    def receive_message(self, pipe):
        vector = pipe.recv()
        self._merge_vectors(vector)

        self.vector[self.idx] += 1
        print('{} received a message at {}'.format(self.idx, self.vector))

    def _merge_vectors(self, received_vector):
        for (i, v) in enumerate(received_vector):
            self.vector[i] = max(self.vector[i], v)

    def is_before(self, process):
        return compare_vectors(self.vector, process.vector) == -1

    def is_after(self, process):
        return compare_vectors(self.vector, process.vector) == 1

    def is_concurrent(self, process):
        return compare_vectors(self.vector, process.vector) == 0
