# Music recognizer

## Використання


Запуск проект:

https://hak-test-litvin-kaverinsky.herokuapp.com/core

Додаток підтримує два способи пошуку музичних композицій:

 1. Потрібно ввести слова пісні, яка вам відома і додаток повинен відшукати та відтворити композицію у плеєрі.
    Наприклад, якщо написати "горы", тоді додаток знайде трек під назвою "Люби меня". Він відобразиться у плеері для відтворення. 

 2. Для пошуку по мелодії натисніть кнопку "Почати запис", тоді за допомогую мікрофона почнеться запис звуку. Запис     повинен продовжуватися не менше 40 секунд, інакше пошук буде не достатньо якісним. Такий тип пошуку краще працює, коли
 на мікрофон записується мелодія якоїсь пісні.
    Щоб закінчити запис натискаємо на кнопку "Зупинити запис". Далі з'являється віджет, де можна відтворити мелоді.

### АPI, які були використані

 - `audd.io` AudD - сервіс, який дозволяе робити пошику по композиціям
 - `developers.deezer.com` Deezer - сервіс, який створює віджети для програвання композицій та було використано його API
