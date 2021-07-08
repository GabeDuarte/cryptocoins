const cardsCriptos = document.getElementsByClassName("cripto");

const criptoSelecionada = document.getElementById("saibamais");
console.log(criptoSelecionada);

for(let el of cardsCriptos){
   el.onmouseover = function(){
       let itens = el.children;
       for(let i of itens){
           if(i.getAttribute("id") == "saibamais"){
               i.classList.add("apareceBtn");
               el.classList.add("desfocaFundo");
           }
            
            else{
                i.classList.add("desaparece");
            }
       }
   }
}


for(let el of cardsCriptos){
    el.onmouseout = function(){
        let itens = el.children;
        for(let i of itens){
            if(i.getAttribute("id") == "saibamais"){
                i.classList.remove("apareceBtn");
            }else{
             i.classList.remove("desaparece");
            }
        }
    }
 }






function alerta(){
    alert("Tem certeza que quer excluir?")
}