import TextNode from "./text_node.js";

export default class Label{
    criar = (props) =>{
        let label = document.createElement("label");
        
        if(props.id){
            label.setAttribute("id", "label"+props.id);
        }
    
        let text = new TextNode().criar({text: props.text});
    
        label.append(text);
    
        return label;
    }
}