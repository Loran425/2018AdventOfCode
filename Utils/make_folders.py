import os
import git

existing_days = list(os.walk(".."))[0][1]
day_num = 0
for day in existing_days:
    if "_" in day:
        day_num = max(day_num, int(day.split("_")[1]))
day_num += 1
folder = f"../Day_{day_num}"
input_txt = f"{folder}/input.txt"
main_py = f"{folder}/main.py"
os.mkdir(folder)

with open(input_txt, mode="w") as f:
    f.write("")

with open(main_py, mode="w") as f:
    f.write(
        """def main():
    pass


if __name__ == '__main__':
    main()
"""
    )

repo = git.repo.Repo(os.path.abspath(".."))
repo.index.add([os.path.abspath(x) for x in [input_txt, main_py]])
repo.index.commit(message=f"Automated File Generation for day {day_num} of AOC")
