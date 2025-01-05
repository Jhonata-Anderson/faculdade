const receitas = [
    {
        titulo: "Torta de Nutella",
        imagem: "./img/Torta de Nutella.jpeg",
        preparo: "Bata os ovos inteiros por cerca de 6 minutos até que tripliquem de volume. Derreta a Nutella no micro-ondas por 20 segundos para facilitar a mistura e misture em três etapas com os ovos. Despeje a massa em uma forma redonda forrada e asse em forno a 175 graus por 20 a 25 minutos, conferindo com um palito se está pronta. Espere esfriar antes de desenformar.",
        ingredientes: ["4 ovos", "240g de Nutella"]
    },
    {
        titulo: "Beijinho de Leite Ninho",
        imagem: "./img/Beijinho de Leite Ninho.jpeg",
        preparo: "Coloque em uma panela, a manteiga, o leite condensado e leve ao fogo médio. Mexa e vá colocando o leite em pó aos poucos. Você deve mexer sem parar. Depois, desligue o fogo e transfira a massa para um recipiente. Passe um pouco de manteiga em suas mãos para enrolar os docinhos.",
        ingredientes: ["1 lata de leite condensado", "4 colheres (sopa) de leite em pó", "1 colher (sopa) manteiga"]
    },
    {
        titulo: "Mousse de maracujá",
        imagem: "./img/Mousse de maracujá.jpeg",
        preparo: "Bata todos os ingredientes no liquidificador, ou misture com um fouet, até ficar no ponto de cremosidade do seu gosto. Deixe gelar por cerca de 2 horas na geladeira. Aproveite!",
        ingredientes: ["1 lata de leite condensado", "1 copo americano de suco concentrado de maracujá", "1 lata de creme de leite sem soro"]
    }
];

function getListaIngredientes(receita) {
    return `<ul>${receita.ingredientes.map(ingrediente => `<li>${ingrediente}</li>`).join('')}</ul>`;
}

function getCard(receita) {
    return `
        <div class="card" style="width: 250px;">
            <img src="${receita.imagem}" class="card-img-top" alt="${receita.titulo}">
            <div class="card-body">
                <h5 class="card-title">${receita.titulo}</h5>
                <p class="card-text">${getListaIngredientes(receita)}<hr>${receita.preparo}</p>
            </div>
        </div>
    `;
}

function preencheCatalogo() {
    const pnlCatalogo = document.getElementById('pnlCatalogo');
    pnlCatalogo.innerHTML = receitas.map(receita => getCard(receita)).join('');
}

window.onload = preencheCatalogo;