let IsOpen = true
let header = document.getElementById('hamburguer')
let icone = document.getElementById('icone')

function menuAction(){
    console.log(IsOpen)
    if(IsOpen){
        console.log(icone)
        IsOpen = false
        header.style.animation = 'down 0.3s ease forwards'
        icone.classList.remove("bi-list")
        icone.classList.add("bi-x")
    }else{
        IsOpen = true
        header.style.animation = 'up 0.3s ease forwards'
        icone.classList.remove("bi-x")
        icone.classList.add("bi-list")
    }
}