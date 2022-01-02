# Technical Excellence 101
Курс про техническое совершенство для нетехнарей.

Этот курс представлят из себя серию воркшопов, при помощи которых можно объяснить смысл основных инженерных практик даже тем, кто в жизни не написал ни одной строчки кода. Это могут быть владельцы продукта, бизнес эксперты, скрам-мастера и любые другие участники команды, которые хотят лучше понимать что такое техническое совершенство и почему ему так много внимания уделяют разработчики. Код — это текст, поэтому мы будем объяснять материал на примере обыкновенного текста. Для прохождения курса не требуется никаких специальных знаний, кроме владения текстовым редактором.

Во время курса вы почувствуете себя разработчиком, столкнетесь с препятствиями, с которыми сталкивается каждый разработчик и поймете как инженерные практики помогают преодолеть эти препятствия.

## Какие темы изучаются в курсе?
* Основные команды git
* Merge
* Pull request
* Unit testing (модульное тестирование)
* Test-driven development (разработка через тестирование)
* Code review
* Парное программирование
* Continuous Integration (непрерывная интеграция)
* Continuous Delivery (непрерывная поставка)

## Подготовка
1. Установите [Visual Studio Code](https://code.visualstudio.com/download)
2. Установите [git](https://git-scm.com/downloads)
3. Проверьте, что git работает
    * Откройте Terminal в MacOS или Git Bash в Windows
    * Выполните команду `git --version`
    * Если вы увидели вывод `git version 2.23.0`, значит все в порядке, git установлен. Числа могут быть другими.
4. Создайте папку, в которой вы будете работать, например `Projects`  
    Windows:
      ```
      cd %USERPROFILE%
      mkdir Projects
      cd Projects
      ```  
    MacOS:  
      ```
      cd ~
      mkdir Projects
      cd Projects
      ```  
5. Склонируйте репозиторий, выполнив команду   
`git clone https://github.com/bevzuk/technical-excellence-101.git`  
или (если у вас добавлен [SSH сертификат](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account))   
`git clone git@github.com:bevzuk/technical-excellence-101.git`  
или (если у вас установлен [GitHub CLI](https://cli.github.com))  
`gh repo clone bevzuk/technical-excellence-101`
6. Откройте локальный репозиторий в VS Code
    * Запустите VS Code
    * Откройте папку Projects/technical-excellence-101
      * Меню File -> Open Folder ... или 
      * Open ... на главном экране
      * Выберите папку Projects/technical-excellence-101
      * Нажмите Open
        ![](images/Open%20folder.png)
    * В левой панельке Explorer вы должны увидеть структуру проекта
      

## Авторство
Идея курса принадлежит Антону Бевзюку (@bevzuk). В создании курса принимали участие Дарья Баянова, Федор Слесаренко, Арсений Кельдышев, Светлана Кривенко.

