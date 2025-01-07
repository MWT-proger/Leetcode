import matplotlib.pyplot as plt

def update_progress_chart():
    tasks = ["Easy", "Medium", "Hard"]
    progress = [10, 5, 2]  # Количество решённых задач

    plt.bar(tasks, progress, color=['green', 'orange', 'red'])
    plt.xlabel("Сложность")
    plt.ylabel("Решено")
    plt.title("Прогресс решений")
    plt.savefig("progress.svg")

if __name__ == "__main__":
    update_progress_chart()
