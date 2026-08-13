class CrudAPI {
  constructor() {
    // Array para armazenar os registros
    this.dados = [];

    this.id = 1;

    const livros = [
      { titulo: "Dom Casmurro", paginas: 256, autor: "Machado de Assis", id_genero: 100 },
      { titulo: "Memórias Póstumas de Brás Cubas", paginas: 208, autor: "Machado de Assis", id_genero: 100 },
      { titulo: "Quincas Borba", paginas: 224, autor: "Machado de Assis", id_genero: 100 },

      { titulo: "O Cortiço", paginas: 272, autor: "Aluísio Azevedo", id_genero: 100 },
      { titulo: "Casa de Pensão", paginas: 336, autor: "Aluísio Azevedo", id_genero: 100 },

      { titulo: "Vidas Secas", paginas: 176, autor: "Graciliano Ramos", id_genero: 101 },
      { titulo: "São Bernardo", paginas: 224, autor: "Graciliano Ramos", id_genero: 101 },

      { titulo: "Capitães da Areia", paginas: 288, autor: "Jorge Amado", id_genero: 100 },
      { titulo: "Gabriela, Cravo e Canela", paginas: 424, autor: "Jorge Amado", id_genero: 100 },

      { titulo: "A Hora da Estrela", paginas: 96, autor: "Clarice Lispector", id_genero: 102 },
      { titulo: "Perto do Coração Selvagem", paginas: 208, autor: "Clarice Lispector", id_genero: 102 },

      { titulo: "Iracema", paginas: 160, autor: "José de Alencar", id_genero: 100 },
      { titulo: "Senhora", paginas: 192, autor: "José de Alencar", id_genero: 100 },

      { titulo: "O Pequeno Príncipe", paginas: 96, autor: "Antoine de Saint-Exupéry", id_genero: 103 },
      { titulo: "Harry Potter e a Pedra Filosofal", paginas: 264, autor: "J. K. Rowling", id_genero: 104 },
      { titulo: "Harry Potter e a Câmara Secreta", paginas: 288, autor: "J. K. Rowling", id_genero: 104 },

      { titulo: "O Hobbit", paginas: 336, autor: "J. R. R. Tolkien", id_genero: 104 },
      { titulo: "A Sociedade do Anel", paginas: 576, autor: "J. R. R. Tolkien", id_genero: 104 },

      { titulo: "1984", paginas: 328, autor: "George Orwell", id_genero: 105 },
      { titulo: "A Revolução dos Bichos", paginas: 152, autor: "George Orwell", id_genero: 105 }
    ];

    livros.forEach(livro => {
      this.dados.push({ id: this.id++, ...livro });
    });
  }

  // Método para criar um novo registro
  async criar(registro) {
    return new Promise((resolve) => {
      setTimeout(() => {
        const novoRegistro = { id: this.id++, ...registro };
        this.dados.push({ ...novoRegistro }); 
        resolve({ ...novoRegistro }); 
      }, 100);
    });
  }

  // Método para ler todos os registros
  async lerTodos() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(this.dados.map(item => ({ ...item })));
      }, 100);
    });
  }

  // Método para ler um registro específico pelo ID
  async lerPorId(id) {
    return new Promise((resolve) => {
      setTimeout(() => {
        const registro = this.dados.find(item => item.id === id);
        resolve(registro ? { ...registro } : null);
      }, 100);
    });
  }

  // Lista de gêneros
  async listaGeneros() {
    return new Promise((resolve) => {
      setTimeout(() => {
        const generos = [
          { id: 100, nome: "Romance" },
          { id: 101, nome: "Regionalismo" },
          { id: 102, nome: "Literatura Intimista" },
          { id: 103, nome: "Infantil" },
          { id: 104, nome: "Fantasia" },
          { id: 105, nome: "Distopia" }
        ];

        resolve(generos.map(genero => ({ ...genero })));
      }, 100);
    });
  }
}

export default new CrudAPI();