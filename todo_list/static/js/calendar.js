document.addEventListener("DOMContentLoaded", function () {
    let date = new Date();
    let currentYear = date.getFullYear();
    let currentMonth = date.getMonth();
    let currentDay = date.getDate();
    let daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    let firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();

    let months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    let daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

    let tableForMonth = document.createElement("table");
    let tableHeader = document.createElement("thead");
    let tableBody = document.createElement("tbody");
    let tableFooter = document.createElement("tfoot");

    let headerRow = document.createElement("tr");

    // Create the header row of the calendar
    for (let i = 0; i < 7; i++) {
        let headerCell = document.createElement("th");
        headerCell.textContent = daysOfWeek[i];
        headerRow.appendChild(headerCell);
    }

    tableHeader.appendChild(headerRow);
    tableForMonth.appendChild(tableHeader);

    // Create the body of the calendar
    for (let i = 1; i <= 42; i++) {
        if (i % 7 === 1) {
            var bodyRow = document.createElement("tr");
            tableBody.appendChild(bodyRow);
            tableForMonth.appendChild(tableBody);
        }

        let bodyCell = document.createElement("td");

        if (i >= firstDayOfMonth && i < daysInMonth + firstDayOfMonth) {
            bodyCell.textContent = i - firstDayOfMonth + 1;
            if (bodyCell.textContent == currentDay) {
                bodyCell.style.backgroundColor = "#ee394c";
                bodyCell.style.color = "#ffffff";
            }
        } else {
            // Calculate the number of days in the previous month
            let prevMonthDays = new Date(currentYear, currentMonth, 0).getDate();

            if (i < firstDayOfMonth) {
                bodyCell.textContent = prevMonthDays - (firstDayOfMonth - i - 1);
                bodyCell.style.backgroundColor = "rgba(187, 233, 219, 0.5)";
            } else {
                bodyCell.textContent = i - daysInMonth - firstDayOfMonth + 1;
                bodyCell.style.backgroundColor = "rgba(187, 233, 219, 0.5)";
            }
        }

        bodyRow.appendChild(bodyCell);
    }

    tableForMonth.appendChild(tableFooter);

    let currentMonthYear = document.createElement("h1");
    currentMonthYear.setAttribute("class", "calendar-heading");
    currentMonthYear.textContent = `${months[currentMonth]}  ${currentYear}`;

    let calendarContainer = document.createElement("div");
    calendarContainer.setAttribute("class", "calendar-container");
    calendarContainer.appendChild(currentMonthYear);
    calendarContainer.appendChild(tableForMonth);

    let calendarSection = document.getElementById("calendar");

    if (calendarSection) {
        calendarSection.appendChild(calendarContainer);
    }
});