jQuery('document').ready(function(){
	jQuery('#commands').hide();

jQuery('#but_1').on('click', function(){
	
	jQuery('#all').hide();
	jQuery('#commands').show();
	jQuery('#razvernut_x').hide();
	jQuery('#razvernut_x_2').hide();
	jQuery('#razvernut_x_3').hide();
	jQuery('#custom_commands').hide();
	jQuery('#razvernut_x_4').hide();
	jQuery('#razvernut_x_5').hide();
	jQuery('#youtube').hide();
	jQuery('#commands_browser').hide();
	jQuery('#open_programs').hide();
	jQuery('#another').hide();

	jQuery('#razvernut_1').on('click', function(){
		jQuery('#custom_commands').show();
		jQuery('#razvernut_1').hide();
		jQuery('#razvernut_x').show();
	})

	jQuery('#razvernut_x').on('click', function(){
		jQuery('#custom_commands').hide();
		jQuery('#razvernut_1').show();
		jQuery('#razvernut_x').hide();
	});

	jQuery('#razvernut_2').on('click', function(){
		jQuery('#commands_browser').show();
		jQuery('#razvernut_2').hide();
		jQuery('#razvernut_x_2').show();
	})

	jQuery('#razvernut_x_2').on('click', function(){
		jQuery('#commands_browser').hide();
		jQuery('#razvernut_2').show();
		jQuery('#razvernut_x_2').hide();
	});
	jQuery('#razvernut_3').on('click', function(){
		jQuery('#open_programs').show();
		jQuery('#razvernut_3').hide();
		jQuery('#razvernut_x_3').show();
	})

	jQuery('#razvernut_x_3').on('click', function(){
		jQuery('#open_programs').hide();
		jQuery('#razvernut_3').show();
		jQuery('#razvernut_x_3').hide();
	});
	jQuery('#razvernut_4').on('click', function(){
		jQuery('#youtube').show();
		jQuery('#razvernut_4').hide();
		jQuery('#razvernut_x_4').show();
	})

	jQuery('#razvernut_x_4').on('click', function(){
		jQuery('#youtube').hide();
		jQuery('#razvernut_4').show();
		jQuery('#razvernut_x_4').hide();
	});
	jQuery('#razvernut_5').on('click', function(){
		jQuery('#another').show();
		jQuery('#razvernut_5').hide();
		jQuery('#razvernut_x_5').show();
	})

	jQuery('#razvernut_x_5').on('click', function(){
		jQuery('#another').hide();
		jQuery('#razvernut_5').show();
		jQuery('#razvernut_x_5').hide();
	});

	jQuery('#nazad_2').on('click', function(){
		jQuery('#commands').hide();
		jQuery('#all').show();

	});

	});

});