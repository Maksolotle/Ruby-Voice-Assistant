jQuery('document').ready(function(){
	jQuery('#options').hide();

jQuery('#but_2').on('click', function(){
	
		jQuery('#all').hide();
		jQuery('#options').show();


		jQuery('#white').on('click', function(){
			
			document.body.style.backgroundImage = 'url(assets/media/background_white.png)';
			document.body.style.color = 'black';

		});

		jQuery('#black').on('click', function(){
			
			document.body.style.backgroundImage = 'url(assets/media/background.png)';
			document.body.style.color = 'white';


		});

		jQuery('#red').on('click', function(){

			document.body.style.backgroundImage = 'url(assets/media/not_standart_temas/red.png)';
			document.body.style.color = 'white';
		});

		jQuery('#green').on('click', function(){

			document.body.style.backgroundImage = 'url(assets/media/not_standart_temas/green.png)';
			document.body.style.color = 'white';
		});

		jQuery('#violet').on('click', function(){

			document.body.style.backgroundImage = 'url(assets/media/not_standart_temas/violet.png)';
			document.body.style.color = 'white';

		});

		jQuery('#nazad').on('click', function(){
			jQuery('#options').hide();
			jQuery('#all').show();

		});

	});

});