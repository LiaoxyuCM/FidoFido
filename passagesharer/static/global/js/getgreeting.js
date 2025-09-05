document.addEventListener("DOMContentLoaded", () => {
    var date = new Date();
    var hour = date.getHours();
    var getgreeting = document.querySelector(".GetGreeting")


    switch (hour) {
        case 2:
        case 3:
        case 4:
        case 5:
            getgreeting.innerHTML = "Good early morning";
            break;
        case 6:
        case 7:
        case 8:
        case 9:
        case 10:
            getgreeting.innerHTML = "Good morning";
            break;
        case 11:
        case 12:
        case 13:
            getgreeting.innerHTML = "Good noon";
            break;
        case 14:
        case 15:
        case 16:
        case 17:
        case 18:
            getgreeting.innerHTML = "Good afternoon";
            break;
        case 19:
        case 20:
            getgreeting.innerHTML = "Good evening";
            break;
        case 21:
        case 22:
            getgreeting.innerHTML = "Good night";
            break;
        case 23:
        case 0:
        case 1:
            getgreeting.innerHTML = "Good latenight";
            break;

    };
});