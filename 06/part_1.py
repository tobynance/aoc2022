from pathlib import Path

PACKET_LENGTH = 14


########################################################################
def main():
    data = Path("input.txt").read_text()
    for i in range(len(data)-PACKET_LENGTH):
        window = data[i:i+PACKET_LENGTH]
        print("window:", window)
        if len(set(window)) == PACKET_LENGTH:
            print(i+PACKET_LENGTH)
            break


########################################################################
main()
