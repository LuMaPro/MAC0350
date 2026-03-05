document.addEventListener('DOMContentLoaded', () => {
        
    // --- Exercício 1 ---
    // Seu código aqui
    const button1 = document.getElementById('btn-listener')
    button1.addEventListener('click',() => {
        button1.innerText = 'Fui clicado via Listener!'
    })
    
    // --- Exercício 2 ---
    // Seu código aqui
    const button2 = document.getElementById('btn-add')
    button2.addEventListener('click',() => {
        let input_value = document.getElementById('input-item').value
        const ul = document.getElementById('lista-itens')
        const li = document.createElement('li')
        li.innerText = input_value
        ul.appendChild(li)
    })
    
    
    // --- Exercício 3 ---
    // Dica: Crie a variável do tempo aqui fora, e o setInterval dentro do listener do botão
    // Seu código aqui
    const button3 = document.getElementById('btn-iniciar')
    const cron = document.getElementById('visor-cronometro')
    let timer = parseInt(cron.innerText)
    button3.addEventListener('click',() => {
        setInterval(() => {
            timer++
            cron.innerText = timer
        }, 1000)
    })
    
    
    // --- Exercício 4 ---
    // Seu código aqui (Lembre-se de checar o localStorage logo que a página carregar!)
    const time_local = localStorage.getItem('time')
    if(time_local != null){
        const span = document.getElementById('time-selecionado')
        span.innerText = time_local
    }
    const selector = document.getElementById('select-time')
    selector.addEventListener('change',() => {
        let time = selector.value
        const span = document.getElementById('time-selecionado')
        span.innerText = time
        localStorage.setItem('time',time)
    })
    
});
