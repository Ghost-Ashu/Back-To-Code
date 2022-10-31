import Resultado from "../events/resultado.js";
import Div from "../htmlElements/div.js";

export default class Calculadora{
    carregar = () =>{
        let index  = document.getElementById("index");

        let visor = new Div().criarDivComInput({
            id: "Visor",
            class: "",
            position: "absolute",
            marginTop: "10px",
            marginLeft: "10px",
            text: "Visor: ",
            type: "text"
        });
        
        index.append(visor);

        let button0 = new Div().criarDivComButton({
            id: "0",
            class: "",
            position: "absolute",
            marginTop: "125px",
            marginLeft: "40px",
            text: "0"
        });

        let button1 = new Div().criarDivComButton({
            id: "1",
            class: "",
            position: "absolute",
            marginTop: "50px",
            marginLeft: "10px",
            text: "1"
        });

        let button2 = new Div().criarDivComButton({
            id: "2",
            class: "",
            position: "absolute",
            marginTop: "50px",
            marginLeft: "40px",
            text: "2"
        });

        let button3 = new Div().criarDivComButton({
            id: "3",
            class: "",
            position: "absolute",
            marginTop: "50px",
            marginLeft: "70px",
            text: "3"
        });

        let button4 = new Div().criarDivComButton({
            id: "4",
            class: "",
            position: "absolute",
            marginTop: "75px",
            marginLeft: "10px",
            text: "4"
        });

        let button5 = new Div().criarDivComButton({
            id: "5",
            class: "",
            position: "absolute",
            marginTop: "75px",
            marginLeft: "40px",
            text: "5"
        });

        let button6 = new Div().criarDivComButton({
            id: "6",
            class: "",
            position: "absolute",
            marginTop: "75px",
            marginLeft: "70px",
            text: "6"
        });

        let button7 = new Div().criarDivComButton({
            id: "7",
            class: "",
            position: "absolute",
            marginTop: "100px",
            marginLeft: "10px",
            text: "7"
        });

        let button8 = new Div().criarDivComButton({
            id: "8",
            class: "",
            position: "absolute",
            marginTop: "100px",
            marginLeft: "40px",
            text: "8"
        });

        let button9 = new Div().criarDivComButton({
            id: "9",
            class: "",
            position: "absolute",
            marginTop: "100px",
            marginLeft: "70px",
            text: "9"
        });

        index.append(button0);
        index.append(button1);
        index.append(button2);
        index.append(button3);
        index.append(button4);
        index.append(button5);
        index.append(button6);
        index.append(button7);
        index.append(button8);
        index.append(button9);

        let buttonEmpty = new Div().criarDivComButton({
            id: "Empty",
            class: "",
            position: "absolute",
            marginTop: "160px",
            marginLeft: "10px",
            text: "empty"
        });

        let buttonAdicao = new Div().criarDivComButton({
            id: "Adicao",
            class: "",
            position: "absolute",
            marginTop: "50px",
            marginLeft: "140px",
            text: "+"
        });

        let buttonSubtracao = new Div().criarDivComButton({
            id: "Subtracao",
            class: "",
            position: "absolute",
            marginTop: "50px",
            marginLeft: "170px",
            text: "-"
        });

        let buttonMultiplicacao = new Div().criarDivComButton({
            id: "Multiplicacao",
            class: "",
            position: "absolute",
            marginTop: "75px",
            marginLeft: "140px",
            text: "*"
        });

        let buttonDivisao = new Div().criarDivComButton({
            id: "Divisao",
            class: "",
            position: "absolute",
            marginTop: "75px",
            marginLeft: "170px",
            text: "/"
        });

        let buttonIgualdade = new Div().criarDivComButton({
            id: "Igualdade",
            class: "",
            position: "absolute",
            marginTop: "100px",
            marginLeft: "155px",
            text: "="
        });

        index.append(buttonEmpty);
        index.append(buttonAdicao);
        index.append(buttonSubtracao);
        index.append(buttonMultiplicacao);
        index.append(buttonDivisao);
        index.append(buttonIgualdade);

        button0.addEventListener("click", ()=>{
            visor.lastChild.value += "0";
        });

        button1.addEventListener("click", ()=>{
            visor.lastChild.value += "1";
        });

        button2.addEventListener("click", ()=>{
            visor.lastChild.value += "2";
        });

        button3.addEventListener("click", ()=>{
            visor.lastChild.value += "3";
        });

        button4.addEventListener("click", ()=>{
            visor.lastChild.value += "4";
        });

        button5.addEventListener("click", ()=>{
            visor.lastChild.value += "5";
        });

        button6.addEventListener("click", ()=>{
            visor.lastChild.value += "6";
        });

        button7.addEventListener("click", ()=>{
            visor.lastChild.value += "7";
        });

        button8.addEventListener("click", ()=>{
            visor.lastChild.value += "8";
        });

        button9.addEventListener("click", ()=>{
            visor.lastChild.value += "9";
        });

        buttonEmpty.addEventListener("click", ()=>{
            visor.lastChild.value = "";
        });

        buttonAdicao.addEventListener("click", ()=>{
            visor.lastChild.value += "+";
        });

        buttonSubtracao.addEventListener("click", ()=>{
            visor.lastChild.value += "-";
        });

        buttonMultiplicacao.addEventListener("click", ()=>{
            visor.lastChild.value += "*";
        });

        buttonDivisao.addEventListener("click", ()=>{
            visor.lastChild.value += "/";
        });

        buttonIgualdade.addEventListener("click", ()=>{
            visor.lastChild.value = new Resultado(visor.lastChild.value).getVisor();
        });
    }

}