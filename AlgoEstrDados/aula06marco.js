/*let permissao; //vendedor, gerente; diretor
permissao = 'vendedor';
switch (permissao) {
    case 'comum':
        console.log('usuário local')
        break;

    case 'gerente':
        console.log('usuário regional')
        break;

    case 'diretor':
        console.log('usuário total')
        break;

    default:
        console.log('Usuario não reconhecido!')
}

let permissao
permissao = 'caixa'


if (permissao == 'vendedor') {
    console.log('acesso local')
} else if (permissao == 'gerente') {
    console.log('acesso regional')
} else if (permissao == 'diretor') {
    console.log('acesso total')
} else {
    console.log('Usuário não reconhecido!')
}
*/
// Exemplo de uso do switch

const fruta = "Bananas";
switch (fruta) {
  case "Laranjas":
    console.log("As laranjas custam $0.59 o quilo.");
    break;
  case "Maçãs":
    console.log("Maçãs custam $0.32 o quilo.");
    break;
  case "Bananas":
    console.log("Bananas custam $0.48 o quilo.");

    break;
  case "Cerejas":
    console.log("Cerejas custam $3.00 o quilo.");
    break;
  case "Mangas":
  case "Mamões":
    console.log("Mangas e mamões custam $2.79 o quilo.");
    break;
  default:
    console.log("Fruta não encontrada.");
}
