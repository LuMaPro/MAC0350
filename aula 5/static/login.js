document.getElementById("submit").addEventListener("click", async () => {
    const user = {
        name: document.getElementById('name').value,
        password: document.getElementById('password').value,
        bio: ""
    };

    const resposta = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });

    if (resposta.ok) {
        const resultado = await resposta.json();
        if (resultado.success){
            alert("Usuário " + resultado.user + " logado!");
            window.location.href = "/profile";
        }
        else{
            alert(resultado.error)
        }
    } else {
        alert("Erro ao enviar!");
    }
})