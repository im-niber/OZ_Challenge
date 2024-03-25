const attackDamage = parseInt(prompt("1회 공격시 데미지는?(자연수)"))
let attackCount = 0

if(attackDamage > 0){
    const container = document.getElementById("container")
    const h1 = document.createElement("h1")
    h1.textContent = "몬스터 잡기 게임을 시작합니다 ! "
    container.appendChild(h1)

    let hp = 100

    while(hp > 0){
        hp -= attackDamage
        attackCount += 1

        const p = document.createElement("p")
        p.textContent = `몬스터를 ${attackCount}회 공격했다`
        container.append(p)

        if(hp < 0){ hp = 0 }
        
        const strong = document.createElement("strong")
        strong.textContent = `몬스터의 남은 hp는 ${hp}입니다`
        container.append(strong)
    }

    const h2 = document.createElement("h2")
    h2.textContent = "몬스터 잡기 완료 ~"
    h2.style.color = "orange"
    h2.title = "새로고침하면 다시 게임 가능" 
    container.appendChild(h2)

} else{
    alert("데미지를 잘못 입력하여 게임을 취소합니다")
}