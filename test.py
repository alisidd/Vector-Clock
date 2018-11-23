from custom_process import CustomProcess
from multiprocessing import Process, Pipe

def unit_test_before_after():
    p0, p1, p2 = CustomProcess(0, 3), CustomProcess(1, 3), CustomProcess(2, 3)

    p0.vector = [1,2,3]
    p1.vector = [2,2,3]
    p2.vector = [2,3,3]

    assert(p0.is_before(p1))
    assert(p0.is_before(p2))
    assert(p1.is_before(p2))

    assert(p2.is_after(p1))
    assert(p2.is_after(p0))
    assert(p1.is_after(p0))

    print('Unit tests for before and after checks passed!')

def unit_test_concurrent():
    p0, p1, p2 = CustomProcess(0, 3), CustomProcess(1, 3), CustomProcess(2, 3)

    p0.vector = [1,2,3]
    p1.vector = [0,3,3]
    p2.vector = [1,3,2]

    assert(p0.is_concurrent(p1))
    assert(p0.is_concurrent(p2))
    assert(p1.is_concurrent(p2))

    print('Unit tests for concurrency checks passed!\n')

def test_events():
    def run_process_0(process, pipe01):
        process.finished_event()
        process.send_message(pipe01)
        process.finished_event()
        process.receive_message(pipe01)
        process.receive_message(pipe02)

        assert(process.vector == [5, 3, 2])
        print('\nAll tests passed!')

    def run_process_1(process, pipe10, pipe12):
        process.receive_message(pipe10)
        process.send_message(pipe10)
        process.send_message(pipe12)

    def run_process_2(process, pipe20, pipe21):
        process.receive_message(pipe21)
        process.send_message(pipe20)

    p0, p1, p2 = CustomProcess(0, 3), CustomProcess(1, 3), CustomProcess(2, 3)
    pipe01, pipe10 = Pipe()
    pipe02, pipe20 = Pipe()
    pipe12, pipe21 = Pipe()

    process0 = Process(target=run_process_0, args=(p0, pipe01))
    process1 = Process(target=run_process_1, args=(p1, pipe10, pipe12))
    process2 = Process(target=run_process_2, args=(p2, pipe20, pipe21))

    process0.start()
    process1.start()
    process2.start()

    process0.join()
    process1.join()
    process2.join()


if __name__ == '__main__':
  unit_test_before_after()
  unit_test_concurrent()

  test_events()
