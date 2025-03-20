import sys
import csv
from functools import cmp_to_key


def compare(item1, item2):
    i = ""
    while not (i == "1" or i == "2"):
        i = input(
            f"\nWhich item goes earlier in the list? 1 for left; 2 for right. {str(item1)} | {str(item2)}\n")
    if i == "1":
        return -1  # item1 earlier
    else:
        return 1  # item2 earlier


def humansort(items):
    return sorted(items, key=cmp_to_key(compare))


def pprint(l):
    print("\n")
    [print("=> " + str(x)) for x in l]
    print("\n")


def main():
    if len(sys.argv) < 2:
        print("Usage:\n\nhumansort.py <path to csv> <path to output file>")
        return

    try:
        f = open(sys.argv[1], newline='')
    except Exception as e:
        print(e)
        return
    print("Opened: "+sys.argv[1])

    reader = csv.reader(f)
    reader_output = list(reader)
    entries = []
    [entries.extend(x) for x in reader_output]
    f.close()

    sorted_entries = humansort(entries)

    print("\nSorting finished. Sorted list:")
    pprint(sorted_entries)

    output_path = None
    successful = False
    attempts = 0
    while not successful:
        if len(sys.argv) < 3 or attempts > 0:
            output_path = input("Output path: ")
        else:
            output_path = sys.argv[2]

        try:
            f_output = open(output_path, "w")
            writer = csv.writer(f_output)
            successful = True
        except Exception as e:
            print(e)

        attempts += 1

    writer.writerow(sorted_entries)
    print("Sorted list written to "+output_path)


if __name__ == "__main__":
    main()
