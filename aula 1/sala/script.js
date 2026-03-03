    // Exercício 1
    function dispararAlerta() {
        // Seu código aqui
        alert('Bem-vindo(a)!')
    }

    // Exercício 2
    function contarPares() {
        // Seu código aqui
        for(let i = 1; i < 11; i++){
            if (i % 2 === 0){
                console.log(i)
            }
        }
    }

    // Exercício 3
    function mudarTexto() {
        // Seu código aqui
        let item = document.getElementById('texto-alvo')
        item.innerText = 'JavaScript Dominado!' 
    }

    // Exercício 4
    function alternarEstado() {
        // Seu código aqui
        let item = document.getElementById('texto-estado')
        let text = item.innerText
        if (text === 'Ligado'){
            item.innerText = 'Desligado'
        }
        else{
            item.innerText = 'Ligado'
        }
    }

    // Exercício 5
    let valorContador = 10;
    function contagemRegressiva() {
        // Seu código aqui
        let item = document.getElementById('visor-contador')
        let num = parseInt(item.innerText)
        if (num === 0){
            alert(`Fim do tempo!`)
        }
        else{
            item.innerText = num - 1
        }
    }
