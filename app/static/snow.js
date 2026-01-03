/* snow.js — генерация реалистичных снежинок */
function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.classList.add("snowflake");

    const span = document.createElement("span");
    span.textContent = "❄";
    snowflake.appendChild(span);

    // Случайная позиция по горизонтали
    snowflake.style.left = Math.random() * 100 + "vw";

    // Случайный размер снежинки
    const size = 10 + Math.random() * 20;
    span.style.fontSize = size + "px";

    // Случайная длительность падения
    const fallDuration = 5 + Math.random() * 7;
    snowflake.style.animationDuration = `
        ${fallDuration}s,
        ${3 + Math.random() * 3}s,
        ${4 + Math.random() * 4}s,
        ${fallDuration}s
    `;

    // Добавляем в контейнер
    document.getElementById("snow-container").appendChild(snowflake);

    // Удаляем после завершения анимации
    setTimeout(() => snowflake.remove(), fallDuration * 1000);
}

// Создаём снежинку каждые 200 мс
setInterval(createSnowflake, 200);
