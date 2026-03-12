document.getElementById("submit").addEventListener("click", async () => {
    const user = {
        name: document.getElementById('name').value,
        password: document.getElementById('password').value,
        bio: document.getElementById('bio').value
    };

    if (user.name.length == 0 || user.password.length == 0){
        alert("Preencha os campos de nome e senha!")
        return
    }

    const resposta = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });

    if (resposta.ok) {
        const resultado = await resposta.json();
        if (resultado.success){
            alert("Usuário " + resultado.user + " criado!");
            window.location.href = "/login";
        }
        else{
            alert("Usuário " + resultado.user + " já registrado!");
        }
    } else {
        alert("Erro ao enviar!");
    }
})