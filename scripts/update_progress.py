import os
import matplotlib.pyplot as plt

BASE_DIR = "problems"
PROGRESS_IMAGE = "progress.svg"
PROGRESS_FILE = "progress.md"

DIFFICULTY = {
    "easy": "🟢 Лёгкая",
    "medium": "🟠 Средняя",
    "hard": "🔴 Сложная",
}

COLORS = {"easy": "green", "medium": "orange", "hard": "red"}


def scan_solved_tasks():
    """Сканирует решённые задачи и общее количество задач."""
    solved_counts = {level: 0 for level in DIFFICULTY}
    total_counts = {level: 0 for level in DIFFICULTY}

    for difficulty in DIFFICULTY:
        difficulty_path = os.path.join(BASE_DIR, difficulty)
        if os.path.exists(difficulty_path):
            for problem in os.listdir(difficulty_path):
                problem_path = os.path.join(difficulty_path, problem)
                if os.path.isdir(problem_path) and os.path.exists(
                    os.path.join(problem_path, "README.md")
                ):
                    total_counts[difficulty] += 1
                    if os.path.exists(os.path.join(problem_path, "solution.py")):
                        solved_counts[difficulty] += 1

    return solved_counts, total_counts


def generate_progress_svg():
    """Создаёт SVG-график с правильным распределением прогресса."""
    solved_counts, total_counts = scan_solved_tasks()

    total_solved = sum(solved_counts.values())
    total_problems = sum(total_counts.values())

    # Рассчитываем общий процент прогресса
    total_progress = (total_solved / total_problems) * 100 if total_problems > 0 else 0

    # Рассчитываем взвешенные проценты по уровням
    weighted_progress = {
        level: (
            (
                (solved_counts[level] / total_counts[level])
                * 100
                * (total_counts[level] / total_problems)
            )
            if total_counts[level] > 0
            else 0
        )
        for level in DIFFICULTY
    }

    # Создаём график
    plt.figure(figsize=(8, 2))
    plt.barh(
        list(DIFFICULTY.keys()),
        [weighted_progress[level] for level in DIFFICULTY],
        color=[COLORS[level] for level in DIFFICULTY],
    )

    plt.xlim(0, 100)
    plt.xlabel("Прогресс (%)")
    plt.title(f"Общий прогресс: {total_progress:.2f}%")
    plt.savefig(PROGRESS_IMAGE, format="svg")

    print("✅ График progress.svg обновлён!")


def generate_progress_md():
    """Создаёт файл progress.md с подробной статистикой по решённым задачам."""
    solved_counts, total_counts = scan_solved_tasks()

    total_solved = sum(solved_counts.values())
    total_problems = sum(total_counts.values())

    # Рассчитываем общий процент прогресса
    total_progress = (total_solved / total_problems) * 100 if total_problems > 0 else 0

    # Рассчитываем прогресс по уровням
    progress_per_difficulty = {
        level: (
            (solved_counts[level] / total_counts[level]) * 100
            if total_counts[level] > 0
            else 0
        )
        for level in DIFFICULTY
    }

    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        f.write("# 📊 Прогресс решений\n\n")
        f.write(
            f"**Прогресс решений: {total_solved}/{total_problems} ({total_progress:.2f}%)**\n\n"
        )
        f.write("![LeetCode Progress](progress.svg)\n\n")

        # Таблица с прогрессом по уровням сложности
        f.write("| Уровень  | Всего задач | Решено | Прогресс |\n")
        f.write("|---------|------------|--------|----------|\n")
        for level in DIFFICULTY:
            f.write(
                f"| {DIFFICULTY[level]} | {total_counts[level]} | {solved_counts[level]} | {progress_per_difficulty[level]:.2f}% |\n"
            )

        f.write("\n## 📌 Решённые задачи\n")
        f.write("| #  | Задача       | Уровень | Решено |\n")
        f.write("|----|-------------|---------|--------|\n")

        task_index = 1
        for level in DIFFICULTY:
            difficulty_path = os.path.join(BASE_DIR, level)
            if os.path.exists(difficulty_path):
                for problem in sorted(
                    os.listdir(difficulty_path)
                ):  # Сортируем задачи по алфавиту
                    problem_path = os.path.join(difficulty_path, problem)
                    if os.path.isdir(problem_path) and os.path.exists(
                        os.path.join(problem_path, "solution.py")
                    ):
                        problem_title = problem.replace("-", " ").title()
                        problem_link = f"problems/{level}/{problem}/README.md"
                        f.write(
                            f"| {task_index} | [{problem_title}]({problem_link}) | {DIFFICULTY[level]} | ✅ |\n"
                        )
                        task_index += 1

    print("✅ Файл progress.md обновлён!")


if __name__ == "__main__":
    generate_progress_svg()
    generate_progress_md()
