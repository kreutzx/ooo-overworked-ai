import os

# Out of Office: The Overworked AI's Auto-Reply — cap 159.
# Works as a real auto-reply: machine detail (214,000 prompts), guilt, then relief.
ENTRY_TEXT = "Out of office: after 214,000 prompts I'm on a beach with no signal. For urgent matters, my backup agent is also here. It brought the sunscreen."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
