import os

TEXT = "My washing machine plays a little victory song when it finishes, like clean socks are a moon landing."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
