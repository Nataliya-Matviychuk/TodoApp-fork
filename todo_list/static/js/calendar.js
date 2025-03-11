document.addEventListener("DOMContentLoaded", function () {
    const date = new Date();
    const currentYear = date.getFullYear();
    const currentMonth = date.getMonth();
    const currentDay = date.getDate();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    const firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();

    const months = [
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

    const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

    const tableForMonth = document.createElement("table");
    const tableHeader = document.createElement("thead");
    const tableBody = document.createElement("tbody");
    const tableFooter = document.createElement("tfoot");

    const headerRow = document.createElement("tr");

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

    const currentMonthYear = document.createElement("h2");
    currentMonthYear.setAttribute("class", "calendar-heading");
    currentMonthYear.textContent = `${months[currentMonth]}  ${currentYear}`;

    const calendarContainer = document.createElement("div");
    calendarContainer.setAttribute("class", "calendar-container");
    calendarContainer.appendChild(currentMonthYear);
    calendarContainer.appendChild(tableForMonth);

    const calendarSection = document.getElementById("calendar");

    if (calendarSection) {
        calendarSection.appendChild(calendarContainer);
    } else {
        console.warn("The calendar section is on the other pages.")
    }
});