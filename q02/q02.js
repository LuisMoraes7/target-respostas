// 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

// IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


// let fib = [0,1]
// for (let i =2; i<=n; i++){
//     fib[i] = fib[i-1] + fib[i-2]
//     console.log(fib[i])

// }
function identifyFibonacci(n){
    let valor1 = 5 * (n * n) + 4
    let valor2 = 5 * (n * n) - 4
    let resultado1 = Number.isInteger(Math.sqrt(valor1))
    let resultado2 = Number.isInteger(Math.sqrt(valor2))
    if (resultado1 == true || resultado2 == true){
        return true
    } else{
        return false
    }

}

while (p != 1){
    // let n = ("Digite o número que deseja descobrir se está ou não na sequência de Fibonacci: ")
    resultado = identifyFibonacci(n)
    if (resultado){
        console.log(n + ' está na sequência de Fibonacci!')
        // let p = ('Deseja continuar? [1 para sim e qualquer outra coisa para não]')
    } else{
        console.log(n + ' não está na sequência de Fibonacci!')
        // let p = ('Deseja continuar? [1 para sim e qualquer outra coisa para não]')
    }
}