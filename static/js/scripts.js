function showPleaseWait() {
    var modalLoading = '<div class="modal" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false" role="dialog">\
        <div class="modal-dialog modal-sm center" style="top:40%;left:40%;position:fixed;color:white">\
            <span class="fa fa-spinner fa-spin fa-4x"></span>\
        </div>\
    </div>';
    $(document.body).append(modalLoading);
    $("#pleaseWaitDialog").modal("show");
}

$(".wait").click(function(){
    showPleaseWait();
});

$(document).ready(function(){
    if(!window.location.hash) {
        $(this).scrollTop(0);
    }
});

function readURL(input,id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.preview-'+id).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }    
}
$(".hasToChange").change(function(){
    var id = $(this).data("id")
    readURL(this,id);
});


function showPrompt(lg_ch,text,link,color) {
    lang_yes = {
        "HT":"Wi",
        "FR":"Oui",
        "EN":"Yes",
    };
    lang_no = {
        "HT":"Non",
        "FR":"Non",
        "EN":"No",
    };
    var modalLoading = '<div class="modal fade in" id="prompt-confirm">\
        <div class="modal-dialog modal-sm">\
            <div class="modal-content">\
                <div class="modal-header">\
                    <button type="button" class="close" data-dismiss="modal">&times;</button>\
                    <h4 class="modal-title text-'+color+'" style="text-align:center"><span class="glyphicon glyphicon-alert"></span> '+text+'<br>\
                    </h4>\
                </div>\
                <div class="modal-body">\
                    <div class="row" style="text-align:center">\
                        <div class="col-sm-6">\
                            <a href="'+link+'" class="btn btn-default btn-block wait"><span class="glyphicon glyphicon-ok"></span> '+lang_yes[lg_ch]+'</a>\
                        </div>\
                        <div class="col-sm-6">\
                            <button class="btn btn-default btn-block" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> '+lang_no[lg_ch]+'</button>\
                        </div>\
                    </div>\
                </div>\
            </div>\
        </div>\
    </div>';
    $(document.body).append(modalLoading);
    $("#prompt-confirm").modal("show");
}
$(".prompt").click(function(){
    var link = $(this).data("link"),
        lg_ch = $(this).data("lg_ch"),
        text = $(this).data("text"),
        color = $(this).data("color");

    showPrompt(lg_ch,text,link,color);
});

$(".only_number").bind('keypress', function(e){
    if(e.keyCode == 8 || e.keyCode == 9){
        return true;
    }
    if(isNumberKey(e)){
        return true;
    }else{
        return false;
    }
});
$(".only_number_plus").bind('keypress', function(e){
    if(e.keyCode == 8 || e.keyCode == 9 || e.which == 43){
        return true;
    }
    if(isNumberKey(e)){
        return true;
    }else{
        return false;
    }
});

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode;
    if((charCode < 48 || charCode > 57))
        return false;
    return true;
}




$(document).on("click",".path-next",function(){
    var url = $(this).data('href');
    if(typeof(url) !== 'undefined')
        window.location.href = url;
});

$(document).ready(function () {
    var time = 10000

    function carouselRun(time){
        // Launch the carousel
        $('.carousel').carousel({
            interval: time
        });
        $('.carousel').carousel('cycle');
    }


    carouselRun(time);


    $(document).on("mousemove",function(){
        // We clear the time
        clearTimeout(time);

        // We call it again if the mouse doesn't move
        setTimeout(function(){
            carouselRun(time);
        }, 3000);
    })


    $("#connexion").on("shown.bs.modal",function(){
        $("#input-connexion").focus();
    });
});




$(function () {
    $('.button-checkbox').each(function () {

        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:radio'),
            color = $button.data('color'),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };

        // Event Handlers
        $button.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Set the button's icon
            $button.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$button.data('state')].icon);

            // Update the button's color
            if (isChecked) {
                $button
                    .removeClass('btn-default')
                    .addClass('btn-' + color + ' active');
            }
            else {
                $button
                    .removeClass('btn-' + color + ' active')
                    .addClass('btn-default');
            }
        }

        // Initialization
        function init() {

            updateDisplay();

            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i> ');
            }
        }
        init();
    });
});
