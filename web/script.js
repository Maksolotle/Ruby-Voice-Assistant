jQuery('document').ready(function(){
	jQuery('#options').hide();

jQuery('#but_2').on('click', function(){
	
		jQuery('#all').hide();
		jQuery('#options').show();
	
		});

		jQuery('#nazad').on('click', function(){
			jQuery('#options').hide();
			jQuery('#all').show();

		});

	});

});
