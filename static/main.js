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
    $('.show-def').on('click', function(){
        $('.td-def').attr('style', 'visibility:initial');
    });

};

// attach ready event
$(document)
    .ready(voca.basic.ready)
;