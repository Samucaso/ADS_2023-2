const shoppingCart = [];

function addItemToCart(item){
    shoppingCart.push(item)
}

function removeItemFromCart(item){
    const index = shoppingCart.indexOf(item);
    if(index !== -1){
        shoppingCart.splice(index,1);
    }
}

function listItens(){
    if(shoppingCart.length === 0){
        console.log("Seu carrinho está vazio")
    }
    else{
        console.log("Itens do carrinho: ")
        for(let i = 0; i < shoppingCart.length; i++){
            console.log(`${i + 1}. ${shoppingCart[i]}`)
        }
    }
    
}

function clearCart(){
    shoppingCart.length = 0;
    console.log("Seu carrinho foi esvaziado!")
}

addItemToCart("Item 1")
addItemToCart("Item 2")
addItemToCart("Item 3")
listItens()

removeItemFromCart("Item 2")
listItens()

clearCart()
listItens()