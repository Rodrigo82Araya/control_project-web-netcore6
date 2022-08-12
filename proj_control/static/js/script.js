function alertConfirmacion(e, text) {
    e.preventDefault();
    
    var url = e.currentTarget.getAttribute('href');
    Swal.fire({
        title: 'Realmente deseas eliminar ' + text + '?',
        text: "Esto no se podra revertir!",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        
        if (result.value) {
            window.location.href=url;
        }else {
            return false;
        }
    })
}

// function alertExito(e){
//     Swal.fire({
//         title: 'Realmente deseas eliminar esta orden?',
//         text: "Esto no se podra revertir!",
//         icon: 'success',
//     })  
// }