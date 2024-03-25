let yourname = prompt("이름을 입력해주세요")
const h1 = document.querySelector("h1")
h1.textContent = yourname

document.querySelector("p")
.textContent = `좋아하는 음식은 ${prompt("좋아하는 음식은 ?")} 입니다`

const p2 = document.querySelector(".fruit")
p2.textContent = "좋아하는 과일은 " + prompt("좋아하는 과일은 ?") + " 입니다"