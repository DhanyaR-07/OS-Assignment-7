import random

# ------------------ BEST FIT ------------------
def best_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]

    return allocation


# ------------------ WORST FIT ------------------
def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j

        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= processes[i]

    return allocation


# ------------------ FIFO ------------------
def fifo(pages, capacity):
    s = []
    faults = 0

    for p in pages:
        if p not in s:
            if len(s) < capacity:
                s.append(p)
            else:
                s.pop(0)
                s.append(p)
            faults += 1

    return faults


# ------------------ LRU ------------------
def lru(pages, capacity):
    s = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.append(pages[i])
            else:
                lru_page = min(s, key=lambda x: pages[:i][::-1].index(x))
                s[s.index(lru_page)] = pages[i]
            faults += 1

    return faults


# ------------------ MAIN ------------------
def main():

    print("Memory Management Simulator")

    # Random Data
    blocks = [random.randint(50,200) for _ in range(5)]
    processes = [random.randint(10,100) for _ in range(5)]
    pages = [random.randint(1,10) for _ in range(15)]
    capacity = 3

    f = open("Output/results.txt","w")

    f.write("Blocks: " + str(blocks) + "\n")
    f.write("Processes: " + str(processes) + "\n\n")

    # Best Fit
    bf = best_fit(blocks.copy(), processes)
    f.write("Best Fit Allocation:\n" + str(bf) + "\n\n")

    # Worst Fit
    wf = worst_fit(blocks.copy(), processes)
    f.write("Worst Fit Allocation:\n" + str(wf) + "\n\n")

    # Page Replacement
    f.write("Pages: " + str(pages) + "\n")

    fifo_faults = fifo(pages, capacity)
    lru_faults = lru(pages, capacity)

    f.write("FIFO Page Faults: " + str(fifo_faults) + "\n")
    f.write("LRU Page Faults: " + str(lru_faults) + "\n")

    f.close()

    print("DONE. Check Output/results.txt")


if __name__ == "__main__":
    main()
