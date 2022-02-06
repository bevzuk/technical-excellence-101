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

---
# Парная работа как альтернатива Code Review

---
![bg ](Images/Driver%20and%20navigator.png)

---
# Правила парной работы
1. Уважать друг друга
2. Меняться
    - по таймеру
    - пинг-понг
    - strong style
3. Отдыхать
4. Перемешивать пары каждый день

---
# Преимущества парной работы
1. Все преимущества Code Review, но без задержек
2. Качественная обратная связь
3. Сфокусированная работа
4. Качественный результат
5. Обмен знаниями
6. Соблюдение договоренностей
7. Формирование команды

---
<!-- _class: invert -->
# Упражнение. Написать сказку в паре
## Правила
* Меняйте роли каждые 2-3 минуты
* Навигатор следит за временем
* Драйвер пишет текст
* Навигатор говорит о чем писать
* Навигатор следит за соблюдением правил русского языка
* Навигатор следит за выполнением критериев приёмки
* Навигатор ведёт To Do List

---
<!-- _class: invert -->
# Упражнение. Написать сказку в паре (15 минут)
## Критерии приемки
* Минимум 3 разных персонажа с именами
* Действие происходит в огороде на даче
* Сказка имеет отношение к сбору урожая
* Минимум двое из персонажей — животные
* Есть 5 глав
* Неожиданный финал
* Каждый из персонажей представлен в отдельном абзаце
* Текст разбит на предложения, есть точки, заглавные буквы
* Правила русского языка соблюдены

---
# Дебриф
* Какие преимущества парной работы вы испытали?
* С какими сложностями вы столкнулись во время парной работы?
* Какие возможности для парной работы вы видите в своей команде?

---
# Домашнее задание

1. Дайте обратную связь людям, которые создали Pull Request
2. Получите обратную связь, исправьте замечания и поблагодарите участников
3. Спросите у вашей команды:
* Как часто master билд красный?
* Насколько большие пулл реквесты (# строк кода)?
* Как долго висят pull requests?
* Как команда относится к парному программированию?

Посчитайте статистику и покажите команде

---
# Материалы
* [Как заставить ревьювера вашего кода буквально влюбиться в вас - перевод статьи Майкла Линча](https://technical-excellence.ru/wiki/CodeReviewLoveForAuthors.html)
* [Парное программирование: Сергей Баранов](http://agilemindset.ru/парное-программирование/)
* [On Pair Programming - Birgitta Böckeler](https://martinfowler.com/articles/on-pair-programming.html)
* [Llewellyn's strong-style pairing: Llewellyn Falco](https://llewellynfalco.blogspot.com/2014/06/llewellyns-strong-style-pairing.html).
* [Mob programming and strong-style pairing: Emily Bache](http://coding-is-like-cooking.info/2016/09/mob-programming-strong-style-pairing/).
* [Pair programming: Marek Kusmin](http://www.kusmin.eu/wiki/index.php/Pair_Programming).
* [Pairing techniques: Roger Almeida](http://roger-almeida.blogspot.co.uk/2010/04/pairing-techniques.html).
* [The Pomodoro Technique: Francesco Cirillo](http://baomee.info/pdf/technique/1.pdf).
* [Rethinking pair programming: Sandro Manusco](http://codurance.com/2015/03/15/rethinking-pair-programming/).
* [Teddy bear pair programming: Adrian Bolboacă](http://blog.adrianbolboaca.ro/2012/12/teddy-bear-pair-programming/).
* [What is pair programming?: Adrian Bolboacă](http://blog.adrianbolboaca.ro/2013/09/what-is-pair-programming/).