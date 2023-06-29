const tareas = window.tareas;

let lastMinute = null;

const modal = document.getElementById('modal');
const modalMessage = document.getElementById('modal-message');
const modalButton = document.getElementById('modal-button');

modalButton.addEventListener('click', () => {
    modal.style.display = 'none';
});

function checkTareas() {
    

    const now = new Date();
    const currentDay = now.getDay();
    const currentMinute = now.getMinutes();

    if (currentMinute !== lastMinute) {
        lastMinute = currentMinute;
        tareas.forEach(tarea => {
            tarea.alertShown = false;
        });
    }
    
    const currentTime = now.toLocaleTimeString('en-US', { hour12: false }).substring(0, 5);
 
    tareas.forEach(tarea => {

        if (tarea.fields.dia === currentDay &&tarea.fields.hora.substring(0, 5) === currentTime && !tarea.alertShown) {
            tarea.alertShown = true;
            modalMessage.textContent = `Es la hora de: ${tarea.fields.titulo}`;
            modal.style.display = 'block';
        }
    });
        
}

setInterval(checkTareas, 1000);