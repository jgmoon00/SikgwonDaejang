const jsConfetti = new JSConfetti();

async function pickRestaurant() {
  try {
    const res = await fetch('./data/random_restaurants.json');
    const data = await res.json();
    const random = data[Math.floor(Math.random() * data.length)];

    document.getElementById('result').innerText = `오늘은 ${random.name}!`;

    jsConfetti.addConfetti({
      emojis: ["🍔", "🍕", "🍣", "🥗", "🍜"],
      emojiSize: 70,
      confettiNumber: 40
    });
  } catch (err) {
    console.error("랜덤 식당 로딩 실패", err);
    document.getElementById('result').innerText = '식당을 불러오지 못했습니다.';
  }
}
