(function($){
	$debug = true ;
	//日期选择
	$(function(){
		var from = $("#from").val() ;
		var to = $("#to").val() ;
		$('#fromDate').datepicker({
			inline: true,
			dateFormat: 'yy-mm-dd',
			maxDate:"+0m +0w",
			defaultDate:from ,
			onSelect:function(dateText,inst){
				$('#toDate').datepicker('option','minDate', new Date(dateText.replace('-',',')));
				var fromday = $("#fromDate").datepicker('getDate').getDate();                 
	            var frommonth = $("#fromDate").datepicker('getDate').getMonth() + 1;             
	            var fromyear = $("#fromDate").datepicker('getDate').getFullYear();
	            frommonth = String(frommonth).length==1?"0"+frommonth:frommonth ;
	            fromday = String(fromday).length==1?"0"+fromday:fromday ;
	            var fromDate = fromyear + "-" + frommonth + "-" + fromday;
	            $("#from").val(fromDate) ;
	            $("#from_date").val(fromDate) ;
	            
			}		
		});
		$('#toDate').datepicker({
			inline: true,
			dateFormat: 'yy-mm-dd',
			maxDate:"+0m +0w",
			defaultDate:to ,
			onSelect:function(dateText,inst){
				$('#fromDate').datepicker('option','maxDate',new Date(dateText.replace('-',',')));
				//alert(1) ;
				//$.log(dateText) ;
				//$.log(inst) ;
				var fromday = $("#fromDate").datepicker('getDate').getDate();                 
	            var frommonth = $("#fromDate").datepicker('getDate').getMonth() + 1;             
	            var fromyear = $("#fromDate").datepicker('getDate').getFullYear();
	            frommonth = String(frommonth).length==1?"0"+frommonth:frommonth ;
	            fromday = String(fromday).length==1?"0"+fromday:fromday ;
	            var fromDate = fromyear + "-" + frommonth + "-" + fromday;

				var today = $("#toDate").datepicker('getDate').getDate();                 
	            var tomonth = $("#toDate").datepicker('getDate').getMonth() + 1;             
	            var toyear = $("#toDate").datepicker('getDate').getFullYear();
	            tomonth = String(tomonth).length==1?"0"+tomonth:tomonth ;
	            today = String(today).length==1?"0"+today:today ;
	            var toDate = toyear + "-" + tomonth + "-" + today;
	            $.log(tomonth) ;
				//$.log(fromDate) ; 
				//$.log(toDate) ; 
				
				$("#from").val(fromDate) ;
				$("#to").val(toDate) ;
				$("#to_date").val(toDate) ;
			}
		});
		//apply
		$("#apply").click(function(){
			var fromDate = $("#from").val() ;
			var toDate = $("#to").val() ;
			date_redirect_url = typeof(date_redirect_url)=="undefined"?"":date_redirect_url ;
			window.location.href=date_redirect_url+"?from="+fromDate+"&to="+toDate ;
		}) ;
		//cancel
		$("#cancel").click(function(){
			$("#J_ID-menu_list").hide() ;
		}) ;
	}) ;
	//监测图表
	var from = $("#from").val() ;
	var to = $("#to").val() ;
	var dealerId = $("#dealerId").val() ;
	$(function () {
		type = "pv" ;
		$.ajax({
			url:"./statisticsAction.php?action=linetype",
			type:"post",
			dataType:"json",
			data:{"from":from,"to":to,"type":type,"dealerId":dealerId,"rand":Math.random()},
			success:function(msg){
				$.log(msg) ;
				$.log("msg.date:"+msg.date) ;
				$.log(msg.data) ;
				var dataArr = msg.data ;
				chart(type,"访问次数",msg.date,dataArr) ;
			}
		}) ;
		$.ajax({
			url:"./statisticsAction.php?action=pietype",
			type:"post",
			dataType:"json",
			data:{"from":from,"to":to,"type":"os","dealerId":dealerId,"rand":Math.random()},
			success:function(msg){
				$.log(msg) ;
				var dataArr = msg.data ;
				pie("设备类型",dataArr) ;
				$.log(dataArr) ;
				$.log("dataArr:"+dataArr) ;
			}
		}) ;
		$("input[name='linetype']").click(function(){
			var type = $(this).val() ;
			$.log(type) ;
			if(type=="pv"){
				title = "访问次数" ;
			}else if(type=="code"){
				title = "获取验证码人数" ;
			}else if(type=="login"){
				title = "登录人数" ;
			}else if(type=="click"){
				title = "广告点击人数" ;
			}
			$.ajax({
				url:"./statisticsAction.php?action=linetype",
				type:"post",
				dataType:"json",
				data:{"from":from,"to":to,"type":type,"dealerId":dealerId,"rand":Math.random()},
				success:function(msg){
					$.log(msg) ;
					$.log("msg.date:"+msg.date) ;
					$.log(msg.data) ;
					var dataArr = msg.data ;
					if(dataArr==""){
						$.Showmsg("该类型在时间段内没有数据") ;
					}
					chart(type,title,msg.date,dataArr) ;
				}
			}) ;
		}) ;
		$("input[name='pietype']").click(function(){
			var type = $(this).val() ;
			if(type=="os"){
				title = "设备类型" ;
			}else if(type=="browser"){
				title = "浏览器" ;
			}else if(type=="screen"){
				title = "屏幕" ;
			}
			$.log(type) ;
			$.ajax({
				url:"./statisticsAction.php?action=pietype",
				type:"post",
				dataType:"json",
				data:{"from":from,"to":to,"type":type,"dealerId":dealerId,"rand":Math.random()},
				success:function(msg){
					$.log(msg) ;
					$.log("msg.date:"+msg.date) ;
					$.log(msg.data) ;
					var dataArr = msg.data ;
					if(dataArr==""){
						$.Showmsg("该类型在时间段内没有数据") ;
					}
					pie(title,dataArr) ;
				}
			}) ;
		}) ;
	});
	/**
	 * 线形图
	 */
	function chart(type,title,dateArr,dataArr){
		if($('#container').length==0){
			return ;
		}
		
		type = type.toUpperCase() ;
	    $('#container').highcharts({
	        chart: {
	            type: 'line',
	            marginRight: 30,
	            marginBottom: 35
	        },
	        title: {
	            text: title,
	            x: -20 //center
	        },
	        subtitle: {
	            text: '',
	            x: -20
	        },
	        xAxis: {
	            categories: dateArr,
	            tickInterval: dateArr.length>10?Math.round(dateArr.length/5):1,
	            labels:{
	            	rotation:0,
	            	x:0,
	            	y:20
	            }
	        },
	        yAxis: {
	            min: 0, 
	            title: {
	                text: '',
	                rotation:0
	            },
	            plotLines: [{
	                value: 0,
	                width: 1,
	                color: '#808080'
	            }]
	        },
	        tooltip: {
	            valueSuffix: ''//单位
	        },
	        legend: {
	            layout: 'vertical',
	            align: 'right',
	            verticalAlign: 'top',
	            x: -10,
	            y: 100,
	            borderWidth: 0
	        },
	        series: [{
	            name: type,
	            data: dataArr,
	            showInLegend: false
	        }]
	    });	
	}
	/**
	 * 饼图
	 */
	function pie(title,dataArr) {
        $('#pie').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: title
            },
            tooltip: {
        	    pointFormat: '{series.name}: <b>{point.percentage}%</b>',
            	percentageDecimals: 1
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        color: '#000000',
                        connectorColor: '#000000',
                        formatter: function() {
                            return '<b>'+ this.point.name +'</b>: '+ this.percentage.toFixed(1) +' %';
                        }
                    }
                }
            },
            series: [{
                type: 'pie',
                name: '百分比',
                data: dataArr
            }]
        });
		/*
		{
			name: 'Chrome',
			y: 12.8,
			sliced: true,
			selected: true
        }
		*/
    }
    
    
})(jQuery)