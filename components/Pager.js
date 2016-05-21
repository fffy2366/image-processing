var logger = require('./../config/Logger') ;
//var req = require('request') ;
//var url = request.originalUrl;
//logger.info("url:"+url) ;
/**
 * 分页
 */
var pager = function(req, totalCount, pageSize, currPage){
	var output = "" ;
	var param_name = "page" ;
	var totalPage = !!totalCount?Math.ceil(totalCount/pageSize):0 ;
	function url(){
		var request_uri = req.originalUrl; ;
		logger.info("request_uri:"+request_uri) ;
		logger.info("currPage:"+currPage) ;
		request_uri = request_uri.replace("&page="+currPage,"").replace("?page="+currPage,"") ;
		logger.info("request_uri:"+request_uri) ;
		if(request_uri.indexOf("?")>-1){
			request_uri = request_uri+"&" ;
		}else{
			request_uri = request_uri+"?" ;
		}
		return request_uri ;	
	}
	//首页 前一页
	function get_first_page(){
		url = url() ;
		output = "<ul class=\"ulfy\">" ;
		output += "<li><a href=\""+url+param_name+"="+1+"\">&lt;&lt;</a></li>" ;
		if(currPage<=1){
			output += "<li><a href=\"javascript:;\">&lt;</a></li>" ;
		}else{
			output += "<li><a href=\""+url+param_name+"="+(currPage-1)+"\">&lt;</a></li>" ;
		}
		return output ;
	}
	/**
	 * 后一页 末页
	 */
	function get_last_page(){
		logger.info("currPage-->:"+currPage) ;
		logger.info("totalPage-->:"+totalPage) ;
		if(currPage>=totalPage){
			output += "<li><a href=\"javascript:;\">&gt;</a></li>" ;
		}else{
			output += "<li><a href=\""+url+param_name+"="+(parseInt(currPage)+1)+"\">&gt;</a></li>" ;
		}
		output += "<li><a href=\""+url+param_name+"="+parseInt(totalPage)+"\">&gt;&gt;</a></li>" ;
		output += "</ul>" ;
		return output ;
	}
	//列表
	function get_list(){
		if(totalPage<=10){
			for(var i=1; i<=totalPage; i++){
				if(i==currPage){
					output += "<li class=\"active\"><a href=\"javascript:;\">"+i+"</a></li>" ;
				}else{
					output += "<li><a href=\""+url+param_name+"="+i+"\">"+i+"</a></li>" ;
				}
			}
		}else{
			for(var i=1;i<=3;i++){
				if(i==currPage){
					output += "<li class=\"active\"><a href=\"javascript:;\">"+i+"</a></li>" ;
				}else{
					output += "<li><a href=\""+url+param_name+"="+i+"\">"+i+"</a></li>" ;
				}
			}
			
			
			if(currPage>5)output += "<li><a>...</a></li>" ;
			if(currPage>4){
				min = currPage-1 ;
			}else{
				min = 4 ;
			}
			if(currPage<totalPage-4){
				max = parseInt(currPage)+2 ;
			}else{
				max = parseInt(totalPage)-2 ;
			}
			//if($max >= $min+2){
				for(var i=min;i<=max-1;i++){
					if(i==currPage){
						output += "<li class=\"active\"><a href=\"javascript:;\">"+i+"</a></li>" ;
					}else{
						output += "<li><a href=\""+url+param_name+"="+i+"\">"+i+"</a></li>" ;
					}
				}						
			//}
				
			if(currPage<totalPage-4)output += "<li><a>...</a></li>" ;					
			
			for(var i=totalPage-2;i<=totalPage;i++){
				if(i==currPage){
					output += "<li class=\"active\"><a href=\"javascript:;\">"+i+"</a></li>" ;
				}else{
					output += "<li><a href=\""+url+param_name+"="+i+"\">"+i+"</a></li>" ;
				}
			}			
		}
		
		return output ;
	}
	get_first_page();
	get_list() ;
	get_last_page() ;
	return output ;
} ;

module.exports = pager;
