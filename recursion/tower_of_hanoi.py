def tower_of_hanoi(n, source, helper, destination):
    # base case
    if n == 1:
        print(f"transferring disk {n} from {source} to {destination}")
        return

    # transferring n-1 disks from source to helper
    tower_of_hanoi(n-1, source, destination, helper)

    # transferring n disk from source to destination
    print(f"transferring disk {n} from {source} to {destination}")

    # transferring n-1 disks from helper to destination
    tower_of_hanoi(n-1, helper, source, destination)

if __name__ == '__main__':
    n = 3 # number of disks
    tower_of_hanoi(n, 'A', 'B', 'C')