<p align="center"><b>Техническое задание</b></p>

<b><p>Python, Django, PostgreSQL, Rest-API, MVC</b></p>

Разработать приложение для бронирования переговорных комнат в офисе компании "Альфа".  
Приложение должно поддерживать две роли сотрудников:  
<li>«Офис менеджер»</li> 
<li>«Сотрудник»</li> 
С помощью приложения сотрудники могут рзервировать переговорную комнату на определенное время, а также получать уведомления о том, что офис менеджер подтвердил или отклонил такую возможность.<br>
Офис менеджер может подтвердить или отклонить бронирование переговорных пользователем, а также отредактировать информацию о переговорной или добавить новую
комнату, или удалить уже имеющуюся.<br>

Для роли «Сотрудник» в приложении доступно несколько экранов:
<ul>
<li>1) Вход в приложение по логину и паролю</li>
<li>2) После входа в приложение видимым становится экран со списком из всех имеющихся переговорных комнат, каждый элемент списка содержит в себе следующую информацию:
  <ul><li>а) Название комнаты</li>
<li>б) Количество кресел</li>
<li>в) Самое ранее забронированное время (если на данный момент такого времени нет то надпись о том что аудитория свободна)</li>
<li>г) Наличие проектора (возможно в виде изображения)</li>
<li>д) Наличие маркерной доски (возможно в виде изображения)</li>
  </li></ul></li>
</ul>

Ниже схематично показан пример:
<p align="center"><img  width=300px  src="https://user-images.githubusercontent.com/71926912/121804986-c980a280-cc51-11eb-8bca-6bd0a6085c7c.png"></p>
<ul>
<li>3) При нажатии на элемент списка открывается экран с описанием комнаты:
<ul><li>а) Информация о комнате: Название комнаты, Количество кресел, Наличие проектора, Наличие маркерной доски, описание комнаты.</li>
<li>б) Список с датами и временем уже зарезервированных по времени мероприятий</li>
<li>в) Кнопка "забронировать"</li></ul>
</li>
</ul>

<p align="center"><img width=300px src="https://user-images.githubusercontent.com/71926912/121805039-0351a900-cc52-11eb-97ea-5ddf7d8a3835.png "></p>
<ul>
<li>4) При нажатии на кнопку "забронировать" открывается экран с выбором даты и времени (начало, конец), и названием мероприятия
<ul>
<li>Технические требования:
<ul><li>Верстка под разные разрешения экранов</li> </ul>
</li></ul></li></ul>
 
Для роли «Офис менеджер» в приложении доступно несколько экранов:
<ul>
  
<li>1. Вход по логину и паролю.
<li>2. На главной форме список из всех переговорных, каждый элемент списка содержит в себе следующую информацию: <ul><li>Название комнаты</li> <li>Количество кресел</li> <li>Наличие проектора</li> <li>Наличие маркерной доски</li></ul></li>
на этой же странице в отдельной области экрана список из заявок которые нужно подтвердить или отклонить, список обновляется каждые 10 сек без перезагрузки страницы, у каждого элемента списка есть кнопка подтвердить или отклонить (нажатие на кнопку подтвердить/отклонить не должно приводить к перезагрузке страницы).</li>
<li>3. Форма редактирования информации о переговорной.</li>
<li>4. Форма управления ролями (роль «Сотрудник» глобальная и по умолчанию в нее входят все пользователи, роль «Офис менеджер» может назначить любой «Офис менеджер»).</li>
</ul>
