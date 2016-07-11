	$(function(){
		$('#create_date').datetimepicker({
			//inline: true,
			dateFormat: 'yy-mm-dd',
			timeFormat: "HH:mm:ss",
			maxDate:"+0m +0w"
		});

		uploadImage("#imgTitle","photo") ;

		$("#signBtn").click(function(){
			signSubmit() ;
		}) ;

	}) ;
	/**
	 * id:#id
	 * type:存储目录名
	 */
	function uploadImage(id,type){
	    var upload = new AjaxUpload(jQuery(id), {
		    action: '/upload',
		    name: 'upfile',
		    data: {
		        'limitMaxSize': "1"
		    },
		    autoSubmit: true,
		    responseType: 'json',
		    onChange: function(file, ext){
		    	$("#msg").html('') ;
		    },
		    onSubmit: function(file, ext){
		        // Allow only images. You should add security check on the server-side.
		        if (ext && /^(gif|jpg|png|jpeg)$/i.test(ext)) {
		            this.setData({
		                'limitMaxSize': '2',
		                'type':type,
		                'key2': '...'
		            });
		            //loading
		            $(id+"_loading").html("<img src=\"/resources/js/fileuploader/loading.gif\"/>") ;
		        } else {
		            alert("上传文件类型不正确") ;
		            return false;
		        }                            
		    },
		    onComplete: function(file, response){
		        //this.disable();
		        //loading
		        $(id+"_loading").empty() ;
		        
		        if(response.status == "y"){
					$(id+"_img").html("<img style=\"height:180px\" src=\"/uploads/"+type+"/"+response.filename+"\"/>") ;
					$(id+"_inp").val(file) ;
					$(id+"_filename").val(response.filename) ;
		        }
		        if(response.status == "n"){
		        	alert(response.info) ;
		        }
                if(response.msg &&response.msg!=""){
                    $("#msg").html(unescape(response.msg)) ;
                }
		    }
		});
	}    	


	$(function(){
		
	}) ;


var uploader = new plupload.Uploader({ //实例化一个plupload上传对象
		browse_button : 'browse',
		url : '/plupload',
		flash_swf_url : '/resources/js/Moxie.swf',
		silverlight_xap_url : '/resources/js/Moxie.xap',
		drop_element : 'drag-area'
	});
	uploader.init(); //初始化
	//绑定文件添加进队列事件
	uploader.bind('FilesAdded',function(uploader,files){
		for(var i = 0, len = files.length; i<len; i++){
			var file_name = files[i].name; //文件名
			//构造html来更新UI
			var html = '<li id="file-' + files[i].id +'"><p class="file-name">' + file_name + '</p><p class="progress"></p></li>';
			$(html).appendTo('#file-list');
		}
	});

	//绑定文件上传进度事件
	uploader.bind('UploadProgress',function(uploader,file){
		$('#file-'+file.id+' .progress').css('width',file.percent + '%');//控制进度条
	});

	//上传按钮
	$('#upload-btn').click(function(){
		uploader.start(); //开始上传
	});

var signSubmit = function(){
	var username = $("input[name='username']").val() ;
	var mobile = $("input[name='mobile']").val() ;
	var address = $("input[name='address']").val() ;
	var photo = $("#imgTitle_filename").val() ;

	if(username==""){
		alert("请填写姓名") ;
		return ;
	}
	if(mobile==""){
		alert("请填写电话") ;
		return ;
	}
	if(address==""){
		alert("请填写常住城市") ;
		return ;
	}
	if(photo==""){
		alert("请上传近照") ;
		return ;
	}
	$.post("/sign",{"username":username,"mobile":mobile,"address":address,"photo":photo},function(data){
		if(data.status=="y"){
			alert("报名成功") ;
			$("#signForm")[0].reset() ;
			$("#imgTitle_inp").val('') ;
			$("#imgTitle_img").empty() ;
		}else{
			alert("报名失败") ;
		}
	}) ;
}
