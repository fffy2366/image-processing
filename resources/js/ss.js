// JavaScript Document
$(function(){
	var calenderH = $('#spancalender').next('div.divcalendar').height() + 4;
	var calenderH2 = calenderH + 154;
	$('#spancalender').css({'height':calenderH+'px','line-height':calenderH+'px'});
	$('#J_ID-menu_list').css({'top':calenderH2+'px'});
	$('#J_ID-menu_list').hide();
	$('#J_acalendar').click(function(){
		$('#J_ID-menu_list').toggle();
	});
	
	$('.uldlist').each(function(){
		$(this).find('li:even').addClass('even');
	});
});