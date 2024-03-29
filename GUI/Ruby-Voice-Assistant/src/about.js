jQuery('document').ready(function(){
	jQuery('#about').hide();

    jQuery('#but_3').on('click', function(){
        jQuery('#about').show();
        jQuery('#all').hide();

    jQuery('#nazad_3').on('click', function(){
        jQuery('#about').hide();
        jQuery('#all').show();
    })

    });

});
