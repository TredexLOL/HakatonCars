<script>
    // Функция для отображения всплывающего окна
    function showPopup() {
        document.getElementById('popup').style.display = 'flex'; // Показываем окно
    }

    // Функция для скрытия всплывающего окна
    function closePopup() {
        document.getElementById('popup').style.display = 'none'; // Скрываем окно
    }

    // Показать всплывающее окно через 1 минуту
    setInterval(showPopup, 60000); // 60000 миллисекунд = 1 минута

    // Закрытие окна при клике на кнопку закрытия
    document.getElementById('closePopup').onclick = closePopup;

    // Закрытие окна при клике вне окна
    window.onclick = function(event) {
        if (event.target == document.getElementById('popup')) {
            closePopup();
        }
    }
</script>
