async function pickRestaurant() {
  const res = await fetch('./random_restaurants.json');
  const data = await res.json();
  const random = data[Math.floor(Math.random() * data.length)];
  document.getElementById('result').innerText = `오늘은 "${random.name}"!`;
}
