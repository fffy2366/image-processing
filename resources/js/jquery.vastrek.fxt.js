(function($){
	$.extend({
		log: function(str){
			//debug 
			if(typeof($debug)!="undefined"&&$debug==true){
				window.console&&console.log(str) ;
			}
		},
		atCount: function(str){
			//@出现的次数
			return str.replace(/[^@]/g, "").length ;
		},
		getLength: function(str){
			//weibo统计字符个数280
		    var realLength = 0, len = str.length, charCode = -1;
		    for (var i = 0; i < len; i++) {
		        charCode = str.charCodeAt(i);
		        if (charCode >= 0 && charCode <= 128) realLength += 1;
		        else realLength += 2;
		    }
		    return realLength;
		},	
		getRandomNum: function(Min,Max){
			//获取随机数
			var Range = Max - Min; 
			var Rand = Math.random(); 
			return(Min + Math.round(Rand * Range)); 
		},
		openwindow: function(url,name,iWidth,iHeight){
			//js打开新窗口（居中）
			var url; //转向网页的地址;
			var name; //网页名称，可为空;
			var iWidth; //弹出窗口的宽度;
			var iHeight; //弹出窗口的高度;
			var iTop = (window.screen.availHeight-30-iHeight)/2; //获得窗口的垂直位置;
			var iLeft = (window.screen.availWidth-10-iWidth)/2; //获得窗口的水平位置;
			window.open(url,name,'height='+iHeight+',,innerHeight='+iHeight+',width='+iWidth+',innerWidth='+iWidth+',top='+iTop+',left='+iLeft+',toolbar=no,menubar=no,scrollbars=auto,resizeable=no,location=no,status=no');
		},
		checkMobile:function(mobile){
			//check mobile
			if(!mobile.match(/^1[3|4|5|8][0-9]\d{4,8}$/)){
				return false ;
			}else{
				return true ;
			}
		},
		checkEmail:function(email){
			//check email
			var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
			if(reg.test(email)){
				return true ;
			}else{
				return false ;
			}			
		},
		format_number:function(n){
			//return parseFloat(n).toLocaleString() ;//method 1
			var b=parseInt(n).toString();
			var len=b.length;
			if(len<=3){return b;}
			var r=len%3;
			return r>0?b.slice(0,r)+","+b.slice(r,len).match(/\d{3}/g).join(","):b.slice(r,len).match(/\d{3}/g).join(",");			
		},
		findSize:function(field_id){
			var fileInput = $("#"+field_id)[0];
			byteSize  = fileInput.files[0].fileSize;
			return ( Math.ceil(byteSize / 1024) ); // Size returned in KB.
		}	
	});
	//dom tool: char left
	$.fn.charCount = function(options){
		var defaults = {	
			allowed: 140,		
			warning: 25,
			css: 'counter',
			counterElement: 'span',
			cssWarning: 'warning',
			cssExceeded: 'exceeded',
			counterText: ''
		}; 
			
		var options = $.extend(defaults, options); 
		
		function calculate(obj){
			//var count = $(obj).val().length;
			var count = Math.floor($.getLength($(obj).val())/2) ;
			if($.getLength($(obj).val())==281){
				count = 140 ;
			}
			var available = options.allowed - count;
			if(available <= options.warning && available >= 0){
				$(obj).next().addClass(options.cssWarning);
			} else {
				$(obj).next().removeClass(options.cssWarning);
			}
			if(available < 0){
				$(obj).next().addClass(options.cssExceeded);
				options.counterText = "发言请遵守社区公约，已经超过" ;
				available = count - options.allowed
			} else {
				options.counterText = "发言请遵守社区公约，还可以输入" ;
				$(obj).next().removeClass(options.cssExceeded);
			}
			
			$(obj).next().html(options.counterText + "<span class=\"spannum\">"+available+"</span>字");
		};
				
		this.each(function() {  			
			$(this).after('<'+ options.counterElement +' class="' + options.css + '">'+ options.counterText +'</'+ options.counterElement +'>');
			calculate(this);
			$(this).keyup(function(){calculate(this)});
			$(this).change(function(){calculate(this)});
		});
	  
	};

})(jQuery);