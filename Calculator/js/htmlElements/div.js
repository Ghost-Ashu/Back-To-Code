import Button from "./button.js";
import Label from "./label.js";
import Input from "./input.js";

export default class Div{
    criar = (props) =>{
        let div = document.createElement("div");
    
        if(props.id){
            div.setAttribute("id", props.id);
        }
    
        if(props.class){
            div.setAttribute("class", props.class);
        }
    
        if(props.position){
            div.style.position = props.position;
        }
    
        if(props.marginTop){
            div.style.marginTop = props.marginTop;
        }
    
        if(props.marginLeft){
            div.style.marginLeft = props.marginLeft;
        }
    
        return div;
    }
    
    criarDivComButton = (props) =>{
        let div = this.criar({
            id: "div"+props.id,
            class: props.class,
            position: props.position,
            marginTop: props.marginTop,
            marginLeft: props.marginLeft
        });
    
        let button = new Button().criar({
            id: "button"+props.id,
            text: props.text
            //onclick: props.onclick
        });
    
        div.append(button);
    
        return div;
    }
    
    criarDivComInput = (props) =>{
        let div = this.criar({
            id: props.id,
            class: props.class,
            position: props.position,
            marginTop: props.marginTop,
            marginLeft: props.marginLeft
        });
    
        let label = new Label().criar({
            id: props.id,
            text: props.text
        });
    
        let input = new Input().criar({
            id: props.id,
            placeholder: props.placeholder,
            type: props.type
        });
    
        div.append(label);
        div.append(input);
    
        return div;
    }
}