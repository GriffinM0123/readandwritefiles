def main():
    infile = open("clients.txt", "r")

    cnt = 1

    for client in infile:
        print(cnt, ". ", client.rstrip("\n"), sep="")
        cnt += 1


main()
