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

---
<!-- _class: invert -->
# 1/2. Автор: Запушить код в свою ветку
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
# 2/2. Автор: Создать Pull Request

![](Images/Create%20pull%20request.png)

---
<!-- _class: invert -->
# 2/2. Автор: Создать Pull Request

![](Images/Create%20pull%20request%202.png)

---
<!-- _class: invert -->
# 2/2. Автор: Создать Pull Request

![](Images/Create%20pull%20request%203.png)

---
# Правила Code Review

---
# Плохо
* Оценочное суждение
* Критика в адрес автора
* Безапелляционное утверждение
* Не информативный комментарий
![bg height:500px right:50%](Images/Code%20review%201.png)

---
# Хорошо
* Лаконично
* По существу
* Дружелюбно
* Со ссылками на источники
![bg height:500px right:50%](Images/Code%20review%202.png)

---
# Хвалите
* "Отличная работа!"
* "Красавчик!"
* "Круто придумано, я бы не догадался"

---
<!-- _class: invert -->
# Упражнение. Исправить замечания и вмержить PR в master
1. Ревьювер: проверить PR и написать коментарии
1. Автор: исправить замечания
1. Ревьювер: заапрувить PR
1. Автор: Смержить Pull Request в master


---
<!-- _class: invert -->
# 1/4. Ревьювер: Откройте PR
![height:500px](Images/Review%20pull%20request%201.png)

---
<!-- _class: invert -->
# 1/4. Ревьювер: Оставьте комментарии
![height:500px](Images/Comment%20pull%20request.png)

---
<!-- _class: invert -->
# 2/4. Автор: Исправьте замечания
* Прочитайте замечания в вашем Pull Request
* Исправьте замечания в VS Code
* Закомитьте и запушьте исправления
  * Ваши исправления автоматически добавятся в Pull Request

--- 
<!-- _class: invert -->
# 3/4. Ревьювер: Заапрувьте Pull Request
* Проверьте исправление замечаний
* Если вас все устраивает, выберите Approve (одобрить)
* Если остались замечания — опишите и выберите Request Changes (запросить изменения)

![bg height:500px right:50%](Images/Approve%20pull%20request.png)

---
<!-- _class: invert -->
# 4/4. Автор: Смержьте Pull Request в master
* Merge pull request
* Delete branch
![height:500px](Images/Merge%20pull%20request.png)

---
# Дебриф
* Какую пользу вы видите от Code Review?
* Чем мы за это платим?