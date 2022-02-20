---
marp: true
paginate: true
footer: 'Technical Excellence 101 / Unit 5. CI/CD'

---
# Unit 5. CI/CD
## Схема занятия
1. Continuous Integration
2. CI Theatre
3. Dos / Dont's
4. Упражнение. Совместное редактирование сказки
5. Continuous Delivery
6. Continuous Deployment
7. Пример CD пайплайна
8. DORA метрики
9. DevOps
10. Дебриф

---
![bg height:100%](Images/Work%20without%20CI.jpg)

---
![bg width:100%](Images/Seldom%20integration.png)

---
# Тест. Есть ли CI в вашей команде?
1. **Каждый разработчик** команды **ежедневно** интегрирует **весь** код в master (1 балл)
2. После каждого изменения master запускается **автоматическая сборка** и тесты (1 балл)
3. Если билд падает, команда его чинит за **10 минут** (1 балл)

Если вы набрали 3 балла — поздравляем, у вас CI.

---
# Определение CI (Кент Бек)
![width:100%](Images/CI%20-%20Kent%20Keck.png)
Kent Beck, Extreme Programming Explained

---
# Определение CI (Мартин Фаулер)
![width:700px](Images/CI%20-%20Martin%20Fowler.png)
[Martin Fowler - Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)

---
# Определение CI (LeSS)
![width:600px](Images/CI%20-%20LeSS.png)
[less.works - Continuous Integration](https://less.works/less/technical-excellence/continuous-integration.html)

---
![bg height:100%](Images/Work%20with%20CI.jpg)


---
# Описание ситуации
* Мы совместно пишем сказку про колобка в markdown
* Сказку будем публиковать на сайте, поэтому нужно преобразовать markdown -> HTML
  * Для этого будем использовать утилиту *markdown2*:
    ```markdown2 Kolobok.md >> ./build/Kolobok.html```
* Тесты проверяют корректность HTML файла 
  * Содержание
  * Форматирование

---
# Демо
 Что нужно сделать, чтобы проверить, что все работает правильно?
 1. ```rm -rf ./build``` удалить папку build со всем содержимым
 2. ```mkdir -p ./build``` пересоздать папку build
 3. ```markdown2 Kolobok.md > ./build/Kolobok.html``` сгенерировать HTML
 4. ```cat ./build/Kolobok.html``` вывести на экран содержимое HTML файла
 5. ```pytest``` запустить тесты

и нигде не ошибиться!

---
# CI билд
Помогает автоматизировать рутинные проверки
![bg right:55% height:100%](Images/CI%20build.png)


---
# Упражнение. Найти ошибку в HTML, написать тест и исправить
1. Возьмите последнюю версию ветки master
   ```git checkout master```
   ```git pull```
2. Создайте свою ветку
   ```git checkout -b feature/group1```
3. Откройте файл *Unit 5. CICD/Kolobok.md*
4. Найдите ошибку в файле
5. Добавьте тест для проверки ошибки в HTML файле, например
   ```python
   def test_has_subheader_wolf(html):
    assert '<h3>3.2 Волк</h3>' in html
   ```
6. Закомитьте и запушьте ваш код
   ```git add .```
   ```git commit -m "Добавил тест на подзаголовок с волком"```
   ```git push```
   

---
![bg height:90%](Images/CI%20theatre.png)

---
![bg height:90%](Images/CI%20Do.png)

---
![bg height:90%](Images/CI%20Dont.png)