// Clase principal para manejar la interactividad de la página
class SoundwaveApp {
    constructor() {
        this.menuCheckbox = document.getElementById('check');
        this.navbar = document.querySelector('.navbar');
        this.infoButtons = document.querySelectorAll('.btn-1');
        this.modal = null;

        // Inicializar funciones de la app
        this.initializeMenu();
        this.initializeInfoButtons();
    }

    // Inicializa el comportamiento del menú
    initializeMenu() {
        // Verifica si hay una preferencia guardada en localStorage
        const isMenuChecked = localStorage.getItem('menuChecked') === 'true';
        this.menuCheckbox.checked = isMenuChecked;
        this.toggleNavbar(isMenuChecked);

        this.menuCheckbox.addEventListener('change', () => {
            this.toggleNavbar(this.menuCheckbox.checked);
            localStorage.setItem('menuChecked', this.menuCheckbox.checked); // Guardar preferencia
        });
    }

    // Función para mostrar u ocultar el menú
    toggleNavbar(isChecked) {
        if (isChecked) {
            this.navbar.style.display = 'flex'; // Muestra el menú en formato flex
        } else {
            this.navbar.style.display = 'none'; // Oculta el menú
        }
    }

    // Inicializa los botones de "Información"
    initializeInfoButtons() {
        this.infoButtons.forEach(button => {
            button.addEventListener('click', (event) => this.handleInfoButtonClick(event));
        });
    }

    // Manejador del clic en los botones de "Información"
    handleInfoButtonClick(event) {
        const eventTitle = event.target.closest('.son-item')?.querySelector('h3')?.textContent || 'Este evento';
        const message = `¡Más información sobre el evento: ${eventTitle}!`;

        this.showModal(message);
    }

    // Función para mostrar un modal con información adicional
    showModal(message) {
        // Si ya existe un modal, no crear uno nuevo
        if (this.modal) return;

        this.modal = document.createElement('div');
        this.modal.classList.add('modal');
        this.modal.innerHTML = `
            <div class="modal-content">
                <p>${message}</p>
                <button class="close-btn">Cerrar</button>
            </div>
        `;

        document.body.appendChild(this.modal);

        // Agregar un manejador de eventos para cerrar el modal
        this.modal.querySelector('.close-btn').addEventListener('click', () => {
            this.closeModal();
        });
    }

    // Función para cerrar el modal
    closeModal() {
        if (this.modal) {
            this.modal.remove();
            this.modal = null; // Liberar el modal para evitar repeticiones
        }
    }
}

// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    const app = new SoundwaveApp(); // Crear una instancia de la app
});
