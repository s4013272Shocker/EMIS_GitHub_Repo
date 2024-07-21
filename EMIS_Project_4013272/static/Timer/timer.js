var seconds = document.getElementById("secondsUpdate");
var minutes = document.getElementById("minutesUpdate");
var hours = document.getElementById("hoursUpdate");
var days = document.getElementById("daysUpdate");

var presentDate = new Date().getFullYear();

var examDateTime = new Date(`August 05 ${presentDate} 04:00:00 `);

function LiveCountdown ()
{
    var presentTime = new Date();
    var gapDifference = examDateTime - presentTime

    var day = Math.floor(gapDifference / 1000 / 60 / 60 / 24 );
    var hour = Math.floor(gapDifference / 1000 / 60 / 60 % 24);
    var minute = Math.floor (gapDifference / 1000 / 60 % 60);
    var second  = Math.floor (gapDifference / 1000 % 60 );

    days.innerHTML = day;
    hours.innerHTML = hour;
    minutes.innerHTML = minute;
    seconds.innerHTML = second;

    console.log("Days: " +  day + "\n" + "Hours: " + hour  + "\n" + "Minutes: " + minute + "\n" + "Seconds: " + second);

}

setInterval(LiveCountdown, 1000);

