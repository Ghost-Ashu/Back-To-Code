export default class TextNode{
    criar = (props)=>
    {
        let text;
        if(props.text){
            text = document.createTextNode(props.text);
        }
    
        return text;
    }
}
