const planner = document.getElementById("planner");
const dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
const refeicoes = ['Café da manhã', 'Almoço', 'Jantar'];

dias.forEach(dia => {
  const column = document.createElement("div");
  column.classList.add("day-column");

  const heading = document.createElement("h3");
  heading.textContent = dia;
  column.appendChild(heading);

  refeicoes.forEach(refeicao => {
    const block = document.createElement("div");
    block.classList.add("meal-block");
    block.onclick = () => {
      const item = prompt(`O que você vai comer no ${refeicao} de ${dia}?`);
      if (item) {
        block.querySelector(".drop-zone").textContent = item;
      }
    };

    const title = document.createElement("h4");
    title.textContent = refeicao;
    const zone = document.createElement("div");
    zone.classList.add("drop-zone");
    zone.textContent = "Drop meal here";

    const plus = document.createElement("div");
    plus.classList.add("add-button");
    plus.textContent = "+";

    block.appendChild(title);
    block.appendChild(zone);
    block.appendChild(plus);
    column.appendChild(block);
  });

  planner.appendChild(column);
});
