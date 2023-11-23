$(document).ready(function(){
    $('#btn-sim').click(function(){
        var url = $(this).data('url');
        window.location.href = url;
    });

    var empilhamentoField = $('#id_empilhamento');
    var empilhamentoTipoField = $('#id_empilhamento_tipo').closest('.col-12');

    empilhamentoField.change(function(){
        var empilhamentoValue = $(this).val();
        if (empilhamentoValue === 'Sim') {
            empilhamentoTipoField.show();
            $('#id_empilhamento_tipo option[value="NA"]').prop('disabled', true);
            $('#id_empilhamento_tipo option[value="NA"]').prop('selected', false);
        } else {
            empilhamentoTipoField.hide();
            $('#id_empilhamento_tipo option[value="NA"]').prop('selected', true);
        }
    });

    // Oculta 'empilhamento_tipo' por padrão
    empilhamentoTipoField.hide();

});