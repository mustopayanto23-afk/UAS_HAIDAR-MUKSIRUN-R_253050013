const kata = ["Mancing", "Main Bola", "Belajar Coding", "Desain Digital"];
let urutan = 0;
let huruf = 0;

function ketik() {
  document.getElementById("typing").textContent = kata[urutan].slice(0, huruf);
  huruf++;

  if (huruf > kata[urutan].length) {
    huruf = 0;
    urutan = (urutan + 1) % kata.length;
  }

  setTimeout(ketik, 180);
}

ketik();

function ubahMode() {
  document.body.classList.toggle("dark");
}