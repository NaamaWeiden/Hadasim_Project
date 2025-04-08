from collections import Counter


def top_N_errors(file_path: str, N: int, num_parts: int = 100000):

    total_counter = Counter()
    lines = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if "Error:" in line:
                try:
                    error_code = line.split("Error:")[1].strip().strip('"')
                    lines.append(error_code)
                except IndexError:
                    continue

            if i % num_parts == 0:
                total_counter.update(Counter(lines))
                lines = []

        # בדיקת השורות בסוף שלא נכללו ב10000
        if lines:
            total_counter.update(Counter(lines))

    return total_counter.most_common(N)


if __name__ == "__main__":
    file_path = "logs.txt"
    N = int(input("בדיקת N קודי השגיאה השכיחים: "))

    result = top_N_errors(file_path, N)

    print(f"\n {N} השגיאות השכיחות ביותר: ")
    for error, count in result:
        print(f"{error}: {count}")


# זמן: O(N) – עיבוד שורה אחת כל פעם.
#
# מקום: O(m + num_parts) – רק מילון של קודי השגיאה השונים +  100,000 שורות בזיכרון בכל רגע.