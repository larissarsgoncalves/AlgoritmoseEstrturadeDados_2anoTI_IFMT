function calculateIMC(pessoa) {
const IMC = pessoa.peso / (pessoa.altura * pessoa.altura);
const resultado = `O IMC de ${pessoa.nome} é ${IMC.toFixed(2)}`;
const saudavel = IMC < 25 && IMC > 18.5;

return {
nome: pessoa.nome,
imc: IMC,
resultado: resultado,
saudavel: saudavel
};
}

const pessoa1 = {
    nome: "João",
    peso: 70,
    altura: 1.75
    };

    
    
console.log(calculateIMC(pessoa1));
