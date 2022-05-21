// Get the modal
const modal = document.getElementById('dialogueModal');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


document.getElementById('wallet-address').readOnly = true;
