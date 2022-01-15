---
marp: true
paginate: true
footer: 'Technical Excellence 101 / Unit 3. Code Review и Парная работа'

---
# Unit 3. Code Review и Парная работа
## Схема занятия
1. Упражнение. Диктант
1. Pull Request
1. Упражнение на Pull Request
1. Code Review + правила
1. Упражнение на Code Review
1. Парная работа
1. Упражнение на Парную работу
1. Дебриф

---
<!-- _class: invert -->
# Упражнение. Диктант
1. Возьмите последнюю версию (pull)
2. Откройте файл Unit 3/dictation.md
3. Напишите диктант
Тренер будет читать быстро, вы не будете успевать. Это нормально. Это сделано специально, чтобы вы совершали ошибки.
4. Сохраните изменения (add, commit, push)

Время: 15 минут.

---
# Ошибка
Вы должны были получить ошибку:
```
remote: error: GH006: Protected branch update failed for refs/heads/master.
remote: error: At least 1 approving review is required by reviewers with write access.
```

Это означает, что больше напрямую пушить код в master нельзя. Нужно создавать Merge Request и проходить Code Review.

---
# Упражнение. Вмержить изменения в master через Pull Request
1. Запушить код в свою ветку
2. Создать Pull Request
3. Получить approve (одобрение) от нужного числа ревьюверов
4. Смержить Pull Request в master

---
<!-- _class: invert -->
# 1/4. Запушить код в свою ветку
1. Создаём ветку
   * *git branch <имя ветки>*
   * *git checkout <имя ветки>*
или одной командой
   * *git checkout -b <имя ветки>*
2. Комитим изменения в локальный репозиторий
   * *git add .*
   * *git commit -m "комментарий"*
3. Пушим изменения из локального репозитория в удаленный
   * *git push*

---
<!-- _class: invert -->
# 2/4. Создать Pull Request

![](Images/Create%20pull%20request.png)

---
<!-- _class: invert -->
# 2/4. Создать Pull Request

![](Images/Create%20pull%20request%202.png)

---
<!-- _class: invert -->
# 2/4. Создать Pull Request

![](Images/Create%20pull%20request%203.png)

---
<!-- _class: invert -->
# 3. Получить approve (одобрение)
![height:500px](Images/Review%20pull%20request%201.png)

---
<!-- _class: invert -->
# 3. Оставьте комментарии
![height:500px](Images/Comment%20pull%20request.png)

