# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: [Сычёв Даниил Владиславович]

def get_system_info():

    system_info = {
        "student_name": "Сычёв Даниил Владиславович",
        "academic_group": "ИВТИИбд-14",
        "github_link": "https://github.com/DEMKA404"
    }
    return system_info

if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
git commit -m "start project-1"
