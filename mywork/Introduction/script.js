function updateDateTime() {
  const now = new Date().toLocaleString("en-EN", {
    timeZone: "Europe/Warsaw",
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  });

  document.getElementById("datetime").textContent =
    "Current data and time in Poland: " + now;
}

// pierwsze uruchomienie
updateDateTime();

// aktualizacja co sekundę
setInterval(updateDateTime, 1000);
