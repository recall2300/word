var voca = window.voca || {};
voca.basic = voca.basic || {};
voca.basic.ready = function () {
    $('.ui.dropdown').dropdown({
        onChange: function (value, text, $selectedItem) {
            console.log(value);
            console.log(text);
            console.log($selectedItem);
            console.log($('.word-def'));
        }
    });
    $('.show-def').on('click', function () {
        $('.td-def').attr('style', 'visibility:initial');
    });
    $('.hide-table-head').on('click', function () {
        $('.table-head').attr('style', 'display:none;');
    });
    $('.hide-table-option').on('click', function () {
        $('.table-option').attr('style', 'display:none;');
    });
    $('.hide-write').on('click', function () {
        $('.td-write').attr('style', 'display:none;');
    });
    $('.hide-day').on('click', function () {
        $('.td-day').attr('style', 'display:none;');
    });
    $('.hide-order').on('click', function () {
        $('.td-order').attr('style', 'display:none;');
    });

};

// attach ready event
$(document)
    .ready(voca.basic.ready)
;
