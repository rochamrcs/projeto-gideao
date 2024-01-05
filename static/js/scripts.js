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
                $('#id_empilhamento_tipo').val('');
                $('#id_empilhamento_tipo').prop('disabled', false);
                $('#id_empilhamento_tipo option[value="NA"]').prop('disabled', true);
                $('#id_empilhamento_tipo option[value="Normal"]').prop('disabled', false);
                $('#id_empilhamento_tipo option[value="Igrejinha"]').prop('disabled', false);
            } else {
                empilhamentoTipoField.show();
                $('#id_empilhamento_tipo').val('');
                $('#id_empilhamento_tipo option[value="NA"]').prop('disabled', false);
                $('#id_empilhamento_tipo option[value="Normal"]').prop('disabled', true);
                $('#id_empilhamento_tipo option[value="Igrejinha"]').prop('disabled', true);
            }
        });

        // Oculta 'empilhamento_tipo' por padrão
        //empilhamentoTipoField.hide();
        //$('#id_empilhamento_tipo option[value="NA"]').prop('disabled', true);

    var statusField = $('#id_status').closest('.col-12');
    statusField.hide();

    var armazenadoField = $('#id_armazenado').closest('.col-12');
    armazenadoField.hide();

    var ocupacaoField = $('#id_ocupacao').closest('.col-12');
    ocupacaoField.hide();

    var disponibilidadeField = $('#id_disponibilidade').closest('.col-12');
    disponibilidadeField.hide();

});
