export default class Resultado{
    constructor(props){
        this.visor = props;
    }

    calcularResultado= () =>{
        let vals = this.visor.split(new RegExp("(?=[*/+-])|(?<=[*/+-])"));
        
        function resolver(operador1, operador2, valores){
            let index1 = valores.indexOf(operador1);
            let index2 = valores.indexOf(operador2);

            while ( index1 != -1 || index2 != -1){
                let indexOperacao;
                if (index1 != -1 && (index1 < index2 || index2 == -1)){
                    indexOperacao = index1;
                }else{
                    indexOperacao = index2;
                }
                
                let val1 = Number(valores[indexOperacao-1]);
                let operador = valores[indexOperacao];
                let val2 = Number(valores[indexOperacao+1]);
                
                switch (operador) {
                    case '+':
                        valores[indexOperacao-1] = val1 + val2;
                        break;
                    case '-':
                        valores[indexOperacao-1] = val1 - val2;
                        break;
                    case '*':
                        valores[indexOperacao-1] = val1 * val2;
                        break;       
                    case '/':
                        valores[indexOperacao-1] = val1 / val2;
                        break;
                }
               
                valores.splice(indexOperacao,2);
                index1 = valores.indexOf(operador1);
                index2 = valores.indexOf(operador2);
            }
            return valores
        }
        vals = resolver("*", "/", vals);
        vals = resolver("+", "-", vals);
        this.visor = vals[0].toString();
    }

    getVisor(){
        this.calcularResultado();
        return this.visor;
    }
}
