// Realiza uma requisição GET para a API que retorna os tipos de passos
fetch('/TiposPassos/')
    .then(response => {
        // Verifica se a resposta foi bem-sucedida (código de status 200)
        if (response.ok) {
            // Converte a resposta para JSON
            return response.json();
        } else {
            // Lança um erro se a resposta não for bem-sucedida
            throw new Error('Erro ao obter os tipos de passos');
        }
    })
    .then(data => {
        // Manipula os dados recebidos
        // Supondo que 'data' seja uma lista de tipos de passos

        // Preenche a grid na página HTML com os tipos de passos
        const grid = document.getElementById('grid');
        data.forEach(tipoPasso => {
            const tipoPassoRow = document.createElement('tr');
            
            const idCell = document.createElement('td');
            idCell.textContent = tipoPasso.ID_Tipo_Passo;
            tipoPassoRow.appendChild(idCell);
            
            const nomeCell = document.createElement('td');
            nomeCell.textContent = tipoPasso.Ds_Tipo_Passo;
            tipoPassoRow.appendChild(nomeCell);

            // Adicione mais colunas conforme necessário
            grid.appendChild(tipoPassoRow);
        });
    })
    .catch(error => {
        // Captura e trata quaisquer erros ocorridos durante a solicitação
        console.error('Erro ao obter os tipos de passos:', error);
    });
