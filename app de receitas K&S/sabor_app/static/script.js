async function carregarCatalogo() {
    const resp = await fetch("/api/recipes");
    const data = await resp.json();
    const area = document.getElementById("lista");

    area.innerHTML = "";

    data.forEach(r => {
        area.innerHTML += `
            <div class="card">
                <img src="${r.imagem}">
                <h3>${r.nome}</h3>
                <p>${r.categoria}</p>
            </div>
        `;
    });
}