import queue

N = int(input())
cards = queue.Queue()

for i in range(1, N + 1):
    cards.put(i)

while cards.qsize() > 1:
    cards.get()

    a = cards.get()
    cards.put(a, 0)

res = cards.get()
print(res)
