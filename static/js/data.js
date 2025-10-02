function data(){
    return{
        modalAddColaborador: false,
        tabColaborador: 'solicitar',
        dropDownHistorico: false,
        carregandoReprovacao: false,
        logout: false,
    }
}


// DESABILITANDO OS BOTÕES DOS FORMULÁRIOS 
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".preventForm").forEach(function (form) {
        form.addEventListener("submit", function (e) {
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
            submitBtn.innerHTML = '<i class="fa-solid fa-rotate-right fa-spin"></i>';
        }
        });
    });
});