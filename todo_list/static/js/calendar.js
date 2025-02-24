document.addEventListener("DOMContentLoaded", function () {
    let date = new Date();
    let currentYear = date.getFullYear();
    let currentMonth = date.getMonth();
    let currentDay = date.getDate();
    let daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    let firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();

    let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    let daysOfWeek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];

    let tableForMonth = document.createElement('table');
    let header = document.createElement('tr');

    for (let i = 0; i < 7; i++) {
        let cell = document.createElement('th');
        cell.textContent = daysOfWeek[i];
        header.appendChild(cell);
    }

    tableForMonth.appendChild(header);

    for (let i = 1; i <= 42; i++) {

        if (i % 7 === 1) {
            var row = document.createElement('tr');
            tableForMonth.appendChild(row);
        }

        let cell = document.createElement('td');

        if (i >= firstDayOfMonth && i < daysInMonth + firstDayOfMonth) {
            cell.textContent = i - firstDayOfMonth + 1;
            if (cell.textContent == currentDay) {
                cell.style.backgroundColor = "#ee394c";
                cell.style.color = '#ffffff';
            }
        } else {
            let prevMonthDays = new Date(currentYear, currentMonth, 0).getDate();
            if (i < firstDayOfMonth) {
                cell.textContent = prevMonthDays - (firstDayOfMonth - i - 1);
                cell.style.backgroundColor = 'rgba(187, 233, 219, 0.5)';
            } else {
                cell.textContent = i - daysInMonth - firstDayOfMonth + 1;
                cell.style.backgroundColor = 'rgba(187, 233, 219, 0.5)';
            }
        }

        row.appendChild(cell);
    }

    let currentMonthYear = document.createElement('h1');
    currentMonthYear.setAttribute('class', 'calendar-heading');
    currentMonthYear.textContent = `${months[currentMonth]}  ${currentYear}`;

    let calendarContainer = document.createElement('div');
    calendarContainer.setAttribute('class', 'calendar-container');
    calendarContainer.appendChild(currentMonthYear);
    calendarContainer.appendChild(tableForMonth);

    let calendarElement = document.getElementById('calendar');
    calendarElement.appendChild(calendarContainer);
});