console.log("script.js carregado");

document.addEventListener("DOMContentLoaded", () => {
    const sintomas = [
        "Tosse", "Enxaqueca", "Vomito", "Diarreia", "Bulboes", 
        "Anemia", "Dores no corpo", "Inchaco nos olhos", "Paranoia", 
        "Pneumonia", "Espirro", "Desmaio", "Insonia", "Tontura", 
        "Febre", "Perda de memoria"
    ];

    const container = document.getElementById("sintomas-container");

    sintomas.forEach(sintoma => {
        const row = document.createElement("tr");

        const cellSintoma = document.createElement("td");
        cellSintoma.textContent = sintoma;
        
        const cellSelect = document.createElement("td");
        const select = document.createElement("select");
        select.name = sintoma;
        select.innerHTML = `
            <option value="0">Irrelevante</option>
            <option value="1">Médio</option>
            <option value="2">Forte</option>
        `;

        cellSelect.appendChild(select);
        row.appendChild(cellSintoma);
        row.appendChild(cellSelect);
        container.appendChild(row);
    });

    document.getElementById("diagnostico-form").addEventListener("submit", event => {
        event.preventDefault();

        const sintomasSelecionados = {};
        sintomas.forEach(s => {
            sintomasSelecionados[s] = parseInt(document.querySelector(`select[name="${s}"]`).value);
        });

        console.log("Sintomas selecionados:", sintomasSelecionados);

        fetch("http://127.0.0.1:5000/diagnostico", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sintomas: sintomasSelecionados })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Resposta do servidor:", data);
            document.getElementById("resultado").textContent = `Diagnóstico: ${data.diagnostico}`;
        })
        .catch(error => {
            console.error("Erro ao obter diagnóstico:", error);
            alert("Erro ao obter diagnóstico. Verifique o console para mais detalhes.");
        });
    });
});
