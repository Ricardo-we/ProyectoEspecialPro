const messageDisplayer = document.getElementById('messagesDisplayer');

const form = document.getElementById('messagesForm');

const submitButton = document.getElementById('submitButton');
const loadingIcon = document.getElementById('loading-icon');
const sendIcon = document.getElementById('send-icon');
const messageInput = document.getElementById('messageInput');

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function addLoadingIcon(){
    sendIcon.classList.add('d-none')
    loadingIcon.classList.remove('d-none')
}

function removeLoadingIcon(){
    sendIcon.classList.remove('d-none')
    loadingIcon.classList.add('d-none')
}

function sendMessage(){
    addLoadingIcon();

    const http = new XMLHttpRequest();
    http.open('POST', '/chat/new_message/', true);
    http.setRequestHeader('X-CSRFToken', csrftoken)
    http.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    http.onload = () => {
        if(http.status === 200){
            console.log(http.responseText)
            messageInput.value = ""
            removeLoadingIcon()
        }
    }
    http.send(`username=${window.data.username}&message=${messageInput.value}`)
}


function getMessages(){
    const http = new XMLHttpRequest();
    http.open('GET', '/chat/get_messages/', true);
    http.onload = () => {
        let response = JSON.parse(http.responseText)
        renderMessages(response)
    }
    http.send()
}


function renderMessages(response){
    return new Promise((resolve, reject) => {
        addLoadingIcon()
        resolve(response)
        reject("Hubo un fallo contacta al tal gatito >:3")
    })
    .then((response) => {
        var messageDisplayerTemplate = ""
        
        for(let i in response.usernames){
            messageDisplayerTemplate += `
                <tr class="row form-control">    
                    <td class="row">${response.usernames[i]}</td>
                    <td class="row"><h5>${response.messages[i]}</h5></td>
                </tr>
            `
        }
        messageDisplayer.innerHTML = messageDisplayerTemplate  
        removeLoadingIcon()
    })
    .catch((error) => {
        swal('Ha ocurrido un error', error.message,'error')
    })

}


document.addEventListener('DOMContentLoaded', () =>{
    swal('Este es el chat gatita :3', 'BESHOTE','success')
    removeLoadingIcon();
    messageDisplayer.innerHTML = " <i class='fas fa-spinner fa-spin' style='align-self: center; font-size:20px;'></i>"
    getMessages()

    form.addEventListener('submit', e => {e.preventDefault()});

    submitButton.addEventListener('click', e =>{
        e.preventDefault();
        sendMessage()
    })
    
    setInterval(() =>{
        getMessages()
    }, 1000)

})

